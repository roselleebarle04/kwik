from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import *
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset, password_reset_confirm

def signup(request):
	if request.method == 'POST':	
		form = UserCreationForm(request.POST or None)

		if form.is_valid():
			username = request.POST.get("username")
			email = request.POST.get("email")
			password1 = request.POST.get("password1")
			password2 = request.POST.get("password2")

			user = User.objects.create_user(username, email, password1)
			user.save()
			
			# new_user = form.save(commit=False)
			# new_user.save()

			# avatar = request.FILES.get("avatar")

			# # We need to create an account for the user created.
			# new_account = Account(user=new_user, avatar=avatar)
			# new_account.save()

			return HttpResponseRedirect('/login/')
	else:
		# form = AccountForm()
		form = UserCreationForm()

	return render(request, 'accounts/signup.html', {'form':form})