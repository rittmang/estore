from flask import Flask, render_template, redirect, request, url_for, jsonify,abort
import os
from flask_bcrypt import Bcrypt
from flask_login import (
    LoginManager,
    login_required,
    login_user,
    logout_user,
    current_user
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc,exc
app=Flask(__name__)
app.secret_key=os.getenv("SECRET_KEY")
db=SQLAlchemy(app)
login_manager  = LoginManager()
login_manager.init_app(app)
login_manager.login_view="login"
bcrypt=Bcrypt(app)
app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL")
#  INSERT INTO users (email, password) VALUES (
#   'johndoe@mail.com',
#   crypt('johnspassword', gen_salt('bf'))
# );
@app.route("/")
def root():
    return render_template(
        "login.html"
    )

@app.route("/login")
def login():
    return render_template(
        "login.html"
    )
@app.route("/register",methods=["GET","POST"])
def register():
    
    if request.method=='POST':
        try:
            name=request.form["name"]
            username=request.form["username"]
            password=request.form["password"]
        except KeyError:
            return jsonify({"response":"Enter all data please"}),400
    u=Users(
        name=name,
        username=username,
        password=password,
    )
    try:
        db.session.add(u)
        db.session.commit()
    return render_template(
        "register.html"
    )