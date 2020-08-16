from flask_login import UserMixin
from werkzeug.security import check_password_hash
from app import db


class Base(db.Model):
    """该项目所有数据库的父类"""
    # 只能被继承使用
    __abstract__ = True

    # id字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        """保存"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """删除"""
        db.session.delete(self)
        db.session.commit()

    def update(self):
        """修改"""
        db.session.commit()


class Users(Base):
    """用户表"""
    # 表名：users
    __tablename__ = 'users'

    # 用户名
    username = db.Column(db.String(32), unique=True)
    # 密码
    password = db.Column(db.String(32))
    # 手机号
    phone = db.Column(db.String(32), nullable=True, unique=True)
    # 邮箱
    email = db.Column(db.String(32), nullable=True, unique=True)
    # 用户等级 0:游客用户,1:普通用户,2:会员用户,3:大会员用户,4:管理员用户,5:站长
    level = db.Column(db.SmallInteger, default=1)
    # 性别
    sex = db.Column(db.Boolean, nullable=True)
    # 出生日期
    birth_date = db.Column(db.Date, nullable=True)
    # 注册日期
    reg_time = db.Column(db.DateTime)
    # 个性签名
    signature = db.Column(db.Text, nullable=True)
    # 用户余额(单位：F币)
    balace = db.Column(db.DECIMAL(10, 2), default=0.00)
    # 小花花
    user_flower = db.Column(db.Integer, default=5)
    # 用户头像
    avatar = db.Column(db.String(32), default='userImages/head.jpg')

    # 反向映射文章表
    u_articles = db.relationship('Articles', backref='users_a')

    # 反向映射评论表
    u_comments = db.relationship('Comments', backref='users_c')


class User(UserMixin):
    def __init__(self, user):
        self.username = user.username
        self.email = user.email
        self.password = user.password
        self.id = user.id

    def verif_password(self, password):
        """密码验证"""
        if self.password is None:
            return False
        else:
            return check_password_hash(self.password, password)

    def get_id(self):
        """获取用户ID"""
        return self.id

    @staticmethod
    def get(user_id):
        """根据用户ID获取用户实体，为 login_user 方法提供支持"""
        if not user_id:
            return None
        user = Users.query.get(user_id)
        if user.id == user_id:
            return User(user)
        return None


class Articles(Base):
    """文章表"""
    # 表名：articles
    __tablename__ = 'articles'

    # 文章标题
    title = db.Column(db.String(32))
    # 外键,作者id
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # 文章内容
    a_content = db.Column(db.Text)
    # 文章点赞
    good = db.Column(db.Integer, default=0)
    # 文章点踩
    bad = db.Column(db.Integer, default=0)
    # 该文章收到的小花花
    a_flower = db.Column(db.Integer, default=0)
    # 文章发布时间
    a_time = db.Column(db.DateTime)
    # 收藏数
    collection = db.Column(db.Integer, default=0)

    # 反向映射评论表
    a_comments = db.relationship('Comments', backref='articles_c')


class Comments(Base):
    """评论表"""
    # 表名：comments
    __tablename__ = 'comments'

    # 评论内容
    c_content = db.Column(db.Text)
    # 外键,评论用户id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # 外键,文章id
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))