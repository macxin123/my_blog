import os

e_password = os.environ["FYX_MYSQL_PASSWORD"]
base_dir = os.path.dirname(os.path.abspath(__file__))


class MySQLConfig:
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://root:{e_password}@127.0.0.1:3306/myblog"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'fyx'
    debug = True