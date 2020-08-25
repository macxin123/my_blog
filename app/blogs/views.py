from flask import render_template, jsonify, redirect, request
from app.blogs import blogs
from app.blogs.forms import ArticlesForm


@blogs.route('/articles/', methods=['GET', 'POST'])
def articles():
    form = ArticlesForm()
    return render_template('/blogs/articles.html', form=form)


@blogs.route('/articles/save/', methods=['GET', 'POST'])
def save_articles():
    if request.method == 'POST':
        print('*1' * 100)
        content = request.form.get('fancy-editormd-html-code')
        print('content:', content)
    return jsonify({'result': 0})


@blogs.route('/publisher/')
def publish_articles():
    return render_template('/blogs/publisher.html')


@blogs.route('/type/')
def hot_type():
    from app import pymongo
    a_type = pymongo.db.type.find({'type': True})
    print(a_type)
    return jsonify(a_type)