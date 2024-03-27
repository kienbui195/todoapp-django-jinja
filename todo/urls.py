from django.urls import path
from .views import sign_up, sign_in, todo, user_logout, edit_todo, del_todo, check_todo

urlpatterns = [
    path('', todo, name="todoList"),
    path('sign-up/', sign_up, name='signUp'),
    path('login/', sign_in, name="login"),
    path("logout/", user_logout, name="logout"),
    path("edit/<int:id>", edit_todo, name="edit"),
    path("del/<int:id>", del_todo, name="del"),
    path("check/<int:id>", check_todo, name="check")
]
