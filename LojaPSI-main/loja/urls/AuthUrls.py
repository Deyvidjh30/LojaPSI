from django.urls import path
from loja.views.AuthView import login_view
from loja.views.AuthView import register_view
from loja.views.AuthView import logout_view

urlpatterns = [
    path("login/", login_view, name='login'),
    path("register/", register_view, name='register'),
    path("logout", logout_view, name='logout'),
]