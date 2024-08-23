from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def homeview(request):
    a=10
    return HttpResponse("<h1>Hello KaaliyeCharan...</h1>")