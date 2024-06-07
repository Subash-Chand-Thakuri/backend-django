from django.shortcuts import render

# Create your views here.
def sub_app(request):
    return render(request,'subapp/sub_app.html')
