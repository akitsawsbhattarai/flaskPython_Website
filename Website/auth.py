from flask import Blueprint,render_template, request,flash,redirect,url_for
import re
from .models import User
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,login_required,logout_user,current_user

auth=Blueprint('auth',__name__)
users=[]

@auth.route('/login', methods=['GET','POST'])
def login():
    msg={}
    email=''
    if request.method=='GET':
        print('It is get methods' )
    else: 
        email=request.form.get('email')
        password=request.form.get('password')

        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in sucessfully',category='sucess')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                msg['incorrectPassword']="Incorrect password"
        else:
            msg['noUser']="Email doesnot exist"


        print('It is post methods' )
    
    return render_template("login.html",context={'msg':msg,'email':email})
   

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup',methods=['GET','POST'])
def Sign_in():
    msg={}
    
    valid=False
    email=''
    if request.method=='GET':
        print('It is get methods' )
    if request.method=='POST':
        has_error = False 
        email=request.form.get('email')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        if email=="":
            flash('email mustn\'t be empty',category='error')
            has_error = True 

        if password1 == "":
            msg['password'] = "Password is required"
            has_error = True 
            
        if password2 == "":
            msg['password'] = "Password is required"
            has_error = True        

        if not has_error:
            user={}
            if ( 8<=len(password1)<=20):
                if re.search('[a-z]',password1):
                        if re.search('[A-Z]',password1):
                            if re.search("[0-9]", password1):
                                if re.search("[ !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]",password1):
                                    if  password1==password2:
                                        user['password']=password1
                                        print(user['password'])
                                        valid=True
    
                                    else:
                                        has_error = True 
            
            if has_error:
                msg['password']="password doesnot matched"
                                                                      
            elif not valid:
                msg['password'] = "Invalid Password"  
                has_error = True                 
        

        if not has_error:
            useR=User.query.filter_by(email=email).first()
            if useR:
                flash('email already exists',category='error')
            else:
                user['email']=email
                users.append(user)
                # creating table first to avoid operational error
                db.create_all()
                new_user=User(email=email,password=generate_password_hash (password1,method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                flash('sucessfully registered',category='sucess')
                login_user(user,remember=True)
                print(user)
                print(users)
                return redirect(url_for('views.home'))

        print('It is post methods' )

    return render_template("sign_up.html",context={'msg':msg,'email':email})