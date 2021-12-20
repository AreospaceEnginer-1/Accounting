from flask import Flask, request, render_template, make_response, redirect, url_for
from .WTF import Create_Account, Login, Register
from flask import Flask, request, render_template, make_response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

web_page = Flask('Account')
web_page.config["SECRET_KEY"] = "#!$1#5!R9*₹^UPP@s^₹*%2!6#10$#"
web_page.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(web_page)

# def get_uname(request):
    
#     u_name = request.cookies.get("User Private Protectd Info", False)

#     if not u_name:
#         set_cookie()

#     return u_name


# def set_cookie():

#     head = "User Private Protectd Info"
#     head = bytes(head, 'utf-8')

#     user_infos = lister(request)

#     u_name_pass = "\n".join(user_infos[-2:])
#     u_name_pass = bytes(u_name_pass, 'utf-8')

#     response = make_response('This site uses cookies')
#     response.set_cookie(head, u_name_pass) 


@web_page.errorhandler(404)
def ERROR404(error):
    error = str(error)
    error = error.split('.')
    return render_template('not_found.html', error = error)


@web_page.route('/')
def home():
    return render_template('home.html')
     

@web_page.route('/register', methods = ["POST"])
def register():
    form = Register()
    return render_template("sign-in.html", form = form)

@web_page.route("/login")
def join_account():
    form = Login()
    return render_template("sign-in.html", form = form)