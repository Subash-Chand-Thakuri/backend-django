from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    # return HttpResponse("Hello from home page")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("Hello from about page")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("Hello from contact page")
    return render(request, 'website/contact.html')