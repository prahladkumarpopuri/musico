from django.shortcuts import render, redirect
from.import forms
from.import models
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def signup(request):
	if request.method=='POST':
		form=forms.Register(request.POST)
		if form.is_valid():
			form.save()
			models.Otherdetails(
			user=User.objects.get(username=form.cleaned_data.get('username')),
			bio=form.cleaned_data.get('bio'),
			dob=form.cleaned_data.get('date_of_birth')).save()
			return HttpResponse("user saved")
		else:
			return render (request,'userauth/signup.html',{'form':form})
	else:
		form=forms.Register()
	return render(request,'userauth/signup.html',{'form':form})
def login_user(request):
	if request.user.is_authenticated:
		return HttpResponse("You are already Logged in")
	else:
		if request.method=='POST':
			username=request.POST['username']
			password=request.POST['password']
			user=authenticate(username=username,password=password)
			if user is not None:
				if user .is_active:
					login(request,user)
					return redirect('/music/list/')
				else:
					return render(request,'userauth/login.html',{'err':'Your account has been BLOCKED'})
			else:
				return render(request,'userauth/login.html',{'err':'Wrong Credentials'})
		else:
			return render(request,'userauth/login.html',{'err':''})