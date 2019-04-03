from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index(request):
    return HttpResponse(render(request, 'views/form.html', None))
