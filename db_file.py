#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    WC_public_flask
#F-Name:    db_file.py
#Login:     Administrator   
#Descripton:
#__Author__  Smartwy
#Date:      2020/7/2 20:42:05
#Version:

'''
    
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:12345678@192.168.10.241/wcp"
# 上面配置报1366 字符集warning 安装mysql-connector-python，使用下面配置
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:12345678@192.168.10.241/fsql"
# 追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 设置每次请求结束后会自动提交数据库中的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_ECHO'] = True  # 查询时会显示原始SQL语句

db = SQLAlchemy(app)
manager = Manager(app)
# 第一参数是flask实例，第二参数是sqlalchemy实例
Migrate(app,db)
# Flask-Script的实例manager，这条语句在flask-Script中添加一个db命令
manager.add_command('db',MigrateCommand)

class students(db.Model):
    __tablename__ = 'students'  # 指明表名，默认与类相同
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    tel = db.Column(db.String(11))
    age = db.Column(db.Integer)

    def __repr__(self):
        return 'id:{} name:{} city:{} addr:{} tel:{}'.format(self.id,
            self.name, self.city, self.addr, self.tel)



