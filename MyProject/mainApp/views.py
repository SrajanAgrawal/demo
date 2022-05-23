from django.shortcuts import render
import mysql.connector as sql
# creating some global variables
us = ''
em = ''
pswd = ''
usL = ''
pswdL = ''

# Create your views here.
def index(request):
    return render(request , 'first.html')
def home(request):
    return render(request , 'home.html')
def faceSignUpSystem(request):
    global us , em , pswd 
    if request.method=="POST":
        m=sql.connect(host='localhost' , user='root' , password='mysql' , database='srajan')
        cursor = m.cursor()
        d=request.POST
        for key , value in d.items():
            if key=="user_name":
                us = value
            if key=="email":
                em = value
            if key=="password":
                pswd = value
        c = "insert into one Values('{}','{}','{}')".format(us,em,pswd)
        cursor.execute(c)
        m.commit()
    return render(request , 'signup_page.html')
def faceLoginSystem(request):
    global usL , pswdL
    if request.method == "POST":
        m=sql.connect(host='localhost' , user='root' ,password='mysql' , database='srajan')
        cursor = m.cursor()
        d=request.POST
        for key ,value in d.items():
            if key=="user_name":
                usL = value
            if key=="password":
                pswdL = value
        c = "select * from one where user_name='{}' and password='{}'".format(usL , pswdL)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render (request , 'error.html')
        else:
            return render(request , 'welcome.html')
    return render(request , 'login_page.html')