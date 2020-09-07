from datetime import datetime
from flask import render_template, jsonify, redirect, request
from flask_login import current_user, login_required
from app.blogs import blogs
from app.blogs.forms import ArticlesForm


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
    form = ArticlesForm()
    return render_template('/blogs/details.html/', form=form)


@blogs.route('/articles/save/', methods=['GET', 'POST'])
def save_articles():
    """保存文章接口"""
    if request.method == 'POST':
        content = request.form.get('fancy-editormd-html-code')
        from app.models import Articles
        article = Articles()
        article.title = request.form.get('title')
        article.a_content = content
        article.body = request.form.get('body')
        article.author_id = current_user.id
        article.a_time = datetime.now()
        article.save()
        return redirect('/articles/save/')

    return jsonify({'result': 0})


@blogs.route('/query/')
def query():
    """查询文章标题接口"""
    res = dict()
    from app.models import Articles
    result = Articles.query.all()
    for i in result:
        res[i.id] = {'id': i.id,  'title': i.title, 'body': i.body, 'html': i.a_content}
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
        art.title = request.form.get('title')
        art.update()
        return {'result': 1}
    return {'result': 0}