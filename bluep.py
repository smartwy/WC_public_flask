#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    WC_public_flask
#F-Name:    bluep.py
#Login:     Administrator   
#Descripton:
#__Author__  Smartwy
#Date:      2020/7/4 14:28:24
#Version:

'''
    
'''

from flask import Blueprint,render_template

# 指定两个参数，gzh表示蓝图的名称，__name__表示蓝图所在模块
gzh = Blueprint('gzh',__name__, template_folder='templates', static_folder='static')

@gzh.route('/')
def bpfun():
	return render_template('bp.html')

