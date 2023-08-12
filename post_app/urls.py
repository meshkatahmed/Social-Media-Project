from django.urls import path
from . import views

app_name = 'post_app'

urlpatterns = [
    path('',views.home,name='home'),
    path('liked/<pk>/',views.like,name='like'),
    path('unliked/<pk>/',views.unlike,name='unlike'),
]
