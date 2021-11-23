from flask import Blueprint

auth=Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return '<p>LOGIN</p>'

@auth.route('/logout')
def logout():
    return '<p>LOGout</p>'

@auth.route('/sign_in')
def Sign_in():
    return '<p>Sign_in</p>'