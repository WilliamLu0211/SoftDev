# William Lu
# SoftDev1 pd7
# K14 -- Do I Know You?
# 2018-10-02

from flask import Flask, request, render_template, session, redirect, url_for
from os import urandom

app = Flask(__name__)

app.secret_key = urandom(32)

users = {"123":"qwer"}

# print(app.secret_key)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html", a = True)
    else:
        usr = request.form.get("username")

        if usr not in users.keys() or users[usr] != request.form.get("password"):
            return login()

        elif users[usr] == request.form.get("password"):
            session["username"] = usr
            return render_template("index.html", a = False, username = usr)

@app.route("/login", methods=["POST"])
def login():
    usr = request.form.get("username")

    if usr not in users.keys():
        return render_template("error.html", msg = "Username not found.")

    elif users[usr] != request.form.get("password"):
        return render_template("error.html", msg = "Incorrect password.")

    else:
        return render_template("error.html", msg = "Uh we screwed up")

@app.route("/out")
def logout():
    return redirect("static/logout.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
