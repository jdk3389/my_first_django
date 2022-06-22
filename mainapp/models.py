# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    # 테이블 필드 중에서 다른 테이블의 행과 식별할 수 있는 키를 의미
    # post 테이블의 댓글 테이블을 연결하기 위해
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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

class Box(models.Model):
    shipId = models.FloatField(default=0)
    width = models.FloatField()
    depth = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    underWaterVolume = models.FloatField()
    globalShipPosition = models.TextField()
    shipAttitude = models.TextField()
    localCOG = models.TextField()
    globalCOG = models.TextField()
    localCOB = models.TextField()
    globalCOB = models.TextField()
    draft = models.FloatField()
    heel = models.FloatField()
    trim = models.FloatField()


class Ship(models.Model):
    shipId = models.IntegerField(default=0, primary_key=True)
    width = models.FloatField()
    depth = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    underWaterVolume = models.FloatField()
    globalShipPosition = models.TextField()
    shipAttitude = models.TextField()
    localCOG = models.TextField()
    globalCOG = models.TextField()
    localCOB = models.TextField()
    globalCOB = models.TextField()
    draft = models.FloatField()
    heel = models.FloatField()
    trim = models.FloatField()
    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)
