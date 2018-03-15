#!/usr/bin/env python
# *-* coding: utf-8 *-*

from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/user/<name>', methods=['GET','POST'])
def home(name):
	return '<h1>Home, {}</h1>'.format(name.encode("utf-8"))

@app.route('/signin', methods=['GET'])
def signin_from():
	return '''<form action="/signin" method="POST">
			  <p><input name="username"></p>
			  <p><input name="password" type="password"></p>
			  <p><button type="submit">Sign In</button></p>
			  </form>'''

@app.route('/signin', methods=['POST'])
def signin():
	if request.form['username']=='admin' and request.form['password']=='password':
		return '<h3>Hello,admin!</h3>'
	return '<h3>Bad username or password.</h3>'

if __name__ == "__main__":
	app.run()
