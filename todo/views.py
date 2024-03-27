from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser

# Create your views here.
def sign_up(request):
  if request.method == 'POST':
    fnm = request.POST.get('fnm')
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    new_user = User.objects.create_user(fnm, email, pwd)
    new_user.save()
    return redirect('/login')
  return render(request, 'signup.html')


def sign_in(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    user = authenticate(request, username = username, password = pwd)
    if user is not None:
      login(request, user)
      return redirect('/')
    else:
      return redirect('/login/') 
  return render(request, 'login.html')

def user_logout(request):
  logout(request)
  return redirect('/login/')

def todo(request):
  if isinstance(request.user, AnonymousUser):
    return redirect('/login/')
  
  if request.method == 'POST':
    title = request.POST.get('title')
    new_todo = Todo.objects.create(title=title, user=request.user)
    new_todo.save()
    res = Todo.objects.filter(user=request.user).order_by('-date')
    return redirect('/', {'res': res})
  
  res = Todo.objects.filter(user=request.user).order_by('-date')   
  
  return render(request, 'todo.html', {'User_Info': request.user, 'res': res})

def edit_todo(request, id):
  data = Todo.objects.get(no=id)
  if request.method == 'POST':
    title = request.POST.get('title')
    data.title = title
    data.save()
    res = Todo.objects.filter(user=request.user).order_by('-date')
    return redirect('/', {'res': res})
    
  return render(request, 'edit.html', {'data': data})

def del_todo(request, id):
  data = Todo.objects.get(no=id)
  data.delete()
  res = Todo.objects.filter(user=request.user).order_by('-date')
  return redirect('/', {'res': res})

def check_todo(request, id):
  data = Todo.objects.get(no=id)
  data.is_done = not data.is_done
  data.save()
  res = Todo.objects.filter(user=request.user).order_by('-date')
  return redirect('/', {'res': res})
    
    
  
