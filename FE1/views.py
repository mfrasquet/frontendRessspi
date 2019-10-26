from django.shortcuts import render
from .auxFunctions import *

# Create your views here.



def index(request):
    return  render(request, 'FE1/index.html',{})

def simulator(request):
    lang_text=langText('eng')
    return  render(request, 'FE1/simulator.html',{'lang_text':lang_text})