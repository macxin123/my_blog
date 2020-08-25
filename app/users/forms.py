from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(message=u"邮箱不能为空"), Email(message=u"请输入正确的邮箱地址")])
    password = PasswordField('password', validators=[DataRequired(message=u"密码不能为空")])


class RegForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(message=u"邮箱不能为空"), Email(message=u"请输入正确的邮箱地址")])
    password_1 = PasswordField('password_1', validators=[DataRequired(message=u"密码不能为空"), Length(6, 15, message='长度大于6，小于15')])
    password_2 = PasswordField('password_2', validators=[DataRequired(message=u"密码不能为空"), Length(6, 15, message='长度大于6，小于15')])
    code = StringField('code', validators=[DataRequired(message=u"验证码不能为空"), Length(4, 6, message='请输入4或6位验证码')])


class PassWordForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(message=u"邮箱不能为空"), Email(message=u"请输入正确的邮箱地址")])
    password = PasswordField('password_1', validators=[DataRequired(message=u"密码不能为空"), Length(6, 15, message='长度大于6，小于15')])
    code = StringField('code', validators=[DataRequired(message=u"验证码不能为空"), Length(4, 6, message='请输入4或6位验证码')])
