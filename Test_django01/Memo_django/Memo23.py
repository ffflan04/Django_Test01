# 汎用ビューでのurlパラメータの受け取りかた
# クエリストリングとやってることは同じ、違いは、渡せる型の幅が広い。
# 汎用ビューのpostメソッドでは、self.kwargs.get() じゃなくて、postメソッドの引数に、urlパラメータをとります。
# self.kwargs.get()
# まさかの、self の中に格納されているとは...
# postメソッドで、urlパラメータを受け取る場合は、postメソッドの引数に、valueをとる必要があった。

# -- template -- #

<a href="http://127.0.0.1:8000/testapp/other_profile/{{tweet.user}}">{{tweet.user}}</a>

# -- urls.py -- #

path('other_profile/<str:other>/', views.OtherProfile.as_view()), # 他ユーザーページへの表示。

# -- views.py -- #

class OtherProfile(ListView):
    template_name = 'testapp/other_page.html'
    model = CommentData

    def get_context_data(self):
        context = {}
        print(self.kwargs.get('other')) # self.kwargs の中に、urlパラメータは格納されてる。
        return context
    
    def get(self, request):
        obj = request.GET.get('other') # requestからも、urlパラメータを引き出すことできるよ。
        return Httpresponse('hi')
    

class ImageDealingView(FormView): # テストメソッド

    def post(self, request, animal): # postメソッドで、urlパラメータを受け取るときは、self.kwargs.get('') では、獲得できない。
        chc = self.kwargs.get('animal') # 引数に、url.py で設定した、引数をとって、初めて、獲得できる。
        print(chc) # -> panda
        print(type(chc)) # -> urls.py で設定した型ですね。
        return HttpResponse('hello')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        obj = self.kwargs.get('animal')
        print(obj)
        print(type(obj))
        return context

# -- 関数ビューの場合 -- #

def test(request, slug):
    obj = User.objects.get(slug=slug)

# -- 汎用ビューの、デフォルトメソッドの豆知識 -- #

def post(self, request): # 汎用ビューメソッドで、requestを引数にとるのは、get,postくらい。
    return HttpResponse('hello')

def get_queryset(self): # get_context_dataとかは、多分、引数、selfだけで、足りると思う。
    return {context:'辞書型マスト'} # *args, **kwargs ってなんのために使うの？

def get_context_data(self, **kwargs): # get_context_dataをオーバーライドした中身。
    context = super().get_context_data() # ここの引数は、なくても、変わらん。
    print(context)
    # 出力結果
    # paginator
    # page_obj
    # is_paginated
    # object_list
    # commentdata_list
    # view   

def get(self, request, **kwargs):
    context = super().get(request)
    print(type(context))
    # 出力結果
    # <class 'django.template.response.TemplateResponse'>

def get(self, request, **kwargs): # オーバーライドを異なる、メソッドの中でやると、エラーがでる。
    context = super().get_context_data() # 'HomeListView' object has no attribute 'object_list'

