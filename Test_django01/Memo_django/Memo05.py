# クラスベースビューを使ってみたよ
# TemplateViewクラス = 簡単にテンプレートファイルをレンダーできました。
# ListViewクラス = データベースのオブジェクトを取り出すことができたお。

# ----- urls.py ------- #
urlpatterns = [
    path('tryTV', views.Tryclassview.as_view())
    path('tryLV', views.TryListView.as_view())
]

# ------ views.py ------- #
class Tryclassview(TemplateView):
    template_name = 'testapp/sakuhin.html'

class TryListView(ListView):
    template_name = 'testapp/sakuhin.html'
    model = BulletinBoard