from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.utils import timezone

class Episode(models.Model):
    episode_id = models.PositiveIntegerField(verbose_name='ID',primary_key=True,auto_created=True,null=False,unique=True)
    contributor = models.ForeignKey('Grateful_User.User',verbose_name='投稿者',null=False,on_delete=models.CASCADE)
    episode = models.CharField(verbose_name='感謝の言葉',null=False,blank=False,max_length=1000)
    contribute_date = models.DateField(verbose_name='投稿日時',null=False,auto_now_add=True)
    be_grateful_count=models.PositiveIntegerField(verbose_name='感謝された回数',default=0)
    public=models.BooleanField(verbose_name='公開有無',null=False,default=True)
