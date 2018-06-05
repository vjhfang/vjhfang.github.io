# coding:utf8
import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:ROOT@localhost/artcms_pro"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
"""
用户模型
1、编号
2、账号
3、密码
4、注册时间
"""


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    pwd = db.Column(db.String(100), nullable=False)
    addtime = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.name
    def check_pwd(self,pwd):
        return check_password_hash(self.pwd,pwd)


"""
文章模型
1、编号
2、标题
3、分类
4、作者
5、封面
6、内容
7、发布时间
"""


class Art(db.Model):
    __tablename__ = "art"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    cate = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    logo = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    fabutime = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return "<Art %r>" % self.title

if __name__ == "__main__":
    db.create_all()

