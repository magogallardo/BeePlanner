from flask import render_template, session, redirect, url_for, request
from settings import app, db
from random import choice
from controller import Controller
from model import InfoCodes
modals_colors = (
    'red lighten-3',
    'amber lighten-3',
    'deep-orange accent-1',
    'blue-grey lighten-1',
    'amber accent-3',
    'lime lighten-2',
    'teal accent-3',
    'indigo lighten-3',
    'purple accent-1',
    'red lighten-2',
    'light-green lighten-2'
)

controller = Controller()


def get_random_color():
    return choice(modals_colors)


def render_this_page(url, title):
    kwargs = logged_args()
    return render_template(url, title=title, **kwargs)


def logged_args():
    if 'username' not in session:
        status_log = 'Login'
        icon_log = 'account_circle'
        redirect_log = 'login'

        status_account = 'Sign up'
        icon_account = 'person_add'
        redirect_account = 'register'
    else:
        status_account = 'Profile'
        icon_account = 'settings'
        redirect_account = 'profile'

        status_log = 'Logout'
        icon_log = 'exit_to_app'
        redirect_log = 'logout'

    return locals()


@app.route('/schedule')
def schedule():
    return render_template('schedule.html')


@app.route('/')
@app.route('/index')
@app.route('/home')
# @logged_args
def home():
    url = 'schedule.html' if 'username' in session else 'index.html'
    return render_this_page(url, 'HOME')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_this_page('login.html', 'LOGIN')
    else:
        if request.form:
            email = request.form['email']
            password = request.form['password']
            response = controller.login(email, password)
            if response == InfoCodes.USER_NOT_FOUND:
                return render_this_page('login.html', 'LOGIN')
            if response == InfoCodes.WRONG_PASSWORD:
                return render_this_page('login.html', 'LOGIN')
            if response == InfoCodes.SUCCESS:
                session['username'] = controller.get_username(email)
                return redirect(url_for('home'))

    return render_this_page('login.html', 'LOGIN')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if 'username' in session or request.method == 'GET':
        return render_this_page('register.html', 'REGISTER')
    elif request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        lastname = request.form['lastname']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        if not all([username, name, lastname, phone, email, password]):
            return render_this_page('register.html', 'REGISTER')
        else:
            response = controller.add_user(username, email, password,
                                           name, lastname, phone)
            if response == InfoCodes.USER_ALREADY_EXIST:
                return render_this_page('register.html', 'REGISTER')
            else:
                controller.save()
                return redirect(url_for('home'))

    return render_this_page('register.html', 'REGISTER')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
