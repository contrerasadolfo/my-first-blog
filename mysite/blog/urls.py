from django.urls import path
from . import views

""" patron URL
se asocia una vista(view) llamada post_list
a la URL raiz
"""
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
