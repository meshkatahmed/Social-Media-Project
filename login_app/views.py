from django.shortcuts import render,HttpResponseRedirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse,reverse_lazy

# Create your views here.
def sign_up(request):
    form = CreateUserForm
    registered = False
    if request.method=='POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            registered = True
            pass

    diction = {'title':'Sign Up','form':form}
    return render(request,'login_app/signup.html',context=diction)
