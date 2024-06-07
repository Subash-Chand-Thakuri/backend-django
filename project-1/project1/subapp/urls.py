
from django.urls import path
from . import views

urlpatterns = [
    path('',views.sub_app, name='sub_app'),
]