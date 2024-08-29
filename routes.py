from flask import render_template, Flask

def setup_routes(app: Flask):
    @app.route('/')
    def home():
        return render_template("home.html")

    @app.route("/login", methods=['GET', 'POST'])
    def login():
        return render_template("login.html")

    @app.route("/register", methods=['GET', 'POST'])
    def register():
        return render_template("register.html")

