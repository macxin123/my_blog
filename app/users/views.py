from flask import render_template, request, flash, jsonify, redirect
from flask_mail import Message, Mail
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
    form = forms.LoginForm()
    return render_template('/users/change_password.html', form=form)


@users.route('/register/', methods=['GET', 'POST'])
def register():
    """注册"""
    form = forms.RegForm()
    if request.method == 'POST':
        email = form.email.data
        password_1 = form.password_1.data
        password_2 = form.password_2.data
        code = form.code.data
        # print(email)
        # print(password_1)
        # print(password_2)
        # print(code)
    return render_template('/users/register.html', form=form)


@users.route('/email/')
def email():
    """发送验证邮件"""
    if request.method == 'POST':
        pass
    email = request.args.get('email')
    print('1email:', email)
    if not email:
        return jsonify({'result': '邮箱为空'})
    else:
        pass

    return jsonify({'result': 1})

