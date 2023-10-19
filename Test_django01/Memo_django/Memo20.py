# クラスベースビューの中でprint関数を実行できたぞ。
# これが、ロジック解析の糸口になる。

# -- views.py -- #

class TestView(TemplateView): # テスト用のメソッドです。
    template_name = 'testapp/home.html'

    def get_context_data(self, **kwargs): # これは、独自のコンテキストを追加するメソッド
        context = super().get_context_data(**kwargs) # get_context_dataをオーバーライドしてくる。
        context['kioku'] = '記憶'
        return context
    
    def get(self, request, *args, **kwargs): # GETメソッド時に、実行される処理
        print(super().get_context_data()) # get_context_dataの返り値を、出力。
        return super().get(self, request, *args, **kwargs)
    # 処理結果 --> {'view': <testapp.views.TestView object at 0x102d03fb0>}