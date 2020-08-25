from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,  Length
from wtforms import StringField, TextAreaField


class ArticlesForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(message=u"标题不能为空"), Length(0, 32, message='长度小于32')])
    body = TextAreaField('Body', validators=[DataRequired(message=u"内容不能为空")])