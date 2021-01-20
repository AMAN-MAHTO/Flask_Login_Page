from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os
import sys

current_path=os.path.dirname(sys.argv[0]).replace('/','\\\\')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/SugantiCosmatic'
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('login.html')
@app.route('/', methods=('GET','POST'))
def about():
    email= request.form.get('email')
    password = request.form.get('pasword')
    con=sqlite3.connect(f'{current_path}\\login.db')
    csr=con.cursor()
    csr.execute("SELECT * from login")
    x=csr.fetchall()
    e=[]
    p=[]
    c_e=False
    c_p=False
    for i in x:
        e.append(i[0])
        p.append(i[1])
    
    for i in e:
        if i==email:
            c_e=True
    for i in p:
        if i==password:
            c_p=True
    if c_e and c_p:
        r=render_template('login_sucess.html')
    else:
        r=render_template('login_fail.html')
        # csr.execute("INSERT INTO login(emails,paswords) VALUES(?,?);",(email,password))
        # con.commit()
        # r=render_template('login.html')
        # if check_ps==True:
        #     render_template('login_sucess.html')
        # else:
        #     render_template('login_fail.html')
        
    return r
app.run(debug=True)
