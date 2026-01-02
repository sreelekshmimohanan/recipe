from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotAllowed
from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from urllib.parse import urlencode
from .models import *
from django.db.models import Q
from django.db.models import Sum
from decimal import Decimal

def first(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def cus_register(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        district=request.POST.get('district')
        street=request.POST.get('street')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if tbl_login.objects.filter(email=email).exists():
            # Email already exists, display an alert message
            return render(request, 'cus_register.html', {'msg': 'Email already exists. Please use a different email.'})
       
        cus=customer_reg(fname=fname,lname=lname,district=district,street=street,phone=phone,gender=gender,dob=dob,email=email,password=password)
        cus.save()
        cus1= tbl_login(email=email,password=password,user_type='customer')
        cus1.save()
        return render(request,"index.html", {'message':'Succesfully Registered'})
    else:
        return render(request,"cus_register.html")
    
def login(request):
    return render(request,'login.html')

def addlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
        request.session['logintdetail'] = email
        request.session['admin'] = 'admin'
        return redirect(first)
    elif customer_reg.objects.filter(email=email, password=password).exists():
        userdetails = customer_reg.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['cuid'] = userdetails.id
            request.session['cuname'] = userdetails.fname
            request.session['cuemail'] = email

            return redirect(index)
        
    

    else:
        return render(request, 'login.html', {'message':'Invalid Email or Password'})
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)




def cus_profile(request):
    staff=customer_reg.objects.get(id=request.session['cuid'] )
    return render(request,'cus_profile.html',{'result':staff})





def view_user_pro(request):
   
    result=customer_reg.objects.all()
    return render(request,'view_user_pro.html',{'data':result})