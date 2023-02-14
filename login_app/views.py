from django.shortcuts import render,HttpResponseRedirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse,reverse_lazy
from .models import UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up(request):
    form = CreateUserForm
    registered = False
    if request.method=='POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user=form.save()
            registered = True
            user_profile = UserProfile(user=user)
            return HttpResponseredirect(reverse('login_app:login'))

    diction = {'title':'Sign Up','form':form}
    return render(request,'login_app/signup.html',context=diction)

def log_in(request):
    form = AuthenticationForm
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            cleaned_data = form.clean()
            user = authenticate(username=cleaned_data['username'],password=cleaned_data['password'])

            if user is not None:
                login(request,user)
                pass
    diction = {'title':'Log In','form':form}
    return render(request,'login_app/login.html',context=diction)

@login_required
def edit_profile(request):
    pass
