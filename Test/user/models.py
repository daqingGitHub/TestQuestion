from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class ScoreUser(models.Model):
    # 客户端号
    clientNumber = models.CharField(max_length=6,null=True,blank=True)
    # 分数
    score = models.IntegerField(null=True,blank=True,default=0)

    class Meta:
        db_table='clients'
        # ordering=('score',)

    def __str__(self):
        return self.clientNumber
