# save()メソッドと、モデルのインスタンスの解説

from .forms import UserForm
from .models import User
from .forms import UserModelForm

def form(request):
    if request.method == 'POST':
        form = UserModelForm(request.POST) # request.POST(フォーム送信内容)をセットした、forms.ModelFormクラスをインスタンス化
        if form.is_valid():
            user = form.save(commit=False) # データベースへの保存 + forms.ModelFormで指定されたモデル(ここではUser)のインスタンスを取得。
            bmi = user.weight / ((user.height /100) * (user.height / 100))
            user.bmi = bmi # user.bmi = Userモデルの、'bmi'フィールド に、値をセット。
            user.save() # 上記で変更したUserモデルクラスを、データベースに保存、反映。