# coding:utf8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from models import User

"""
登录
1、账号
2、密码
3、登录按钮
"""


class LoginForm(FlaskForm):
    name = StringField(
        label="账号",
        validators=[
            DataRequired("账号不能为空")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！"
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("密码不能为空")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！"
        }
    )
    submit = SubmitField(
        "登录",
        render_kw={
            "class": "btn btn-primary"
        }
    )

    def validate_pwd(self, field):
        pwd = field.data
        user = User.query.filter_by(name=self.name.data).first()
        if not user.check_pwd(pwd):
            raise ValidationError("密码不正确")


"""
注册
1、账号
2、密码
3、确认密码
4、验证码
5、注册按钮
"""


class RegisterForm(FlaskForm):
    name = StringField(
        label="账号",
        validators=[
            DataRequired("账号不能为空！")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！"
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("密码不能为空！")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！"
        }
    )
    repwd = PasswordField(
        label="确认密码",
        validators=[
            DataRequired("确认密码不能为空！"),
            EqualTo('pwd', message="两次输入密码不一致！")
        ],
        description="确认密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请确认密码！"
        }
    )
    code = StringField(
        label="验证码",
        validators=[
            DataRequired("验证码不能为空！先随便填几个数字吧")
        ],
        description="验证码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入验证码！"
        }

    )
    submit = SubmitField(
        "注册",
        render_kw={
            "class": "btn btn-success"
        }
    )

    # 自定义字段规则：validate_字段名
    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user > 0:
            raise ValidationError("账号已经存在，不能重复注册！")


"""
发布文章表单
1、标题
2、分类
3、封面（logo）
4、内容
5、发布文章按钮
"""


class ArtForm(FlaskForm):
    title = StringField(
        label="标题",
        description="标题",
        validators=[
            DataRequired("标题不能为空！")
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入标题！！"
        }
    )
    cate = SelectField(
        label="分类",
        description="分类",
        validators=[
            DataRequired("分类不能为空！")
        ],
        choices=[(1, "科技"), (2, "搞笑"), (3, "军事")],
        default=3,
        coerce=int,
        render_kw={
            "class": "form-control"
        }
    )
    logo = FileField(
        label="封面",
        validators=[
            DataRequired("封面不能为空！")
        ],
        description="封面",
        render_kw={
            "class": "form-control-file"
        }
    )
    content = TextAreaField(
        label="内容",
        validators=[
            DataRequired("内容不能为空！")
        ],
        description="内容",
        render_kw={
            "style": "height:300px;",
            "id": "content"
        }
    )
    submit = SubmitField(
        "发布文章",
        render_kw={
            "class": "btn btn-primary"
        }
    )


class ArtEditForm(FlaskForm):
    id = IntegerField(
        label="编号",
        validators=[
            DataRequired("编号不能为空！")
        ]
    )
    title = StringField(
        label="标题",
        description="标题",
        validators=[
            DataRequired("标题不能为空！")
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "请输入标题！！"
        }
    )
    cate = SelectField(
        label="分类",
        description="分类",
        validators=[
            DataRequired("分类不能为空！")
        ],
        choices=[(1, "科技"), (2, "搞笑"), (3, "军事")],
        default=3,
        coerce=int,
        render_kw={
            "class": "form-control"
        }
    )
    logo = FileField(
        label="封面",
        validators=[
            DataRequired("封面不能为空！")
        ],
        description="封面",
        render_kw={
            "class": "form-control-file"
        }
    )
    content = TextAreaField(
        label="内容",
        validators=[
            DataRequired("内容不能为空！")
        ],
        description="内容",
        render_kw={
            "style": "height:300px;",
            "id": "content"
        }
    )
    submit = SubmitField(
        "编辑文章",
        render_kw={
            "class": "btn btn-primary"
        }
    )
