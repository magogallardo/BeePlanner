from flask import render_template, session, redirect, url_for
from settings import app
# import os


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    session['user_name'] = ''
    if 'user_name' not in session:
        status_log = 'Login'
        icon_log = 'account_circle'
        redirect_log = 'login'

        status_account = 'Sign up'
        icon_account = 'person_add'
        redirect_accoutn = 'register'

    else:
        status_account = 'Profile'
        icon_account = 'settings'
        redirect_accoutn = 'profile'

        status_log = 'Logout'
        icon_log = 'exit_to_app'
        redirect_log = 'logout'

    return render_template('index.html', title='HOME',
                           status_log=status_log, icon_log=icon_log,
                           redirect_log=redirect_log,
                           status_account=status_account,
                           icon_account=icon_account,
                           redirect_accoutn=redirect_accoutn
                           )


@app.route('/login')
def login():
    return render_template('login.html', title='LOGIN')


@app.route('/logout')
def logout():
    session.pop('user_name', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
