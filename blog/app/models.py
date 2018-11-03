from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=10,unique=True)
    pw = models.CharField(max_length=10,)
    create_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'user'


class Culumn(models.Model):
    culumn_name = models.CharField(max_length=20,unique=True)
    culumn_alias = models.CharField(max_length=10,null=True)
    culumn_father = models.CharField(max_length=10,null=True)
    culumn_key = models.CharField(max_length=10,null=True)
    culumn_description = models.CharField(max_length=100,null=True)
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'culumn'


class Article(models.Model):
    title = models.CharField(max_length=20,unique=True)
    label = models.CharField(max_length=20,null=True)
    comment = models.CharField(max_length=200,null=True)
    create_time = models.DateField(auto_now_add=True)
    option_time = models.DateField(auto_now_add=True)
    comm_count = models.IntegerField(default=0)
    status = models.BooleanField(default=0)
    culm = models.ForeignKey(Culumn)
    class Meta:
        db_table ="article"