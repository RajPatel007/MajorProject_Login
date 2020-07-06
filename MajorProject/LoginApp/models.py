from django.db import models


class AppUser(models.Model):
    firstname = models.CharField(unique=True, max_length=20)
    lastname = models.CharField(unique=True, max_length=20)
    email = models.CharField(unique=True, max_length=20)
    password = models.CharField(unique=True, max_length=30)


class UserBlog(models.Model):
    blogheader = models.CharField(max_length=100)
    blog = models.CharField(max_length=500)
    userid = models.ForeignKey(AppUser, on_delete=models.CASCADE)
