from django.contrib import admin
from django.urls import path
from .views import index, delete, update
urlpatterns = [
    path("",index,name='home'),
    path("delete/<id>/",delete,name='delete'),
    path("update/<id>/",update,name='update'),
]