from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    diction = {}
    return render(request,'post_app/home.html',context=diction)
