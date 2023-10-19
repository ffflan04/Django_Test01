# slugについて
# urlとslugを関連付けて、URLマッピングを動的にします。
# 指定のURLで、slugに対応したレコードを取得できます。

# ---- urls.py ------- #

urlpatterns = [
    path('<slug:slug>/', views.test_get) # slug型で、"slug"という変数名で定義します。
]

# ---- views.py ------- #

def test_get(request, slug): # urls.pyでセットされたslugを引数として取得します。
    motti = BulletinBoard.objects.get(slug=slug)
    context = {'checkGet': motti}
    return render(request, 'testapp/sakuhin.html', context)

# -- テンプレートファイル -- #

{{checkGet}} # slugに対応したレコードを取得できます。