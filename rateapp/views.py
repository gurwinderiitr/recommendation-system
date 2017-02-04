#!python
#rateapp/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/login/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'register.html',
    variables,
    )


@login_required(login_url="login/")
def home(request):
	return render(request,"home.html")
