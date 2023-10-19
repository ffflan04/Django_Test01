# strメソッドとMetaクラスを使ってみた。

# ----- models.py --------- #

from django.db import models

class BulletinBoard(models.Model):
    user = models.CharField(max_length=255)
    food = models.CharField(null=True, max_length=200)
    hoby = models.TextField(null=True)
    age = models.IntegerField()
    sex = models.BooleanField()

    def __str__(self):
        return self.user

    class Meta:
        ordering = ['user']