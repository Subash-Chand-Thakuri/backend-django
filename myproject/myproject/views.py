# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello I'am in the home page of django")
    return render(request, 'home.html')

def about(req):
    # return HttpResponse("I am in the about page")
    return render(req, 'about.html')