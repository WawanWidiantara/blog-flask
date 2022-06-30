from app.model.data_model import User
from flask import request, flash, redirect,url_for, render_template
import os
from app import app, db
from flask_login import current_user, login_user, logout_user, UserMixin


def buatAdmin():
    try:
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        cpassword = request.form.get('cpassword')
        level = 2
        
        # check email exist
        email_exists = User.query.filter_by(email=email).first()
        
        if email_exists:
            flash('Email is already in use.', category='error')
        elif password != cpassword:
            flash('Password don\'t match!', category='error')
        elif len(username) < 2:
            flash('Username is too short.', category='error')
        elif len(password) < 6:
            flash('Password is too short.', category='error')
        elif len(email) < 4:
            flash("Email is invalid.", category='error')
        else:
            users = User(username=username, email=email, level=level)
            users.setPassword(password)
            db.session.add(users)
            db.session.commit()
            flash('New Admin created!')
            return redirect(url_for('index'))

        return render_template('new_admin.html', user=current_user)
    except Exception as e:
        print(e)

def login():
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if user.checkPassword(password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('index'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')
            
        return render_template("login.html", user=current_user)
    except Exception as e:
        print(e)
        
def logout():
    try:
        logout_user()
        return redirect(url_for("index"))
    except Exception as e:
            print(e)
        

