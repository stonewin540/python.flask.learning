#!/usr/bin/env python3
# coding=utf-8

from flask import Flask, url_for, request, render_template, make_response, redirect

app = Flask(__name__)


@app.route('/')
def index():
    # return 'Index Page'
    username = request.cookies.get('username')
    resp = None
    if not username:
        username = 'The first user name'
        resp = make_response('Create user name')
        resp.set_cookie('username', username)
    else:
        username = 'Fetched user name'
        resp = make_response(username)
        resp.set_cookie('username', username)
    return resp


@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name=None):
    # return 'Hello, World!'
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'In the first case, ' \
           'the canonical URL for the projects endpoint has a trailing slash. ' \
           'In that sense, it is similar to a folder on a filesystem. ' \
           'Accessing it without a trailing slash will cause ' \
           'Flask to redirect to the canonical URL with the trailing slash.'


@app.route('/about')
def about():
    # return 'In the second case, however, the URL is defined without a trailing slash, ' \
    #        'rather like the pathname of a file on UNIX-like systems. ' \
    #        'Accessing the URL with a trailing slash will produce a 404 “Not Found” error.'
    return redirect(url_for('login'))


with app.test_request_context():
    print(url_for('index'))

    print(url_for('hello_world'))
    print(url_for('hello_world', age=123))

    print(url_for('show_user_profile', username='user_name'))
    print(url_for('show_post', post_id=1999))


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     return 'You are "POST"ing...'
    # else:
    #     return 'You are "GET"ing...'


    error = None
    name = None
    passwd = None
    # if request.method == 'POST':
    #     if request.form.get('username', None) and request.form.get('password', None):
    #         name = request.form.get('username')
    #     else:
    #         error = 'Invalid username/password'
    #
    # return render_template('login.html', name=name, error=error)
    if request.method == 'POST':
        # name = request.form['username']
        name = request.form.get('username')
        passwd = request.form.get('passwd')
    else:
        name = request.args.get('username')
        passwd = request.args.get('passwd')

    if name and passwd:
        return render_template('login.html', username=name, passwd=passwd)
    else:
        error = 'Invliad username/passwd\n'
        return render_template('login.html', error=error)
