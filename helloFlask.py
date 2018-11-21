# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:53:32 2018

@author: ethan.kong
"""

from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/goodbye")
def goodbye():
    return "Goodbye World!"

if __name__ == "__main__":
    app.run()