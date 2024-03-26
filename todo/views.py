from django.shortcuts import render

# Create your views here.
def sign_up(request):
  if request.method == 'POST':
    fnm = request.POST.get('fnm')
    email_id = request.POST.get('email')
    pwd = request.POST.get('pwd')
    re_pwd = request.POST.get('re_pwd')
    
    print(fnm, email_id, pwd, re_pwd)
  return render(request, 'signup.html')
