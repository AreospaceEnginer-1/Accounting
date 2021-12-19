from flask import request, render_template, make_response, redirect, url_for
from .WTF import Account
from .__init__ import web_page

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


@web_page.errorhandler(404)
def ERROR404(code):
    code = str(code)
    code = code.split('.')
    return render_template('not_found.html', code = code)


@web_page.route('/')
def home():
    return render_template('home.html')
     

@web_page.route('/create_account', methods = ["POST"])
def create_account():
    pass

@web_page.route("/join_account")
def join_account():
    pass

@web_page.route("/log-in")
def login():
    return render_template('log-in.html')


@web_page.route("/sign-in")
def signin():
    return render_template('sign-in.html')

if __name__ == '__main__':
    web_page.run(host = "http://www.shamith.com", debug = True, port=12345)