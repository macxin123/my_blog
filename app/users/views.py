from flask import render_template, request, flash, jsonify, redirect
from flask_login import login_user, login_required, logout_user
from app.users import users
from app.users import forms


@users.route('/')
def index():
    """首页"""
    return render_template('/users/index.html')


@users.route('/login/', methods=['GET', 'POST'])
def user_login():
    """登录"""
    from app.models import Users

    form = forms.LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        print(1)
        user = Users.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            route = request.args.get('next')
            return redirect(route)
        else:
            flash('用户不存在或者密码错误')

    return render_template('/users/login.html', form=form)


@users.route('/logout/')
def user_logout():
    """退出"""
    logout_user()
    return redirect('/')


@users.route('/change/')
def change_password():
    """修改密码"""
    return render_template('/users/change_password.html')


@users.route('/register/')
def register():
    """注册"""
    form = forms.LoginForm()
    return render_template('/users/register.html', form=form)


@users.route('/email/')
def email():
    """发送验证邮件"""
    return jsonify({'result': 1})

