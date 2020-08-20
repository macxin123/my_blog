import os

# 从环境变量读取信息
e_password = os.environ["FYX_MYSQL_PASSWORD"]
mail_username = os.environ["MAIL_USERNAME"]
mail_password = os.environ["MAIL_PASSWORD"]
base_dir = os.path.dirname(os.path.abspath(__file__))


class MySQLConfig:
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://root:{e_password}@127.0.0.1:3306/myblog"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'fyx'
    debug = True

    # 邮箱设置
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = mail_username
    MAIL_PASSWORD = mail_password