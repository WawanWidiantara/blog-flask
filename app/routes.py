from app import app
from flask_login import LoginManager, login_required, current_user, login_user, logout_user, UserMixin
# from app.controller import DosenController
from app.controller import UserController
from app.model.data_model import User
from flask import request, flash, redirect,url_for, render_template


@app.route('/')
@login_required
def index():
    return render_template('home.html')


# @app.route('/dosen', methods=['GET', 'POST'])
# # @jwt_required
# def dosens():
#     if request.method == 'GET':
#         return DosenController.index()
#     else:
#         return DosenController.save()


# @app.route('/dosen/<id>', methods=['GET', 'PUT', 'DELETE'])
# def dosensDetail(id):
#     if request.method == 'GET':
#         return DosenController.detail(id)
#     elif request.method == 'PUT':
#         return DosenController.ubah(id)
#     elif request.method == 'DELETE':
#         return DosenController.hapus(id)
    
    
@app.route('/createadmin', methods=['GET','POST'])
@login_required
def admins():
    if request.method=='POST':
        return UserController.buatAdmin()
    return render_template('new_admin.html', user=current_user)

@app.route('/login', methods=['GET','POST'])
def logins():
    if request.method == 'POST':
        return UserController.login()
    return render_template("login.html", user=current_user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return UserController.logout()
