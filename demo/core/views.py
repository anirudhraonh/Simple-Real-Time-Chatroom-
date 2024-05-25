from django.shortcuts import render,redirect,HttpResponse
from .forms import Signupform
from django.contrib.auth import login
# Create your views here.
def frontpage(request):
    return render(request,'core/frontpage.html')

def signup(request):
    if request.method == 'POST': #if form has been submitted
        form = Signupform(request.POST)

        if form.is_valid():
            user = form.save() #create user save form data

            login(request,user)

            return redirect('frontpage')# 'frontpage' refers to name of url specified in urls.py
        
    else:
        form = Signupform()

    return render(request,'core/signup.html',{'form':form})




