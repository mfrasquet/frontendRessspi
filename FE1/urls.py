# Create your views here.
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


import os

urlpatterns = [
    path('',views.index,name='index'),
    path('simulator',views.simulator,name='simulator'),
]