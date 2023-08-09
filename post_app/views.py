from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required
def home(request):
    if request.method=='GET':
        search = request.GET.get('search','')
        result = User.objects.filter(username__icontains=search)
    diction = {'title':'Home','search':search,'result':result}
    return render(request,'post_app/home.html',context=diction)
