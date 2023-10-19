# フォームに初期値を設定できた。
# フォームのフィールドを隠した。

# -- forms.py -- #

class TestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): # フォームのフィールドを隠すメソッドです。
        super().__init__(*args, **kwargs) 
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['email'].widget = forms.HiddenInput()
    class Meta:
        model = CommentData
        fields = ['user', 'email', 'body']

# -- views.py -- #

def testform(request): # request.userを代入する方法。
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/testapp/')
    if request.method == 'GET':
        ctx = {}
        ctx['user'] = request.user # user: <ユーザー名> の辞書をセット
        ctx['email'] = request.user.email # email: <メールアドレス> の辞書をセット
        form = TestForm(ctx) # 引数の辞書を基に、forms.ModelForm をインスタンス化。
        context = {'test': form}
        return render(request, 'testapp/home.html', context)

def ttestform(request): # instanceを使って、フォームの初期値をセットする。
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        obj = User.objects.get(username=request.user)
        print(obj.username)
        form = TestForm(instance=obj) 
        context = {'test01': form}
        return render(request, 'testapp/home.html', context)
# instanceは、models.pyのモデルの枠組みを提供します。
# instanceのモデルの枠組みの中で、foreignKeyのフィールドに初期値をいれることはできなかった。