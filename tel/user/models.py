from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=10,unique=True,verbose_name='姓名')
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30,null=True)
    create_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'user'


class UserToken(models.Model):
    token = models.CharField(max_length=30,verbose_name='标识符')
    user = models.OneToOneField(User)

    class Meta:
        db_table =  'token'