from app.model.data_model import Post
from flask import request, flash, redirect,url_for, render_template
import os
from app import app, db

def getPost():
    try:
        posts = Post.query.all()
        return render_template("posts.html", posts=posts)
    except Exception as e:
        print(e)
        
def createPost():
    try:
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')
        if not title:
            flash('Title cannot be empty', category='error')
        if not author:
            flash('Author cannot be empty', category='error')
        if not content:
            flash('Content cannot be empty', category='error')
        else:
            post = Post(title=title, author=author, content=content)
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('posts'))
    except Exception as e:
        print(e)
        
def editPost(id):
    try:
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')

        post = Post.query.filter_by(id=id).first()
        post.title = title
        post.author = author
        post.content = content

        db.session.commit()
        flash('Post edited!', category='success')
        return redirect(url_for('posts'))
    except Exception as e:
        print(e)
    
def deletePost(id):
    try:
        post = Post.query.filter_by(id=id).first()
        if not post:
            flash("Post does not exist.", category='error')
        else:
            db.session.delete(post)
            db.session.commit()
            flash('Post deleted.', category='success')
        return redirect(url_for('posts'))
    except Exception as e:
        print(e)