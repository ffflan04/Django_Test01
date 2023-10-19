# request.GET/POST の使い方

# request.GET = GETメソッドの、クエリストリングを取得。
# request.POST = POSTメソッドの、リクエストボディ(送信内容)を取得。
# どちらも辞書ライク型でね。
# 重複したkeyには、getlist()だってよ。

# -- views.py -- #

def testform(request):
    if request.method == 'POST':
        print(request.POST) # formなどをpostメソッドで送れば、取得できる。
        return HttpResponse('hello')
    if request.method == 'GET':
        print(request.GET) # 末尾にクエリストリングを指定すれば、取得できる。
        return HttpResponse('hello')