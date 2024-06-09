from django.shortcuts import render,get_object_or_404
from .models import ShoesVareity

# Create your views here.
def sub_app(request):
    shoes = ShoesVareity.objects.all()
    return render(request,'subapp/sub_app.html', {'shoes':shoes})

def shoe_detail(request, shoe_id):
    shoe = get_object_or_404(ShoesVareity, pk=shoe_id)
    return render(request,'subapp/shoe_detail.html', {'shoe':shoe})

