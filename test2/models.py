from django.db import models
from django.utils import timezone


class Member_info(models.Model):
    identity = models.CharField(max_length=200)

    name = models.CharField(max_length=200)
    myinfo = models.TextField()
    callnumber = models.IntegerField
    
    #성별 설정 필요
    
    created_date = models.DateTimeField(
        default=timezone.now)


    def __str__(self):
        return self.identity

# (사용자이름), 이름, 소개, 전화번호, 성별,























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
