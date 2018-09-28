# William Lu
# SoftDev1 pd7
# K13 -- Echo Echo Echo
# 2018-09-28 F

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def display():
    return render_template("frontEnd.html",
                           t = "K13_frontEnd",
                           msg = "Please type your username.")

@app.route("/auth", methods=["GET"])
def authenticate():
    print(request.method)
    return render_template("backEnd.html",
                           t = "K13_backEnd",
                           greet = "Hello, " + request.args['username'] + "!",
                           method = "GET")

if __name__ == "__main__":
    app.debug = True
    app.run()
