from app import app
from flask_login import (
    LoginManager,
    login_required,
    current_user,
    login_user,
    logout_user,
    UserMixin,
)
from app.controller import PostController
from app.controller import UserController
from app.model.data_model import User, Post
from flask import request, flash, redirect, url_for, render_template


@app.route("/")
@login_required
def index():
    return render_template("home.html")


@app.route("/posts", methods=["GET", "POST"])
@login_required
def posts():
    if request.method == "GET":
        return PostController.getPost()
    return render_template("posts.html", user=current_user)


@app.route("/create-post", methods=["GET", "POST"])
@login_required
def newPosts():
    if request.method == "POST":
        return PostController.createPost()
    return render_template("new_post.html", user=current_user)


@app.route("/edit-post/<id>", methods=["GET", "POST"])
@login_required
def editPosts(id):
    post = Post.query.filter_by(id=id).first()
    if request.method == "POST":
        return PostController.editPost(id)
    return render_template("edit_post.html", user=current_user, post=post)


@app.route("/delete-post/<id>")
@login_required
def deletePosts(id):
    return PostController.deletePost(id)


@app.route("/createadmin", methods=["GET", "POST"])
@login_required
def admins():
    if request.method == "POST":
        return UserController.buatAdmin()
    return render_template("new_admin.html", user=current_user)


@app.route("/login", methods=["GET", "POST"])
def logins():
    if request.method == "POST":
        return UserController.login()
    return render_template("login.html", user=current_user)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return UserController.logout()
