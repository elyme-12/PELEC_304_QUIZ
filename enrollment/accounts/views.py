from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm

def register_user(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Account created successfully! You can now log in.')
      return redirect ('login_user')
    else:
      messages.error(request, 'Please correct the errors below.')

  else:
    form = RegisterForm()
  
  return render(request, 'accounts/register.html', {'form': form})
     

def login_user(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login (request, user)
        messages.success(request, f'Welcome Back, {username}!')
        return redirect('dashboard')
      else:
        messages.error(request, 'Invalid Username and Password.')
    
    else:
      messages.error (request, 'Invalid input.')
  
  else:
    form = AuthenticationForm()
  return render(request, 'accounts/login.html', {'form': form}) 


def logout_user(request):
  logout(request)
  messages.info(request, 'You have been logged out')
  return redirect('login_user')

def dashboard(request):
  return render(request, 'accounts/dashboard.html')