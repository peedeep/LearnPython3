#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
	return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	if username == 'rick' and password == '123456':
		return render_template('signin_ok.html', username = username)
	return render_template('form.html', message='Bad username or password', username = username)


if __name__ == '__main__':
	app.run(
		host = '192.168.113.211',
		port = 7777,
		debug = True
	)
