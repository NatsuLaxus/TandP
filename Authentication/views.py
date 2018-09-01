from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserLoginForm
from .models import *


def is_member(user):
	return user.groups.filter(name='Admin(taff)').exists()

def index(request):
	return render(request, 'Authentication/index.html',{})

# for registering students
def register_page(request):
	if request.method == 'POST':
		
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			username = userObj['username']
			email = userObj['email']
			password= userObj['password']
			firstname = userObj['first_name']
			lastname = userObj['last_name']
			regnum = userObj['regnum']
			branch = userObj['branch']
			course = userObj['course']
			contact = userObj['contact']

			if Userprofile.objects.filter(regNum = regnum).count()>0:
				return render(request,'Authentication/register.html',{'error':'this reg.no has already been taken','form': form})

			elif not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
				user = User.objects.create_user(username= username, password=password)
				user.set_password(password)
				user.first_name = firstname
				user.last_name = lastname
				user.save()
				login(request,user)
				profile = Userprofile.objects.create(user = request.user)
				profile.regNum = regnum
				profile.branch = branch
				profile.course = course
				profile.contact = contact
				profile.save()
				return redirect('/home/')
			else:
				return render(request , 'Authentication/register.html',{'error':'Username/email not avalible', 'form':form})
	else:
		form=UserRegistrationForm()

	return render(request,'Authentication/register.html',{'form': form})

# for students login . only after students has registered.
def login_page(request):
	if request.method == "POST":
		
		form = UserLoginForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			username = userObj['username']
			password = userObj['password']
			user = authenticate(username= username , password=password)
			if user is not None:
				login(request,user)
				if(is_member(user)):
					return HttpResponseRedirect('/home')
				else:
					forms.ValidationError('password/username is wrong')
	else:
		form=UserLoginForm()
	
	return render(request,'Authentication/login.html',{'form': form})

@login_required(login_url='login/')
def logout_page(request):
	logout(request,user)
	return redirect('/login')