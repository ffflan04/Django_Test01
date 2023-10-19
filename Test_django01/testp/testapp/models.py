from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class CommentData(models.Model): # コメントのデータベース
    user = models.CharField(max_length=200)
    user_icon = models.ImageField(null=True)
    email = models.EmailField()
    body = models.TextField()
    like = models.IntegerField(default=0)
    good_bool = models.BooleanField(default=False) # 一人のユーザーが、一つのツイートにいいねした判定子ですが、LikedBoolモデルのフィールドを反映させる形で使用してます。
    time_date = models.DateTimeField(auto_now_add=True)

class Self_Introduction(models.Model): # 自己紹介用のデータベース
    user = models.CharField(max_length=200)
    body = models.TextField(default='自己紹介してくだせぇ')
    image = models.ImageField(default='one.png')

class LikedBool(models.Model): # ユーザーが、ツイートにいいねした履歴
    byuser = models.CharField(max_length=200)
    tweet = models.IntegerField(default=0)
    like_bool = models.BooleanField(default=False)

class DM_strage(models.Model): # ユーザー同士のチャットを記録するデータベース
    send_user = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    to_user = models.CharField(max_length=200)
    time_date = models.DateTimeField(auto_now_add=True)

class Image_strage(models.Model): # テスト用
    kyara = models.CharField(max_length=200) 
    image = models.ImageField(default='one.png') # 初期値入るやーーーーん！！！

# フォロー、フォロワーの仕組みを作ってください！！
class FF_bool(models.Model): # 同じ人をフォローできないようにするスイッチの役割を持つデータベース。
    userby = models.CharField(max_length=200)
    be_followed = models.CharField(max_length=200)
    follow_switch = models.BooleanField(default=False)

class FF_total(models.Model): # フォロー、フォロワーの合計を記録
    user = models.CharField(max_length=200)
    followed = models.IntegerField(default=0)
    follower = models.IntegerField(default=0)






