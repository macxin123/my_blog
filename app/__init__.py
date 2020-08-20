import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_login import LoginManager
from flask_mail import Mail
from app.users import users
from app.blogs import blogs
from app.admins import admins
from settings import MySQLConfig

# 实例化数据库
db = SQLAlchemy()
# 实例化CSRF
csrf = CSRFProtect()
# 登录验证
login_manager = LoginManager()
# 邮箱
mail = Mail()
# redis
redis_cli = redis.Redis()


# 定义获取登录用户的方法
@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.get(user_id)


def make_app(config=MySQLConfig):
    # 创建app
    app = Flask(__name__, static_url_path='/static/', template_folder='templates')
    # 配置app
    app.config.from_object(config)
    # 解决jinja2与vue的冲突
    app.jinja_env.variable_start_string = '{['
    app.jinja_env.variable_end_string = ']}'
    # 数据库绑定app
    db.init_app(app)
    # CSRF绑定app
    csrf.init_app(app)
    # 邮箱绑定app
    mail.init_app(app)
    # 登录绑定app
    login_manager.init_app(app)
    login_manager.login_view = '/login/'
    login_manager.session_protection = 'strong'
    # 注册app
    app.register_blueprint(users)
    app.register_blueprint(blogs, url_prefix='/blogs/')
    app.register_blueprint(admins, url_prefix='/admins/')

    return app