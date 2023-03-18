from flask import Blueprint, render_template, url_for, request, redirect

auth = Blueprint('auth', __name__)


@auth.route('/register')
def register():
    return render_template('register.html')


@auth.route('/register', methods=['POST'])
def reg_post():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    print(name, email, password)

    return redirect(url_for('auth.login'))


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return 'User Logout'
