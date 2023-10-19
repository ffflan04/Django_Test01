# views.pyで、データベースにデータを保存するメソッドを実装することに成功

# ------ views.py --------- #

from django.shortcuts import render, HttpResponse
from .models import BulletinBoard
from http.client import HTTPResponse

def document01(request):
    person = BulletinBoard.objects.all()
    context = {'features': person}
    return render(request, 'testapp/sakuhin.html', context)

def AddField(request):
    bb = BulletinBoard()
    bb.user = '忍野メメ'
    bb.food = 'ドーナツ'
    bb.hoby = 'お祓い'
    bb.age = 32
    bb.sex = True
    bb.save()
    return HttpResponse("helloworld")
