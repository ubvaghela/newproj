from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/',views.post,name='post'),
    path('post_update/',views.post_update,name="post_update")
]