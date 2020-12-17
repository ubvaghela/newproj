from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/about/',views.about,name='about'),
    path('home/contact/',views.contact,name='contact'),
    path('home/search/',views.search,name='search'),
]