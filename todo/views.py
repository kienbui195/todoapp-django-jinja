from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def sign_up(request):
  if request.method == 'POST':
    fnm = request.POST.get('fnm')
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    new_user = User.objects.create_user(fnm, email, pwd)
    new_user.save()
    return redirect('/todo/login')
  return render(request, 'signup.html')


def sign_in(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    user = authenticate(request, username = username, password = pwd)
    print(user)
    if user is not None:
      login(request, user)
      return redirect('/todo/')
    else:
      return redirect('/todo/login/') 
  return render(request, 'login.html')

def todo(request):
  if request.user is None:
    return redirect('/todo/login')
  if request.method == 'POST':
    title = request.POST.get('title')
    new_todo = Todo.objects.create(title=title, user=request.user)
    new_todo.save()
    res = Todo.objects.filter(user=request.user).order_by('-date')
    return redirect('/todo/', {'res': res})
  res = Todo.objects.filter(user=request.user).order_by('-date')   
  
  return render(request, 'todo.html', {'User_Info': request.user, 'res': res})
