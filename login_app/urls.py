from django.urls import path
from . import views

app_name = 'login_app'

urlpatterns = [
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.log_in,name='login'),
]
