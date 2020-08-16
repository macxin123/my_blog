from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(message=u"邮箱不能为空"), Email(message=u"请输入正确的邮箱地址")])
    password = PasswordField('password', validators=[DataRequired(message=u"密码不能为空")])