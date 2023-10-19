# DeleteViewを使ってみた。

# -- urls.py -- #

path('<int:pk>/delete', views.MemberDeleteView.as_view(), name='delete'), # ツイート削除のメソッド

# -- views.py -- #

class MemberDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'testapp/delete_confirm.html' # 削除確認画面のテンプレートファイル
    model = CommentData # 取り出す先のモデル <- <int:pk>で指定したpkのモデルが削除対象です。
    success_url = reverse_lazy('mypage') # 削除完了した後に遷移するURLを指定する。

# -- テンプレートファイルURL設置 -- #

<p><a href="http://127.0.0.1:8000/testapp/{{object.pk}}/delete">ツイートを削除する</a></p>

# - テンプレートファイル確認画面 - #

    <form method="post">
        {% csrf_token %}
        <p>データ "{{ object }}" を本当に削除しますか?</p>
        <input type="submit" value="確定">
    </form>




