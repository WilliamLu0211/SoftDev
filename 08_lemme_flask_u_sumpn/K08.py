# William Lu
# SoftDev1 pd7
# K08 -- Fill Yer Flask
# 2018-09-20

from flask import Flask

app = Flask(__name__)

@app.route("/")
def greeting():
	return "xd"

@app.route("/java")
def shout():
	return "<h1>NullPointerException</h1>"

@app.route("/gay")
def show():
	return "<h2><i>no homo</i></h2>"

app.debug = True
app.run()