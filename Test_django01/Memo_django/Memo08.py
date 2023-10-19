# ListViewクラスの処理で、レコードの追加できたよ。

# ----- views.py ------- #

class TryListView(ListView): # テンプレートにデータベースをレンダーできます。
    template_name = 'testapp/sakuhin.html'
    sb = SecondBoard()
    sb.kyara = '名探偵コナン'
    sb.slugnum = 6
    sb.save()
    model = SecondBoard # ここで、モデルクラスをテンプレートにレンダー。