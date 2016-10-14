#!/usr/bin/env python
# coding: utf-8

from flask import Flask

app = Flask(__name__)   #__name__参数决定了程序的更目录

@app.route('/')
def index():
    return "hello world"

@app.route('/<name>')
def user(name):
    return "hello {0}".format(name)

if __name__ == "__main__":
    app.run(debug=True)
