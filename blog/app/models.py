from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=10,unique=True)
    pw = models.CharField(max_length=10,)
    create_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'user'

