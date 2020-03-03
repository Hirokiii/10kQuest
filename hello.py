from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__) #__name__ represents the current module name
app.secret_key = 'asdfghjkl'
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session['user'] = user
        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if 'user' in session:
            flash("Already Logged In:)")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if 'user' in session:
        user = session['user']
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in...")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop('user', None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug= True) # if you the host is raspberry pi, host should be 0.0.0.1