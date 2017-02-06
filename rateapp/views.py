#!python
#rateapp/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print "FORM    ",form
        print "POST    ",request.POST
        print form.is_valid()
        if form.is_valid():
            user = User.objects.create_user(
        	name = form.cleaned_data['name'],
            # enrollment = form.cleaned_data['enrollment'],
            # semester=form.cleaned_data['semester'],
            # branch = form.cleaned_data['branch'],
            # username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
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
