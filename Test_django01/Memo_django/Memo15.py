# クエリストリングの色々な取り出し方。
# これまじで使える。
# 同じ関数の中で、処理を分岐させることができるから、マジで使える。
# self.request.GET.get('') これ使っときゃ問題ない！
# request.GETは、クエストリングを辞書型で取得します。
# selfなくても、処理結果変わらない。

# -- HttpRequest -- #

http://127.0.0.1:8000/testapp/testform?q=100 

# -- views.py -- #

http://127.0.0.1:8000/testapp/testform/check03?test=try

class ImageDealingView(FormView):
    # self.request.GETだろうと、request.GETだろうと変わらんやん。
    def post(self, request):
        obj = request.GET['test']
        print(obj)
        print(type(obj))
        obj_01 = self.request.GET['test']
        print(obj_01)
        print(type(obj_01))
        obj_02 = request.FILES['image']
        print(obj_02)
        print(type(obj_02))
        obj_03 = self.request.FILES['image']
        print(obj_03)
        print(type(obj_03))
        return HttpResponse('hi')

# 処理結果⇩

try
<class 'str'>
try
<class 'str'>
Enemy01_killed.png
<class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
Enemy01_killed.png
<class 'django.core.files.uploadedfile.InMemoryUploadedFile'>

# selfなくても、処理結果変わらない。

# -- views.py -- #

def testform(request):
    if request.method == 'GET':
        meta_querystring = request.META['QUERY_STRING']
        print(meta_querystring)
        return HttpResponse('hello')

>>> q=100

# -- views.py -- #

def testform(request):
    if request.method == 'GET':
        print(request.GET)
        return HttpResponse('hello')

>>> <QueryDict: {'q': ['100']}>