# -*- coding: utf-8 -*-
from app.models.User import User
from app.models.Category import Category
from app import app, db
from flask import request, render_template, flash, abort, url_for, redirect, session, Flask, g
from flask import escape


@app.errorhandler(404)
def not_found(error):
    # return render_template('404.html'), 404
    flash('404')


@app.route('/')
def show_entries():
    categorys = Category.query.all()
    return render_template('show_entries.html', entries=categorys)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    title = request.form['title']
    content = request.form['text']
    category = Category(title, content)
    db.session.add(category)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username.strip():
            error = 'username is temp'
        elif not password.strip():
            error = 'password is temp'
        else:
            user = User.query.filter_by(username=request.form['username']).first()
            if user is None:
                error = 'Invalid username'
            elif password != user.password:
                error = 'Invalid password'
            else:
                session['logged_in'] = True
                flash("you were login")
                return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
