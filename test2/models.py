from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
##
from django.conf import settings



class Member_info(models.Model):
    identity = models.CharField(max_length=200)

    name = models.CharField(max_length=200)
    myinfo = models.TextField()
    callnumber = models.IntegerField

    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.identity


##

class My_under(models.Model):
    identity = models.CharField(max_length=200)
    my_unders = models.ManyToManyField(Member_info)

    def __str__(self):
        return self.identity


class My_role(models.Model):
    identity = models.CharField(max_length=200)
    my_roles = models.ManyToManyField(Member_info)

    def __str__(self):
        return self.identity

#성별 설정 필요
# (사용자이름    ), 이름, 소개, 전화번호, 성별,


#####

def user_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    return '%s/%s.%s' % (instance.owner.username, pid, extension)


class Post(models.Model):
    identity = models.CharField(max_length=200)

    story = models.TextField()
    photo = models.FileField(null=True)
    published_date = models.CharField(max_length=20)

    created_date = models.DateTimeField(
        default=timezone.now)






















class Community_post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




# Create your models here.
