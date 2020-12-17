from django.urls import path, include, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('<int:id>/',views.blogpost,name='blogpost'),
    path('<int:id>/likepost/',views.likepost,name='likepost'),
    #path('<int:id>/',views.postlikes,name='postlikes'),
    path('<int:id>/updatelike/',views.updatelike,name='updatelike'),
    path('login/',views.login_user,name='login_user'),
    path('logout/',views.logout_user,name='logout_user'),
    path('signup/',views.signup_user,name='signup_user'),
    path('password_change/',views.password_change,name='password_change'),
    path('new/add/',views.add_post,name='add_post'),
    path('<int:id>/edit',views.edit_post,name='edit_post'),
    path('post_delete/<int:id>',views.post_delete,name='post_delete'),
    path('comments/<int:id>',views.comments,name='comments'),
    path('password_reset/',views.password_reset,name="password_reset"),
    url(r'^password_reset_confirm/(?P<uidb36>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.password_reset_confirm,name="password_reset_confirm"),
    #path('password_reset_confirm/<uidb36>/<token>/',views.password_reset_confirm,name="password_reset_confirm"),
    path('password_reset_complete/',views.password_reset_complete,name="password_reset_complete"),
    path('profile/',views.user_profile,name="user_profile"),
    path('update_profile/',views.update_profile,name="update_profile"),
    
]