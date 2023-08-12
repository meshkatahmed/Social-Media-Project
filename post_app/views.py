from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from login_app.models import UserProfile,Follow
from .models import Post

# Create your views here.
@login_required
def home(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts = Post.objects.filter(author__in=following_list.values_list('following'))
    if request.method=='GET':
        search = request.GET.get('search','')
        result = User.objects.filter(username__icontains=search)
    diction = {'title':'Home','search':search,'result':result,'posts':posts}
    return render(request,'post_app/home.html',context=diction)
