#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    smart_yl.py
#Login:     Administrator
#Descripton:
#Author:    Smartwy
#Date:      2019/6/11 10:25:56
#Version:

from flask import jsonify
from appm import app, db
from flask_restful import Api, Resource, reqparse, abort
import time
# app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
def reg_args():
	# parser.add_argument('user_id')
	parser.add_argument('low')  # 接收的变量名称一定要在这里‘注册’
	parser.add_argument('hig')
	parser.add_argument('name')
	parser.add_argument('id')
	parser.add_argument('sex')
	parser.add_argument('age')
	parser.add_argument('addr')
	parser.add_argument('tel')
	parser.add_argument('xuet')

def exist_id(u_id):
	if User.query.get(u_id): # 精确查询
		abort(400, message="{} exist！".format(u_id))

class User(db.Model):
	__tablename__ = 'User' # 指明表名，默认与类相同
	__table_args__ = {'mysql_collate': 'utf8_general_ci'}
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	sex = db.Column(db.String(4))
	age = db.Column(db.Integer)
	addr = db.Column(db.String(64))
	tel = db.Column(db.String(11))
	date_c = db.Column(db.DateTime)
	xy = db.relationship("Xy", backref='User')
	xt = db.relationship("Xt", backref='User')
	# relationship()	把两个表关联在一起，不添加也是可以的，根据自己的需求
	def __repr__(self):
		return 'name:%r' % (self.name)

class Xy(db.Model):
	__tablename__ = 'Xy'
	__table_args__ = {'mysql_collate': 'utf8_general_ci'}
	number = db.Column(db.Integer, autoincrement=True, primary_key=True) # 需要使用__tablename__参数指定表名
	u_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=True)
	hig = db.Column(db.Integer)
	low = db.Column(db.Integer)
	x_date = db.Column(db.DateTime)
	def __repr__(self):
		return 'id:%s, hig:%s, low:%s, x_date:%s' % (self.u_id,self.hig,self.low,self.x_date)

class Xt(db.Model):
	__tablename__ = 'Xt'
	__table_args__ = {'mysql_collate': 'utf8_general_ci'}
	number = db.Column(db.Integer, autoincrement=True, primary_key=True) # 需要使用__tablename__参数指定表名
	u_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=True)
	xt = db.Column(db.Integer)
	x_date = db.Column(db.DateTime)
	def __repr__(self):
		return 'id:%s, xt:%s, x_date:%s' % (self.u_id, self.xt, self.x_date)

# 多对多表设置示例：
# tags = db.Table('tags',
#     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
#     db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
# )
#
# class Page(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	tags = db.relationship('Tag', secondary=tags, lazy='subquery',
#         backref=db.backref('pages', lazy=True))
#
# class Tag(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)

class Add_user(Resource):
	def put(self):
		args = parser.parse_args() # 获取传递过来的变量与值，字典格式
		exist_id(args['id'])
		data = User(name=args['name'],
		            id=args['id'],
		            sex=args['sex'],
		            age=args['age'],
		            addr=args['addr'],
		            tel=args['tel'],
		            date_c=time.strftime('%Y-%m-%d %H:%M:%S'))
		db.session.add(data)
		db.session.commit()
		db.session.close()
		return 'ok',200

class Xue_ya(Resource):
	def get(self, id):
		# args = parser.parse_args()
		# args = args['id']
		# result = Xy.query.filter_by(u_id=args).all()  # 条件查询
		# name = User.query.filter_by(id=args).first()
		result = Xy.query.filter_by(u_id=id).all()  # 条件查询
		name = User.query.filter_by(id=id).first()
		return '{} {}'.format(name, result)

	def put(self):
		args = parser.parse_args()
		data1 = Xy(u_id=args['id'], low=args['low'], hig=args['hig'], x_date=time.strftime('%Y-%m-%d %H:%M:%S'))
		db.session.add(data1)
		db.session.commit()
		db.session.close()
		return 'id：{}，low：{}，hig：{}'.format(args['id'], args['low'], args['hig'])

class Xue_tang(Resource):
	def get(self):
		args = parser.parse_args()
		args = args['id']
		result = Xt.query.filter_by(u_id=args).all()  # 条件查询
		name = User.query.filter_by(id=args).first()
		return '{} {}'.format(name, result)

	def put(self):
		args = parser.parse_args()
		data2 = Xt(u_id=args['id'], xt=args['xuet'], x_date=time.strftime('%Y-%m-%d %H:%M:%S'))
		db.session.add(data2)
		db.session.commit()
		db.session.close()
		return 'id：{}，xt：{}'.format(args['id'], args['xuet'])

class men_suo(Resource):
	pass
class xin_lv(Resource):
	pass
class ti_zhong(Resource):
	pass

api.add_resource(Add_user, '/adduser')  # http://127.0.0.1:5000/adduser?name=wy&id=22349822&age=341&sex=f&addr=北京顺建新北区&tel=18623327
# api.add_resource(Xue_ya, '/xueya')      # http://127.0.0.1:5000/xueya?id=100&low=90&hig=120  第一种方法
api.add_resource(Xue_ya, '/xueya/<id>') # http://127.0.0.1:5000/xueya/100 第二种方法
api.add_resource(Xue_tang, '/xuetang')  # http://127.0.0.1:5000/xuetang?id=100&xt=85
api.add_resource(men_suo, '/mensuo')    # http://127.0.0.1:5000/mensuo?=100&flag=off/on
api.add_resource(xin_lv, '/xinlv')      # http://127.0.0.1:5000/xuetang?=100&lv=85
api.add_resource(ti_zhong, '/tizhong')   # http://127.0.0.1:5000/tizhong?=100&zhong=85

if __name__ == '__main__':
	reg_args()
	db.create_all()  # 创建数据表
	app.run(debug=True)

