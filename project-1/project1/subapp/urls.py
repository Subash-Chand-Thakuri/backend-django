
from django.urls import path
from . import views

urlpatterns = [
    path('',views.sub_app, name='sub_app'),
    path('<int:shoe_id>/',views.shoe_detail, name='shoe_detail'),
]