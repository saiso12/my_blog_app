from flask import Flask, render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        "author": "Sai Varun",
        "title": "Blog Post 1",
        "content": "First Post",
        "date_posted": "April 20, 2018",
    },
    {
        "author": "Bane",
        "title": "Blog Post 2",
        "content": "First Post",
        "date_posted": "April 22, 2018",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): #validate handled in 'register.html' with jinja2 template
        flash(f"Account  created for {form.username.data}!", "success")  # success from bootstrap class
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'saiprash@outlook.com' and form.password.data == 'pass':
            flash(f"You have been logged in!", "success")
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessesful. Please check username and password.", "danger")
    return render_template("login.html", title="Login", form=form)