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
    # session['username'] = ''
    kwargs = logged_args()
    redirect_page = 'schedule.html' if 'username' in session else 'index.html'
    return render_template(redirect_page, title='HOME', **kwargs)


@app.route('/login', methods=['GET'])
def login():
    def render_this_page():
        kwargs = logged_args()
        return render_template('login.html', title='LOGIN', **kwargs)
    if request.form:
        username = request.form['username']
        password = request.form['password']
        response = controller.login(username, password)
        if response == InfoCodes.USER_NOT_FOUND:
            return render_this_page()
        if response == InfoCodes.WRONG_PASSWORD:
            return render_this_page()
        if response == InfoCodes.SUCCESS:
            session['username'] = username
            return redirect(url_for('home'))

    return render_this_page()


@app.route('/register')
def register():
    kwargs = logged_args()
    return render_template('register.html', title='REGISTER', **kwargs)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
