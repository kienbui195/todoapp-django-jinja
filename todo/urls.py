from django.urls import path
from .views import sign_up, sign_in, todo

urlpatterns = [
    path('', todo, name="todoList"),
    path('sign-up/', sign_up, name='signUp'),
    path('login/', sign_in, name="login"),
]
