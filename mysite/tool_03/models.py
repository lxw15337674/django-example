from django.db import models

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=50, default='default name')
    user_id = models.IntegerField(default=1)
    user_name = models.CharField(max_length=10, default='default user_name')
    content = models.CharField(max_length=500, default="default content")
    created_at = models.IntegerField(default=1514879938)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=50, default='default name')
    user_id = models.IntegerField(default=1)
    user_name = models.CharField(max_length=10, default='default user_name')
    content = models.CharField(max_length=500, default="default content")
    created_at = models.IntegerField(default=1514879938)
