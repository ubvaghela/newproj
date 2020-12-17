from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='ShopHome'),
    path('about/',views.about, name='AboutUs'),
    path('contact/',views.contact, name='ContactUs'),
    path('tracker/',views.tracker, name='TrakingStatus'),
    path('search/',views.search, name='Search'),
    path('productview/<int:myid>',views.productview, name='ProductView'),
    path('checkout/',views.checkout, name='Checkout'),
    path('login/',views.login,name='Login'),
    path('stx/',views.stx,name='stx'),
    path('handlerequest/',views.handlerequest, name='HandleRequest'),
    
]
