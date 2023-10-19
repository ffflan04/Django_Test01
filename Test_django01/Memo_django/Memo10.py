# user.nameに対応した、レコードを取得するために、
# ユーザーネームをslug型で取得して、user=slug の条件式に加えた。

# ---- 静的.html ---- #

 <td><a href="http://127.0.0.1:8000/testapp/delete/{{person.user}}">削除</a></td>

# ---- urls.py ----- #

urlpatterns = [
    path('delete/<slug:user>', views.member_delete)
]


# ---- views.py ----- #

def member_delete(request, slug): # 会員情報ページで指定の、objectを削除するメソッド
    person = BulletinBoard.objects.get(user=slug)
    person.delete()
    return redirect('http://127.0.0.1:8000/testapp/memberlist')



