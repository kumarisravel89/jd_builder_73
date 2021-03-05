from django.shortcuts import render, redirect
import json

# Create your views here.

def home(request):
    return render(request,"index.html")

def signIn(request):
    if request.method=="POST":
        pass
    return render(request,"sign_in.html")

def signUp(request):
    from .models import UserPasswordTable
    from django.http import HttpResponse
    if request.method=="POST":
        try:
            userPasswordTable = UserPasswordTable(UserName=request.POST.__getitem__('name'), UserEmail=request.POST.__getitem__('email'), Password1=request.POST.__getitem__('passwordConfirmed'))
            userPasswordTable.save()
            json_data=json.dumps({'value':'signed up successfully!'})
            return HttpResponse(json_data)

        except Exception as e:
            json_data=json.dumps({'value':'E-mail is Already taken please sign up other email!'})
            return HttpResponse(json_data)

    return render(request,'sign_up.html')



