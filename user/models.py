#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
#장고의 기본모델 클래스(auth_user연동)

# Create your models here.
class UserModel(AbstractUser):#상속
    class Meta:
        db_table = "my_user"

    bio = models.CharField(max_length=256, default='')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')
