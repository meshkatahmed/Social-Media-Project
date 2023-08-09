from django.urls import path
from . import views

app_name = 'login_app'

urlpatterns = [
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.log_in,name='login'),
    path('editprofile/',views.edit_profile,name='editprofile'),
    path('logout/',views.log_out,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('user/<username>',views.user,name='user'),
]
