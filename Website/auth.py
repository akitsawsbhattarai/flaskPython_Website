from flask import Blueprint,render_template, request,Response

auth=Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method=='GET':
        print('It is get methods' )
    else: 
        print('It is post methods' )
    
    return render_template("login.html", text="testing")
   

@auth.route('/logout')
def logout():
    return '<p>LOGout</p>'

@auth.route('/signup',methods=['GET','POST'])
def Sign_in():
    if request.method=='GET':
        print('It is get methods' )
    else: 
        print('It is post methods' )

    return render_template("sign_up.html")