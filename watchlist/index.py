from flask_wtf import FlaskForm
from wtforms import FileField, SelectField, SubmitField, TextAreaField, StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed


class InfoForm(FlaskForm):
    fileopenname = StringField(label='信息文件', render_kw={'placeholder': '账号第一列，密码第二列，不加标题', 'disabled': 'disabled'})
    fileopen = FileField(
        validators=[
            FileRequired('请选择信息文件'),
            FileAllowed(['xls', 'xlsx'], '只接受.xls和.xlsx格式的文件')
        ]
    )
    term = SelectField(
        label='学期',
        validators=[DataRequired('请选择学期')],
        choices=[(1, '大一上'), (2, '大一下'), (3, '大二上'), (4, '大二下'), (5, '大三上'), (6, '大三下'), (7, '大四上'), (8, ('大四下'))],
        #default=1,
        coerce=int
    )
    submit = SubmitField('执行')
    result = TextAreaField('结果如下⬇⬇⬇', render_kw={'disabled': 'disabled'})
