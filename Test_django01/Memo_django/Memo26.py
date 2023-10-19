# Djangoで画像をhtmlに表示
# フォームで送った、画像ファイルを、request.FILESで獲得する。

# -- templates -- #

{% for i in images %}
<p>{{i.kyara}}</p>
<p>{{i.image.url}}</p> <!--すげぇ！データベースに、画像が保存されてるフォルダのurlが格納されてる！！！-->
<img src="{{i.image.url}}" alt="">
{% endfor %}

<p>{{obj_01.image.url}}</p> # 画像が保存されているpathがわかります。
<p><img src="/media/rubii_pkX8jX7.png" alt=""></p> # データベースを介さなくても、画像が保存されているpathをそのまま打てば、表示させることが可能。

# -- views.py -- #

class ImageDealingView(FormView): # フォームで送った、画像ファイルを、request.FILESで受け取れたぞぉ！
    template_name = 'testapp/home.html'
    form_class = ImageSendForm
    success_url = 'home'

    def form_valid(self, form): # form_valid関数はレコードが保存される直前で呼ばれる関数だ。
        print(self.request.FILES['image']) # --> murabito.jpg
        print(type(self.request.FILES['image'])) # --> <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>