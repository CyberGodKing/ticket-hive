from ast import Delete
from http.client import REQUEST_ENTITY_TOO_LARGE
from os import name
from urllib.request import Request
from wsgiref.util import request_uri
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect , HttpRequest 
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from .forms import RegisterUserForm , SetPasswordForm, PaymentForm
from django.contrib.auth.forms import UserCreationForm
from .models import  party ,Agent , Payment
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User 
# Create your views here.
import requests

def log_out(request):
    logout(request)
    return redirect('sign_in')


def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None :
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,('There was an error logging in, check credential and TRY AGAIN...'))
            return redirect('sign_in')
    else:
        return render(request,'sign_in.html',{})




def signup(request):
    if request.method=="POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,('Account created successfully...'))
            return redirect('home')
    else:
         form = RegisterUserForm()       
    return render(request,'sign_up.html',{'form':form})

#def login_user(request):
 #   return render(request,'login.html',{})   
def home(request):
    if request.user.is_authenticated == False:
        messages.success(request,('You need logging access before you can access page...'))
        return redirect("sign_in")
    else:
        if request.user.is_authenticated == True:
           return render(request,"home.html",{})   



def acc_info(request):
    #context    =   user_detail.objects.all()
    #info    = {"context":context,}
    if request.user.is_authenticated == False:
        messages.success(request,('You need logging access before you can access page...'))
        return redirect('sign_in')
    else:
        return render(request , "minor_pages/acc_info.html",{})
    

    
def update_login(request):
    user = request.user
    #edit   = user_detail.objects.get()
    if request.user.is_authenticated == False:
        messages.success(request,('You need logging access before you can access page...'))
        return redirect("sign_in")
    else:
        if request.method=="POST":
            form = SetPasswordForm(user,request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Password changed successfully..")
                return redirect('sign_in')
            else:
                messages.success(request,"Error updating password .TRY AGAIN..")
                return redirect("info")
        form = SetPasswordForm(user)
        return render(request,'tool/update_login.html',{"form":form})
    
def paymethod(request):
    return render(request,"tool/method.html",{})

        

def myticket(request):
    context    =   Payment.objects.all()
    info    = {"context":context,}
    if request.user.is_authenticated == False:
        messages.success(request,('You need logging access before you can access page...'))
        return redirect('sign_in')
    else:
        if request.user.is_authenticated == True:
            return render(request , "tool/tickets.html",info)


def initiate_payment(request: HttpRequest )-> HttpResponse:
    parti = party.objects.all()
    checks = Payment.objects.all()
    try :
        if request.user.is_authenticated== True:
            for obj in parti:
                global price
                price = obj.price
            for ob in checks :
                if ob.verified == False:
                    check = Payment.objects.get(verified=False)
                    check.delete()
        else:
            return redirect("sign_in")
    except party.DoesNotExist:
        pass
   
    if request.method== "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            user = payment_form.save(commit=False)
            cost = payment_form.save(commit=False)
            cost.amount = price
            user.name = request.user
            cost.save()
            user.save()
            payment = payment_form.save()
            return render(request,"make_payment.html",{"payment":payment,"paystack_public_key":settings.PAYSTACK_PUBLIC_KEY})
    else:
        payment_form= PaymentForm()
    return render(request,"initiate_payment.html",{"payment_form":payment_form,"parti":parti})


PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY #'sk_test_212aef506c8d43e3c4877ef5369800950d18d0b6'
base_url = "https://api.paystack.co"
header = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "content-type": "application/json",
    }



def verify_payment(request):
    global status
    ob = Payment.objects.all()
    try:
        if request.user.is_authenticated==True:
            #owner = Payment.objects.get(name=request.user)
            for obj in ob :
                if obj.name == request.user and obj.verified == False:
                    ref=obj.ref
                    path = f"/transaction/verify/{ref}"
                    url = base_url + path
                    response = requests.get(url,headers=header)
                    if response.status_code == 200:
                        obj.verified = True
                        obj.save()
                        status = "verified"
                    else:
                        status = "failed"
                else:
                    pass
    except Payment.DoesNotExist:
        pass
    except requests.ConnectionError:
        messages.success(request,"Error Validating Transection")
        return redirect('error')
    check = status
    if request.user.is_authenticated == True:
        messages.success(request,"Transaction Successfull .")
        if check == "verified":
            return redirect("ticket")
        else:
            messages.success(request,"Transaction Failed .")
            return render("home")
    else:
        messages.success(request,"you need loging access before viewing page")
        return redirect("sign_in")
    #return render(request,"home.html",{})

def errorvalidating(request):
    if request.user.is_authenticated == False:
        messages.success(request,"you need loging access before accessing page")
    else:
        if request.user.is_authenticated == True:
            return render(request,"minor_pages/error.html",{})