from django.urls import path, include
from rest_framework import routers
from .views import *
app_name = 'post'

urlpatterns = [
    path('', todolist),
    path('create/', todocreate),
    path('delete/<str:id>/', tododelete),
    path('put/<str:id>/', todoupdate)
]