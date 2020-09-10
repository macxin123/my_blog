from datetime import datetime
from flask import render_template, jsonify, redirect, request
from flask_login import current_user, login_required
from app.blogs import blogs
from app.blogs.forms import ArticlesForm
from app.es import es


@blogs.route('/articles/', methods=['GET', 'POST'])
@login_required
def articles():
    """文章页面"""
    form = ArticlesForm()
    from app.models import Articles
    result = Articles.query.all()
    body = [i.a_content for i in result]
    return render_template('/blogs/articles.html', form=form, body=body)


@blogs.route('/articles/aid/', methods=['GET', 'POST'])
@login_required
def articles_detail():
    """文章详情页面"""
    form = ArticlesForm()
    return render_template('/blogs/details.html/', form=form)


@blogs.route('/articles/save/', methods=['GET', 'POST'])
def save_articles():
    """保存文章接口"""
    if request.method == 'POST':
        # 将文章保存到mysql
        content = request.form.get('fancy-editormd-html-code')
        from app.models import Articles
        article = Articles()
        title = request.form.get('title')
        article.title = title
        article.a_content = content
        body = request.form.get('body')
        article.body = body
        article.author_id = current_user.id
        article.a_time = datetime.now()
        article.save()

        # 再将新文章保存到elasticsearch
        new_id = article.id
        this = Articles.query.get(new_id)
        tmp = dict(zip(this.__dict__.keys(), this.__dict__.values()))
        tmp.pop('_sa_instance_state')
        es.create(index='blogs', id=new_id, doc_type='politics', body=tmp)

        return redirect('/articles/save/')

    return jsonify({'result': 0})


@blogs.route('/query/title/')
def query():
    """查询文章标题接口"""
    res = dict()
    from app.models import Articles
    result = Articles.query.all()
    for i in result:
        res[i.id] = {'id': i.id, 'title': i.title, 'body': i.body, 'html': i.a_content}
    return jsonify(res)


@blogs.route('/publisher/')
def publish_articles():
    """文章功能页面"""
    return render_template('/blogs/publisher.html')


@blogs.route('/alter/title/<id>/', methods=['GET', 'POST'])
def alter_title(id):
    """更新文章标题的接口"""
    from app.models import Articles
    art = Articles.query.get(int(id))
    if request.method == 'POST':
        title = request.form.get('title')
        print('title:', title)

        # mysql更新
        art.title = title
        art.update()

        # elasticsearch更新
        dsl = {
            'query': {
                'match': {
                    'id': int(id)
                }
            }
        }
        res = es.search(index='blogs', doc_type='politics', body=dsl)
        content = res['hits']['hits'][0]['_source']
        content['title'] = title
        r = es.update(index='blogs', id=id, doc_type='politics', body={'doc': content})
        print('r:', r)

        return {'result': 1}

    return {'result': 0}


@blogs.route('/query/blog/', methods=['GET', 'POST'])
def query_blogs():
    """显示在首页的博客接口"""
    dct = dict()
    lst = ['python', '爬虫', 'centos', 'redis']
    for i in lst:
        dsl = {
            'query': {
                'match': {
                    'title': i
                }
            },
            "sort": {
                "good": {
                    "order": "asc"
                }
            },
            'size': 5
        }
        result = es.search(index='blogs', doc_type='politics', body=dsl)
        source = result['hits']['hits']
        dct[i] = source

    return jsonify(dct)


@blogs.route('/del/')
def del_blogs():
    """删除文章接口"""
    from app.models import Articles
    id = request.args.get('id')
    try:
        # mysql删除
        blog = Articles.query.get(int(id))
        blog.delete()
        # elasticsearch删除
        es.delete(index='blogs', doc_type='politics', id=id)
        return jsonify({'result': 1})
    except Exception as e:
        print('e:', e)
        return jsonify({'result': 0, 'error': str(e)})
