# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#exception
from django.db.utils import IntegrityError
#models
from django.contrib.auth.models import User
from users.models import Profile

#form
from users.forms import ProfileForm, SignupForm

@login_required
def update_profile(request):
  profile = request.user.profile

  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      data = form.cleaned_data
      profile.website = data['website']
      profile.phone_numer = data['phone_numer']
      profile.biography = data['biography']
      profile.picture = data['picture']
      profile.save()

      return redirect('update_profile')
  else:
    form = ProfileForm()

  return render(
    request=request,
    template_name='users/update_profile.html',
    context={
      'profile': profile,
      'user': request.user,
      'form': form
    }
  )

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('feed')
		else:
			return render(request, 'users/login.html', { 'error': 'Invalid username and password'})
	return render(request, 'users/login.html' )

def signup(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     passwd = request.POST['passwd']
    #     passwd_confirmation = request.POST['passwd_confirmation']
    #     email = request.POST['email']

    #     if passwd != passwd_confirmation:
    #         return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

    #     u = User.objects.filter(email=email)
    #     if u:
    #       error = 'There is another account using {}'.format(email)
    #       return render(request, 'users/signup.html', {'error': error})

    #     try:
    #         user = User.objects.create_user(username=username, password=passwd)
    #     except IntegrityError:
    #         return render(request, 'users/signup.html', {'error': 'Username is already in user'})

    #     user.first_name = request.POST['first_name']
    #     user.last_name = request.POST['last_name']
    #     user.email = request.POST['email']
    #     user.save()

    #     profile = Profile(user=user)
    #     profile.save()

    #     return redirect('login')

    # return render(request, 'users/signup.html')
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = SignupForm()

  return render(
    request=request,
    template_name='users/signup.html',
    context={
      'form': form
    }
  )   

def detail(request):
  return render(
    request=request,
    template_name='users/detail.html',
    context={
     
    }
  )

@login_required
def logout_view(request):
	logout(request)
	return redirect('login')

