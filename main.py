from flask import Flask, request, render_template, redirect, url_for
from WTF import Login, Register
from flask_sqlalchemy import SQLAlchemy
from SECRET import secret_key, private_key

web_page = Flask(__name__, template_folder='templates')
web_page.config["SECRET_KEY"] = secret_key
web_page.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
web_page.config['RECAPTCHA_USE_SSL'] = False
web_page.config['RECAPTCHA_USE_TSL'] = True
web_page.config['RECAPTCHA_PUBLIC_KEY'] = 'CS$3^PKEY'
web_page.config['RECAPTCHA_PRIVATE_KEY'] = private_key
web_page.config['RECAPTCHA_OPTIONS'] = {'theme': 'white'}
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
     

@web_page.route('/register', methods = ["GET", "POST"])
def register():
    form = Register()
    return render_template("sign-in.html", form = form)

@web_page.route("/login", methods = ["GET", "POST"])
def login():
    form = Login()
    return render_template("log-in.html", form = form)

if __name__ == '__main__':
    web_page.debug = True
    web_page.run(debug = True)