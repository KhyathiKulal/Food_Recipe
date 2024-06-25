from django.urls import path
from .views import index, delete, update, login_page, register_page, logout_page
urlpatterns = [
    path("",index,name='home'),
    path("delete/<id>/",delete,name='delete'),
    path("update/<id>/",update,name='update'),
    path("login/",login_page,name='login'),
    path("logout/",logout_page,name='logout'),
    path("register/",register_page,name='register'),
]