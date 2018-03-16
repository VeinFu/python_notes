#!/usr/bin/env python
# *-* coding: utf-8 *-*

import os
from flask import Flask,request,redirect,url_for

app = Flask(__name__)
@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
	if request.method == "POST":
		f = request.files['file']
		filename = f.filename
		f.save(os.path.join('/var/www/upload', filename))
		return redirect(url_for('upload_file', filename=filename))

	return '''
			<!doctype html>
			<title>Upload new file</title>
			<h1>Upload new file</h1>
			<form action="" method=post enctype=multipart/form-data>
				<p><input type=file name=file></p>
				<p><input type=submit value=Upload></p>
			</form>
			'''

if __name__ == "__main__":
	app.run('0.0.0.0')
