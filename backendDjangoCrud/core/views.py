from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def studentView(request):
    return HttpResponse("hi juba")
