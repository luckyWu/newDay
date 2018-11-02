from django.contrib.auth.models import AbstractUser,User,Group
from django.db import models

# Create your models here.


class MyUser(AbstractUser):

    class Meta:
        #django默认给每个模型初始化三个权限
        #  change  , delete .add 权限
        permissions = (
            ('add_my_user','新增用户权限'),
            ('change_my_user_username', '修改用户权限'),
            ('change_my_user_password', '修改密码权限'),
            ('all_my_user', '查看用户权限'),
        )