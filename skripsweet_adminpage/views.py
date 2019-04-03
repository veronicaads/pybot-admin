from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index(request):
    return HttpResponse(render(request, 'form.html', None))

def process_form(request):
    data = request.POST.copy()
    # th = TransactionHeader()
    return HttpResponse(str(data))

