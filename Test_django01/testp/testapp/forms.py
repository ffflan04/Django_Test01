from django import forms
from .models import CommentData, Self_Introduction, DM_strage, Image_strage, FF_bool, FF_total
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class TweetList(forms.ModelForm): # コメント投稿用のフォーム
    class Meta:
        model = CommentData
        fields = {'user', 'email', 'body'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.fields['user'].widget = forms.HiddenInput() # フォームの入力項目を隠しています。
        self.fields['email'].widget = forms.HiddenInput()

class IntroductionModelForm(forms.ModelForm): # 自己紹介用のフォーム
    class Meta:
        model = Self_Introduction
        fields = {'user', 'body'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput() # フォームの入力項目を隠しています。

class DirectMessageModelForm(forms.ModelForm): # チャットを送るためのフォームです。
    class Meta:
        model = DM_strage
        fields = {'send_user', 'body', 'to_user'}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['send_user'].widget = forms.HiddenInput()
        self.fields['to_user'].widget = forms.HiddenInput() # メッセージフォームの入力項目を隠しています。

class SignupForm(UserCreationForm): # ユーザー登録用のデータベースとformの関連付け。
    class Meta:
        model = User # djangoで標準で用意されているモデルを使用。
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    # AuthenticationFormクラスを使えば、簡単にユーザ名とパスワードで認証する画面フォームを作成できます。
    pass

class ImageSendForm(forms.ModelForm): # テスト用
    class Meta:
        model = Image_strage
        fields = '__all__'

class ChangeIconForm(forms.ModelForm): # アイコンを変えるためのフォーム
    class Meta:
        model = Self_Introduction
        fields = ['image']

class ForrowedForm(forms.ModelForm): # フォロー情報の追加、フォロー判定の役割を担うフォーム
    class Meta:
        model = FF_bool
        fields = ['userby', 'be_followed']

class TotalFollowInit(forms.ModelForm): # フォロー数を管理するモデルの初期値をセットするためのフォーム
    class Meta:
        model = FF_total
        fields = ['user']






