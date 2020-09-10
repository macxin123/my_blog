import os
import random
from datetime import datetime
from flask import render_template, request, flash, jsonify, redirect
from werkzeug.security import generate_password_hash
from flask_mail import Message
from flask_login import login_user, login_required, logout_user, current_user
from app.users import users
from app.users import forms


@users.route('/')
def index():
    """首页"""
    return render_template('/users/blog_index.html')


@users.route('/login/', methods=['GET', 'POST'])
def user_login():
    """登录"""
    from app.models import Users, User

    form = forms.LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        this_user = Users.query.filter_by(email=form.email.data).first()
        user = User(this_user)
        if user and user.verif_password(form.password.data):
            login_user(user)
            route = request.args.get('next')
            if route is None:
                return redirect('/')
            else:
                return redirect(route)
        else:
            flash('用户不存在或者密码错误')

    return render_template('/users/login.html', form=form)


@users.route('/logout/')
def user_logout():
    """退出"""
    logout_user()
    return redirect('/')


@users.route('/change/', methods=['GET', 'POST'])
def change_password():
    """修改密码"""
    form = forms.PassWordForm()
    if request.method == 'POST':
        if form.validate():
            from app import redis_cli
            email = form.email.data
            password = form.password.data
            code = form.code.data
            # 从redis中获取验证码
            key = redis_cli.get(email)
            # 验证验证码是否正确
            if key.decode('utf-8') == code:
                from app.models import Users
                this_user = Users.query.filter_by(email=form.email.data).first()
                # 密码进行哈希加密更新
                this_user.password = generate_password_hash(password)
                this_user.update()
                return redirect('/login/')
            else:
                return jsonify({'result': 0, 'message': '密码不一致'})

    return render_template('/users/change_password.html', form=form)


@users.route('/register/', methods=['GET', 'POST'])
def register():
    """注册"""
    form = forms.RegForm()
    if request.method == 'POST':
        # 表单验证
        if form.validate():
            from app import redis_cli
            email = form.email.data
            password_1 = form.password_1.data
            password_2 = form.password_2.data
            code = form.code.data
            # 从redis中获取验证码
            key = redis_cli.get(email)
            # 验证2次密码是否一致， 以及验证码是否正确
            if password_1 == password_2 and key.decode('utf-8') == code:
                from app.models import Users
                user = Users()
                # 默认用户名为邮箱
                user.username = email
                user.email = email
                # 密码进行哈希加密
                user.password = generate_password_hash(password_2)
                user.reg_time = datetime.now()
                user.save()
                return redirect('/login/')
            else:
                return jsonify({'result': 0, 'message': '密码不一致'})

    return render_template('/users/register.html', form=form)


@users.route('/email/', methods=['GET', 'POST'])
def email():
    """发送验证邮件"""
    email = request.args.get('email')
    print('email:', email)
    if not email:
        return jsonify({'result': 0, 'message': '邮箱为空'})
    else:
        from app import mail, redis_cli
        try:
            msg = Message('Verification Code', sender='2549012701@qq.com', recipients=[email])
            num = f'{random.randint(1, 9999):04}'
            msg.body = num
            # 发送邮件
            mail.send(msg)
            # 向redis中添加验证码，60s过期
            redis_cli.set(email, num, ex=60)
        except Exception as e:
            return jsonify({'result': 0, 'message': str(e)})

        return jsonify({'result': 1})


@users.route('/users/', methods=['GET', 'POST'])
@login_required
def user():
    """用户个人中心界面"""
    form = forms.LoginForm()
    return render_template('/users/users.html', form=form)


@users.route('/alter/avatar/', methods=['GET', 'POST'])
@login_required
def alter_avatar():
    """修改头像接口"""
    if request.method == 'POST':
        print('*' * 100)
        user_id = current_user.id
        from app.models import Users
        user = Users.query.get(user_id)
        file = request.files['file']

        # 修改文件名，使用id+随机数
        filename = file.filename
        filename = filename.rsplit('.', 1)
        name = filename[0] + str(user_id) + str(random.randint(1, 999))
        filename = name + '.' + filename[1]

        user.avatar = filename
        # user.update()
        print('filename:', filename)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + f'\static\\users\\ava\\{user_id}\\'
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        save_path = base_dir + f'{filename}'
        file.save(save_path)
        user.update()
        return redirect('/users/')

    return jsonify({'result': 0})


@users.route('/avater/')
def avater():
    """查询头像接口"""
    user_id = current_user.id
    from app.models import Users
    user = Users.query.get(user_id)
    return jsonify({'avater': user.avatar, 'id': user_id})


@users.route('/alter/info/')
def alter_info():
    """修改个人资料"""
    return render_template('/users/info.html')

