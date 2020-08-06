from flask import render_template, request
from db_file import app,db,students,manager
from bluep import gzh

# 注册一个gzh蓝图
app.register_blueprint(gzh,url_prefix='/bp')
#参数url_prefix='/xxx'的意思是设置request.url中的url前缀，
#即当request.url是以/admin或者/user的情况下才会通过注册的蓝图的视图方法处理请求并返回

@app.route('/',methods=['GET','POST'])
def hello():
    if request.method == 'GET':
        data = students.query.all()
        return render_template('index.html',result = data)
    elif request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        city = request.form['city']
        addr = request.form['addr']
        tel = request.form['tel']
        user = students(id=id,name=name,city=city,addr=addr,tel=tel)
        db.session.add(user)
        db.session.commit()
        data = students.query.all()
        return render_template('index.html',result = data)

@app.route('/delurl',methods=['POST'])
def delfun():
    delobj = request.form['del']
    user = students.query.filter_by(id=delobj).first()
    db.session.delete(user)
    db.session.commit()
    data = students.query.all()
    return render_template('index.html', result=data)

if __name__ == '__main__':
    db.create_all()
    app.run()
    # manager.run()
