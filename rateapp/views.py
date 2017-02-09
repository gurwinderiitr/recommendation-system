#!python
#rateapp/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import *
from .models import *

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating

@csrf_protect
def loginview(request):
	loginerror = False
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		print "NEW METHOD ",username,password
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			#redirect
			return HttpResponseRedirect('/')
		else:
			loginerror = True
	context = {'form': LoginForm, 'loginerror': loginerror}
	# context['errors'] = loginerror
	return render( request, 'login.html', context)

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # print "FORM    ",form
        print "POST    ",request.POST
        print form.is_valid()
        if form.is_valid():
			user = User.objects.create_user(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['password1'])
			name_t = form.cleaned_data['name']
			enrollment_t = form.cleaned_data['enrollment']
			semester_t =form.cleaned_data['semester']
			branch_t = form.cleaned_data['branch']
			username_t =form.cleaned_data['username']
			email_t =form.cleaned_data['email']
			print "Adding new entry to UserTable"
			entry = UserTable(username = username_t, email = email_t, name = name_t, enrollment = enrollment_t, semester = semester_t, branch = branch_t, hasrated = False)
			entry.save()
			print "New Entry Added!"
			return HttpResponseRedirect('/login/')
    else:
        form = RegistrationForm()
    print "Inside REGISTER"
    print request
    print request.body
    print request.method
    context = {'form':form}
    return render( request, 'register.html', context)


@login_required(login_url="login/")
def home(request):
	return render(request,"home.html")

@login_required(login_url="login/")
def rate(request):
	return render(request,"rate.html")