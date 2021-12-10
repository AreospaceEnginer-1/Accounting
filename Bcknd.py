from flask import Flask, request, render_template, make_response, redirect, url_for
from flask_sqlalcemy import SQLAlchemy
from WTF import Account

app = Flask('Account') 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///acounts.db"
app.config["SECRET_KEY"] = "#!$1#5!R9*₹^UPP@s^₹*%2!6#10$#"

db = SQLAlchemy(app) 
class Accounts(db.Model):
    
    Id = db.Column(db.Integer, primary_key=True) 

def get_uname(request):
    
    u_name = request.cookies.get("User Private Protectd Info", False)

    if not u_name:
        set_cookie()

    return u_name


def set_cookie():

    head = "User Private Protectd Info"
    head = bytes(head, 'utf-8')

    user_infos = lister(request)

    u_name_pass = "\n".join(user_infos[-2:])
    u_name_pass = bytes(u_name_pass, 'utf-8')

    response = make_response('This site uses cookies')
    response.set_cookie(head, u_name_pass)

def lister(request):

    user_infos = list()
    
    user_infos.append(request.form['f_name'])
    user_infos.append(request.form['l_name'])
    user_infos.append(request.form['email'])
    user_infos.append(request.form['address'])
    user_infos.append(request.form['pincode'])
    user_infos.append(request.form['DOB'])
    user_infos.append(request.form['u_name'])
    user_infos.append(request.form['password'])

    return user_infos  


@app.errorhandler(404)
def ERROR404(code):
    code = str(code)
    code = code.split('.')
    return render_template('not_found.html', code = code)


@app.route('/')
def home():
    return render_template('home.html')
     

@app.route('/create_account', methods = ["POST"])
def create_account():

    with sqlite3.connect('ShamithApp.db', check_same_thread=False) as db:
        cur = db.cursor()

        user_infos = lister(request)

        return redirect(url_for("login"))

@app.route("/join_account")
def join_account():

    with sqlite3.connect('ShamithApp.db', check_same_thread=False) as db:
        cur = db.cursor()
        u_name = get_uname(request)
        cur.execute("SELECT * FROM persons WHERE U_name = ? and Password = ?", u_name)
        stuff = cur.fetchall()

        db.commit()
        return

@app.route("/log-in")
def login():
    return render_template('log-in.html')


@app.route("/sign-in")
def signin():
    return render_template('sign-in.html')

if __name__ == '__main__':
    app.run(debug = True)
