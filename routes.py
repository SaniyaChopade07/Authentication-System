from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash
from models import User
from extensions import db

def setup_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            user = User.query.filter_by(email=email).first()

            if user and check_password_hash(user.password, password):
                flash('Logged in successfully!', 'success')
                return redirect('http://127.0.0.1:5001/')  # Redirect to the specified URL
            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')

        return render_template("login.html")

    @app.route('/home')
    def home():
        return render_template("index.html")

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            phone_number = request.form['phone_number']
            occupation = request.form['occupation']
            password = request.form['password']
            confirm_password = request.form['confirm_password']

            if password == confirm_password:
                hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
                new_user = User(username=username, email=email, phone_number=phone_number, occupation=occupation, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                flash('Your account has been created! You can now log in', 'success')
                return redirect(url_for('login'))
            else:
                flash('Passwords do not match. Please try again.', 'danger')

        return render_template("signup.html")
