from flask import Flask, render_template, redirect, url_for, flash
from WTF import Login, Register, Search, LoginForm
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from SECRET import secret_key

web_page = Flask(__name__, template_folder='templates')
web_page.config["SECRET_KEY"] = secret_key
web_page.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
web_page.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(web_page)

forms = list()

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

class Jinja2_NOT_ReadableError(Exception): pass

class Accounts(db.Model):
    Id = db.Column(db.Integer, primary_key = True) 
    Name = db.Column(db.String(50), nullable = False) 
    U_name = db.Column(db.String(30), nullable = False, unique = True)
    # Email = db.Column(db.String(50), nullable = False, unique = True)
    # Age = db.Column(db.Integer, nullable = False)

    def __repr__(self):
      return """Your username is %s...
                Yoo... %s
                Your password is hashed and secure
                To hackers your Password is: %s (simplified)
                """.format(self.U_name, self.Name, "ha28$" + "hashed password"[::5])

@web_page.context_processor
def base():
    search = Search()
    return dict(search = search, forms = forms)


@web_page.errorhandler(404)
def ERROR404(error):
    error = str(error)
    error = error.split('.')
    return render_template('not_found.html', error = error)


@web_page.route('/')
def home():
    return render_template('home.html')

@web_page.route('/search', methods = ["GET", "POST"])
def search(): 
    return "etwzbwetrbxtz zs"

@web_page.route('/register', methods = ["GET", "POST"])
def register():
    form = Register()
    forms.append(form)
    users = Accounts.query.order_by(Accounts.Name)
    if form.validate_on_submit():
        # sim_e_user = Accounts.query.filter_by(Email=form.email.data).first()
        sim_u_user = Accounts.query.filter_by(U_name=form.username.data)
        # if sim_e_user:
        #     flash(f"Someone already has this email address - {form.email.data}")
        if sim_u_user:
             flash(f"Someone already has this username - {form.username.data}", category = "warning")
        if not (sim_u_user): # and sim_e_user):
            # Email = form.email.data , Age = form.age.data)
            new_user = Accounts(Name = form.name.data, U_name = form.username.data)
            db.session.add(new_user)
            db.session.commit()
            form.username.data = ''
            form.name.data = ''
            flash("Your Registration has been succesfull", category="info")
            flash("Login Here", category="info")
            return render_template("log-in.html", form = form)
    else:
        return render_template("sign-in.html", form = form, users = users)

@web_page.route("/login", methods = ["GET", "POST"])
def login():
    form = Login()
    loc = len(forms)
    forms.append(form)
    forms.pop(loc)
    return render_template("log-in.html", form = form)

@web_page.route("/diffin")
def diffin():
    form = LoginForm()
    return render_template('diffin.html', title='Sign In', form=form)


if __name__ == '__main__':
    web_page.debug = True
    web_page.run(debug
     = True)