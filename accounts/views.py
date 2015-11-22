from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

def login(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'accounts/login.html', {})

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	print "Username " + username
	print user
	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/account/')
	else:
		return HttpResponseRedirect('/account/invalid')
	return render(request, 'accounts/login.html', {})

def signup(request):
	return render(request, 'accounts/signup.html', {})

# @login_required
def dashboard(request):
	return render(request, 'accounts/dashboard.html', {
		'person': request.user.username
	})

# @login_required
def postings(request):
	return render(request, 'accounts/postings.html', {})

# @login_required
def drafts(request):
	return render(request, 'accounts/drafts.html', {})

# @login_required
def bookmarks(request):
	return render(request, 'accounts/bookmarks.html', {})

# @login_required
def payments(request):
	return render(request, 'accounts/payments.html', {})
