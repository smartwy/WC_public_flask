#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    appm.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/6/11 14:45:37
#Version:

#导入模块
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

#创建flask对象
app = Flask(__name__)

#配置链接数据库
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:12345678@192.168.10.241/yl"
# 上面配置报1366 字符集warning 安装mysql-connector-python，使用下面配置
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:12345678@192.168.10.241/yl"

# app.config['SQLALCHEMY_ECHO'] = True # 查询时显示原始语句
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # 追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True # 每次请求结束后自动提交数据变动

#获取SQLAlchemy实例对象，接下来就可以使用对象调用数据
db = SQLAlchemy(app)



