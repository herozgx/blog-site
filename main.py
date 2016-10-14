#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)   #__name__参数决定了程序的更目录
manager = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    manager.run()
