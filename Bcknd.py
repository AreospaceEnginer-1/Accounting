
from flask import Flask, request, render_template, abort, make_response, redirect, url_for
import sqlite3

app = Flask('Account')
app.secret_key = "#!$1#5!R9*₹^UPP@s^₹*%2!6#10$#"

def get_uname(request):
    
    u_name = request.cookies.get("User Private Protectd Info", False)

    if not u_name:
        redirect(url_for("login"))

    return u_name


def set_cookie():

    head = "User Private Protectd Info"
    head = bytes(head, 'utf-8')

    user_infos = lister(request)

    u_name_pass = "\n".join(user_infos[-2:])
    u_name_pass = bytes(u_name_pass, 'utf-8')

    response = make_response('This site uses cookies')
    response.set_cookie(head, u_name_pass)


@app.route('/')
def home():
    return render_template('home.html')


def lister(request):

    user_infos = list()
    
    user_infos.append(request.form.get('f_name', False))
    user_infos.append(request.form.get('l_name', False))
    user_infos.append(request.form.get('email', False))
    user_infos.append(request.form.get('address', False))
    user_infos.append(request.form.get('pincode', False))
    user_infos.append(request.form.get('DOB', False))
    user_infos.append(request.form.get('u_name', False))
    user_infos.append(request.form.get('password', False))
    request.form.get('func', False)

    return user_infos


def check_info(request):
    p = str(request.form.get('password', False))
    c_p = str(request.form.get('c_password', False))
    
    if p != c_p:
        pas = ".".join([p, c_p])
        return pas

    return "<h1 Your Registering is being processed>"
        


@app.route('/create_account', methods = ["POST"])
def create_account():

    with sqlite3.connect('ShamithApp.db', check_same_thread=False) as db:
        cur = db.cursor()
            
        check_info(request)

        user_infos = lister(request)

        cur.execute("INSERT INTO persons (F_name, L_name, U_name, Email, Addr, PINCODE, DOB, Password) VALUES (?,?,?,?,?,?,?,?)", \
            user_infos)
             
        db.commit()

        return redirect(url_for("login"))

@app.route("/join_account")
def join_account():

    with sqlite3.connect('ShamithApp.db', check_same_thread=False) as db:
        cur = db.cursor()
        u_name = get_uname(request)
        cur.execute("SELECT * FROM persons WHERE U_name = ? and Password = ?", u_name)
        

        return

@app.route("/log-in")
def login():
    return render_template('log-in.html')


@app.route("/sign-in")
def signin():
    return render_template('sign-in.html')

if __name__ == '__main__':
    app.run(debug = True)