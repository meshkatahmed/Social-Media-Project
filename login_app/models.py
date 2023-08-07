from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    description = models.TextField(blank=True)
    full_name = models.CharField(max_length=264,blank=True)
    dob = models.DateField(blank=True,null=True)
    website = models.URLField(blank=True)
    facebook_id = models.URLField(blank=True)

class Follow(models.Model):
    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    date_created = models.DateTimeField(auto_now_add=True)
