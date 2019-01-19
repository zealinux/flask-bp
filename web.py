#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from app import create_app
from models import User

app = create_app()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def test():
    user = User.query.first()
    json = {'name': user.name}
    return jsonify(json)

if __name__ == '__main__':
    app.run()
