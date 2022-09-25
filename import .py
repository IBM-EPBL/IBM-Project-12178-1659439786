import os
import sqlite3
from unittest import result
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
currentlocation = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def main():
    return render_template("login.html")


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["form-username"]
        password = request.form["form-password"]

        sqlcon = sqlite3.Connection(currentlocation + "/user.db")
        cursor = sqlcon.cursor()
        query1 = ("SELECT username,password FROM users WHERE username='"+username+"' AND password='"+password+"'")
        cursor.execute(query1)
        result = cursor.fetchall()
        if len(result) == 1:
            return render_template("welcome.html", uname = username)
        else:
            return render_template("login.html", invalidMsg = "User doesn't exist, please register to continue")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["form-username"]
        regno = request.form["form-password"]
        email = request.form["form-password"]
        password = request.form["form-password"]

        sqlcon = sqlite3.Connection(currentlocation + "/user.db")
        cursor = sqlcon.cursor()
        query1 = "INSERT INTO users VALUES('"+username+"','"+regno+"','"+email+"','"+password+"')"
        cursor.execute(query1)
        sqlcon.commit()
        return redirect("/")
    return render_template("register.html")


if __name__ == "__main__":
    app.run()
