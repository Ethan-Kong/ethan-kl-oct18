# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:09:55 2018

@author: ethan.kong
"""

from Flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/goodbye")
def goodbye():
    return "<b>Goodbye World!</b>"

@app.route("/")
def formpage():
    return render_template('formpage.html')

@app.route ("/submit")
def submitPage():
    txtValue = request.form['txtName']
    return "<h>Thank you for</h>, : " + txtValue

if __name__ == "__main__":
    app.run()