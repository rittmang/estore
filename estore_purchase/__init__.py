from flask import Flask, render_template, redirect, request, url_for, abort
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
@app.route("/register")
def register():
    return render_template(
        "register.html"
    )