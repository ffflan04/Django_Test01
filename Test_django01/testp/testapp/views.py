from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from .models import CommentData, Self_Introduction, LikedBool, DM_strage, Image_strage, FF_bool, FF_total
from http.client import HTTPResponse
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, FormView
from django.utils import timezone
from .forms import TweetList, SignupForm, LoginForm, IntroductionModelForm, DirectMessageModelForm, ImageSendForm, ChangeIconForm, ForrowedForm, TotalFollowInit
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeListView(LoginRequiredMixin, ListView): # トップページになります。
    template_name = 'testapp/home.html'
    model = CommentData

    def post(self, request):
        if request.GET.get('like') is not None: # クエリストリングが、いいね！のKeyだったら。
            liked_user = int(request.GET.get('like')) # pk のvalueに対応させるために、int型に変換。
            CDobj = CommentData.objects.get(pk=liked_user) # いいね対象のツイートをインスタンス化
            if LikedBool.objects.filter(byuser=self.request.user, tweet=liked_user).exists() == False: # 一人のユーザーにつき、一つのいいねしか押せない機能を実装するため、
                LikedBool.objects.create(byuser=self.request.user, tweet=liked_user, like_bool=False) # LikedBoolデータベースを、判定子として、 動的に、レコードを作成します。
            LBobj = LikedBool.objects.get(byuser=self.request.user, tweet=liked_user) # 強制的に作られた、ユーザー毎の、ツイートのいいね履歴データベースをインスタンス化。
            if LBobj.like_bool == False: # いいねボタンが押されたとき、いいねボタンがfalseだったら、
                LBobj.like_bool = True # いいねボタンをTrueにして、
                CDobj.like += 1 # いいね数を追加する。
            else: # いいねボタンが押されたとき、いいねボタンがTrueだったら、
                LBobj.like_bool = False # いいねボタンをFalseにして、
                CDobj.like = CDobj.like - 1 # いいね数を一つ減らします。
            CDobj.save() # いいね数を保存します。
            LBobj.save() # いいね判定子を保存します。
            return redirect('home') # 元いたサイトにリダイレクト。
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 必ず、home に着地させて、初期値をセットさせる。
        # 初期値をセットする関連の処理。
        if not Self_Introduction.objects.filter(user=self.request.user):
            ctx = {}
            ctx['user'] = self.request.user
            ctx['body'] = '自己紹介してね！'
            IDform = IntroductionModelForm(ctx) # 自己紹介モデルに初期値をセットしたかったのです。
            IDform.save() # create, save()では、動的な値->変数をセットできなかったので、モデルフォームで無理やり、初期値をセットしました。
        if not FF_total.objects.filter(user=self.request.user):
            ctx_01 = {}
            ctx_01['user'] = self.request.user
            FFtotal = TotalFollowInit(ctx_01) # フォロー数管理モデルに初期値をセットしたかったのです。
            FFtotal.save()

        # あーそういうことか、新しいユーザーにすると、LikedBoolが空だから、塗り替えられないのか。
        # じゃあ、頭で、コメントデータベースのboolを初期化すればいいんじゃね。
        CDobj = CommentData.objects.all()
        for cdobj in CDobj:
            cdobj.good_bool = False
            cdobj.save()
        
        if LikedBool.objects.filter(byuser=self.request.user): # いいねボタンを一度でも押したことがあるユーザーは..
            LBobj = LikedBool.objects.filter(byuser=self.request.user, like_bool=True) # この一連の処理は、一つのツイートに対して、一人のユーザーにつき、１いいね判定を実装したかったため、
            for lbobj in LBobj: # 予め、ユーザ＋いいね対象ツイートで選別されて登録された、別データベースに保存されている、ツイート番号＋いいね判定子のデータを、ツイート番号のフィルターを使って、全て、別データベースに反映させた。
                obj = CommentData.objects.get(pk=lbobj.tweet)
                obj.good_bool = True
                obj.save()
            LBobj = LikedBool.objects.filter(byuser=self.request.user, like_bool=False)
            for lbobj in LBobj:
                obj = CommentData.objects.get(pk=lbobj.tweet)
                obj.good_bool = False
                obj.save()
        
        SIobj = Self_Introduction.objects.get(user=self.request.user) # 
        context['profile_topuga'] = SIobj # ホーム画面にアイコンを表示させたいので、インスタンスを渡します。

        IconIsTrue = Self_Introduction.objects.exclude(image=None) # マイページモデルのimageフィールドを、コメントモデルに全て移植しまーす。
        for IconUser in IconIsTrue: # アイコンを設定してるユーザーを、forで回す。
            UserComment = CommentData.objects.filter(user=IconUser.user) # アイコンを設定してるユーザそれぞれの、持つコメントデータのクエリセットを抽出。
            for comment in UserComment: # 特定のユーザーの持つコメントを一つ一つ抽出して、imageフィールドを代入します。
                comment.user_icon = IconUser.image
                comment.save()
        
        obj_01 = FF_total.objects.get(user=self.request.user)
        context['ff_num'] = obj_01 # ログイン中のユーザーのフォロワー数を表示します。

        
        if self.request.GET.get('list') == 'follow': # フォロー中のユーザーを表示したいというリクエスト
            obj_02 = FF_bool.objects.filter(userby=self.request.user, follow_switch=True)
            if obj_02: # 誰もフォローしていない時の、分岐を作ります。
                SI_init_obj = Self_Introduction.objects.filter(user='空の戦士') # レコードを結合させる土台を作ってます。
                for ff_obj in obj_02: # フォロー中のユーザー名をループで抽出。
                    SI_obj = Self_Introduction.objects.filter(user=ff_obj.be_followed) # フォロー中のユーザーの、自己紹介モデルのインスタンスを取得。
                    SI_init_obj = SI_init_obj | SI_obj # 抽出した、クエリセットを一つずつ、結合していく。
                context['follow_user_info'] = SI_init_obj
            else:
                context['none_ff'] = '誰もフォローしてねぇよ。'
        elif self.request.GET.get('list') == 'follower': # フォロワーを表示したいというリクエスト
            obj_02 = FF_bool.objects.filter(be_followed=self.request.user, follow_switch=True) # 自分をフォローしてるユーザーのインスタンスを取得
            if obj_02: # 誰もフォローしていない時の、分岐を作ります。
                SI_init_obj = Self_Introduction.objects.filter(user='空の戦士') # レコードを結合させる土台を作ってます。
                for ff_obj in obj_02: # フォロー中のユーザー名をループで抽出。
                    SI_obj = Self_Introduction.objects.filter(user=ff_obj.userby) # フォロー中のユーザーの、自己紹介モデルのインスタンスを取得。
                    SI_init_obj = SI_init_obj | SI_obj # 抽出した、クエリセットを一つずつ、結合していく。
                context['follow_user_info'] = SI_init_obj
            else:
                context['none_ff'] = '誰からもフォローされてねぇよ。'

        return context# ツイートに対する、ユーザーのいいね判定子を格納した、CommentDataモデルを、For文で回してもらうために、コンテキストで返す。


class myprofile(LoginRequiredMixin, ListView): # mypageを表示するためのメソッド
    template_name = 'testapp/mypage.html'
    
    def get_queryset(self): # ログインユーザーのクエリセットを取得
        qs = User.objects.none()
        if self.request.user.is_authenticated: # ログイン状態かの判定です。
            qs = CommentData.objects.filter(user=self.request.user)
        return qs #  Querysetを返すだけで、テンプレートにレンダーしてくれる凄いメソッド。
    
    def get_context_data(self, **kwargs): # 自己紹介用フィールドを、フォームで実装する。
        context = super().get_context_data(**kwargs) # 文章の編集をスムーズにするためにフォームを採用しました。
        ctx = {} # getとfilterの使い分けは、一つのレコードか、複数のレコードか？です。
        obj = Self_Introduction.objects.get(user=self.request.user) # 予め登録してある自己紹介モデルのオブジェクトを取得。
        context['topuga'] = obj # マイページのプロフィール画像のデータベース情報も渡したいので、ちゃっかり、失礼します。
        ctx['user'] = self.request.user # 自己紹介フォームに初期値を入れています。
        ctx['body'] = obj.body 
        itd = IntroductionModelForm(ctx) # 初期値をセットしたModelFormクラスをインスタンス化。
        context['introduction'] = itd # テンプレートに渡すために、contextにセット。
        if self.request.GET.get('q') == 'update': # 自己紹介フォーム更新の、クエリストリングの判定ですね。
            context['DoneUpdate'] = 'ーーー＞ 変更を保存したよ〜！' # 変更したことをUIに表示したほうがいいですよね。
        
        LBobj = LikedBool.objects.filter(byuser=self.request.user, like_bool=True) # 自分がいいねしたツイートを表示する処理
        for lbobj in LBobj: # 自分がいいねしたツイートのみを、CommentDataのいいね判定子に、反映させることで、実現。
            CDobj = CommentData.objects.get(pk=lbobj.tweet)
            CDobj.good_bool = True
            CDobj.save() # この時点で、自分がいいねした投稿に、Trueが反映されます。
        CD_result_True = CommentData.objects.filter(good_bool=True)
        context['tweet_data'] = CD_result_True # いいね判定子の反映されたCommentDataのレコードを、コンテキストにセット

        form = ChangeIconForm() # マイページアイコン更新専用フォームをインスタンス化
        context['choice_icon'] = form # テンプレートに渡します。

        return context # コンテキストを返します。
    
    def post(self, request):
        if request.GET['change'] == 'icon': # アイコン更新フォーム -> クエリストリングで更新内容を分岐させてる。
            SIobj = Self_Introduction.objects.get(user=self.request.user)
            SIobj.image = request.FILES['image'] # データベースのフィールドに直接、値を入れることで更新。
            SIobj.save() # 更新内容を保存
            messages.success(self.request, '良かったな。変更できたぞ。')
            return redirect('http://127.0.0.1:8000/testapp/mypage')
        elif request.GET['change'] == 'body': # 自己紹介文更新のフォーム
            obj = Self_Introduction.objects.get(user=self.request.user) # データベースのレコードを単一(get)で、取得。
            obj.user = request.POST['user'] # データベースのフィールドに直接、値を入れることで更新。
            obj.body = request.POST['body'] 
            obj.save() # 更新内容を保存
            return redirect('http://127.0.0.1:8000/testapp/mypage?q=update') # クエリストリングを付与して、リダイレクト先に、自己紹介フォームを更新したことを伝える。

class MemberDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'testapp/delete_confirm.html' # 削除確認画面のテンプレートファイル
    model = CommentData # 取り出す先のモデル <- <int:pk>で指定したpkのモデルが削除対象です。
    success_url = reverse_lazy('mypage') # 削除完了した後に遷移するURLを指定する。

def tweet_set(request): # ツイートの画面遷移、ツイートデータの保存、のメソッド
    if request.method == 'POST': # ツイートデータの保存処理
        form = TweetList(request.POST)
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/testapp/')
    if request.method == 'GET': # 初期値の入ったツイート画面
        ctx = {}
        c = CommentData.objects.all() # 既存のタイムラインのデータ
        ctx['user'] = request.user # user: <ユーザー名> の辞書をセット
        ctx['email'] = request.user.email # email: <メールアドレス> の辞書をセット
        push = TweetList(ctx) # 引数の辞書を基に、forms.ModelForm をインスタンス化。
        context = {'tweet': push, 'Tweets': c}
        return render(request, 'testapp/home_derive/tweet.html', context)

class OtherProfile(ListView): # 他のユーザーのプロフィールを表示する。
    template_name = 'testapp/other_page.html'
    model = CommentData

    def post(self, request, other):
        if request.GET.get('count') == 'ff': # クエリストリングで条件分岐
            obj_bool = FF_bool.objects.get(userby=self.request.user, be_followed=other) # 
            obj_self = FF_total.objects.get(user=self.request.user)
            obj_one = FF_total.objects.get(user=other)
            if obj_bool.follow_switch: # もし、もう、そのユーザーをフォローしていたら。
                obj_bool.follow_switch = False # フォロー判定を、オフにして。
                obj_self.followed = obj_self.followed - 1 # 自分のフォロー数を１減らす。
                obj_one.follower = obj_one.follower - 1 # 相手のフォロワー数を１減らす。
                obj_bool.save()
                obj_self.save()
                obj_one.save()
                return redirect(f'http://127.0.0.1:8000/testapp/other_profile/{other}') # 元いたページにリダイレクト
            else: # まだ、そのユーザーをフォローしていなかったら。
                obj_bool.follow_switch = True # フォロー判定を、オンにして。
                obj_self.followed += 1 # ユーザーのフォロー数を１増やす
                obj_one.follower += 1 # ユーザーのフォロワー数を１増やす
                obj_bool.save()
                obj_self.save()
                obj_one.save()
                return redirect(f'http://127.0.0.1:8000/testapp/other_profile/{other}') # 元いたページにリダイレクト
        else:
            HttpResponse('想定外のpostきたぁ。')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Self_Introduction.objects.get(user=self.kwargs['other']) # URLパラメータを使って、自己紹介データベースからデータを取得してます。
        context['introduction'] = obj.body # 自己紹介文をコンテキストにセット
        context['the_user'] = obj.user # プロフィールのユーザー名をセット
        context['mypage_icon'] = obj # マイページアイコンをセット
        CDobj = CommentData.objects.filter(user=self.kwargs['other']) # 特定のユーザーのツイートを抽出。
        context['user_tweet'] = CDobj # for文で回すので、このまま渡します。

        # 自分が相手に対する、フォロー判定を、テンプレートに送ってくれ！
        # マイページ訪れた時点で、FF_boolのレコード作っちゃいますか。
        # フォロー数のデータベースも、コンテキストに送ってください。
        obj_bool = FF_bool.objects.filter(userby=self.request.user, be_followed=self.kwargs.get('other')) 
        if not obj_bool: # FF_boolデータベースに、すでに、情報が登録されていなかったら、
            ctx_01 = {}
            ctx_01['userby'] = self.request.user
            ctx_01['be_followed'] = self.kwargs.get('other')
            ff_form = ForrowedForm(ctx_01)
            ff_form.save() # ユーザーページに訪れた時点で、FF_boolデータベースレコードの初期値を入れるようにしました。
        uni_obj = FF_bool.objects.get(userby=self.request.user, be_followed=self.kwargs.get('other'))
        num = FF_total.objects.get(user=self.kwargs.get('other')) # ユーザーのフォロー人数を管理するモデルを渡します。
        context['follow_bool'] = uni_obj # if文でレコードがないときの処理を実装したので、確実にレコードが存在するはずです。
        context['ff_num'] = num

        return context

class DirectMessageView(ListView): # 個チャのデータベースあたりをいじるクラス。
    template_name = 'testapp/DMroom.html'
    model = DM_strage

    def post(self, request, touser):
        fm = DirectMessageModelForm(request.POST) # 送信されたフォームを保存する処理
        if fm.is_valid():
            fm.save() # これで、データベースに保存
        return redirect(f'http://127.0.0.1:8000/testapp/directmessage/{touser}') # fストリング使えて良かったぁー！

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        fctx = {} # メッセージを送信するフォームを作成してます。
        fctx['send_user'] = self.request.user # メッセージ以外の入力項目を予めセット
        fctx['to_user'] = self.kwargs.get('touser')
        message_form = DirectMessageModelForm(fctx)
        context['Message_Form'] = message_form

        # データベースからメッセージを抽出する処理
        my_log = DM_strage.objects.filter(send_user=self.request.user, to_user=self.kwargs.get('touser'))
        one_log = DM_strage.objects.filter(send_user=self.kwargs.get('touser'), to_user=self.request.user)
        m_log = my_log | one_log # 複数のクエリセットを結合する。
        context['dm_log'] = m_log
        context['myside'] = self.request.user # テンプレートの。if文で使いたいらしいので渡しときました。
        context['oneside'] = self.kwargs.get('touser')
        self_icon = Self_Introduction.objects.get(user=self.request.user)
        one_icon = Self_Introduction.objects.get(user=self.kwargs.get('touser'))
        context['icon_self'] = self_icon
        context['icon_one'] = one_icon # マイページアイコンをテンプレートで渡します。 

        return context 

class ImageDealingView(FormView): # テストメソッド
    template_name = 'testapp/home.html'
    form_class = ImageSendForm
    success_url = 'http://127.0.0.1:8000/testapp/'

    def post(self, request, animal):
        chc = animal
        print(chc)
        print(type(chc))
        return HttpResponse('hello')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        obj = Self_Introduction.objects.all()
        if obj:
            print('objの中身は入ってます')
        if Self_Introduction.objects.all():
            print('このままでもいいんか？')
        return context

class EditProfileView(FormView): # マイページのトプ画を変更するためのメソッド
    template_name = 'testapp/home.html'
    form_class = ChangeIconForm
    success_url = 'http://127.0.0.1:8000/testapp/mypage'

    def post(self, request):
        obj = self.request.GET['q']
        print(obj)
        print(type(obj))
        return HttpResponse('hello')













# Userモデルでログイン機能を実装すると、
# contextをテンプレートに渡さなくても、
# {{user.username}} のように、Userモデルのフィールドを操れる。

class MySignupView(CreateView): # Createviewはレコードの新規作成、保存を担当します。
    template_name = 'testapp/user_register.html'
    form_class = SignupForm # UserCreationFormクラスはcontextのkeyを'form'に自動で設定します。
    success_url = 'http://127.0.0.1:8000/testapp/' # なぜか、includeした先からのpaht名でいいらしい..

    def form_valid(self, form): # 送信されてきたformが有効ならば、ログインするメソッド。
        result = super().form_valid(form) # Userモデルにインスタンス(受け取ったform)を保存
        user = self.object # 'self.object'は、form_validメソッドに保存されたモデルのインスタンスを取得
        login(self.request, user) # (受け取ったform)情報で、login関数を実行。
        return result

class MyLoginView(LoginView): # Django標準の、LoginViewはログインを担当するクラスです。
    template_name = 'testapp/user_login.html'
    form_class = LoginForm # なに!? これだけでいいだとぉ？？
    # AuthenticationFormクラスも、contextのkeyが'form'に自動で設定されている。
    # パスワード：parukia01

class MyLogoutView(LogoutView): # Django標準の、LogoutViewはログアウトを担当するクラスです。
    template_name = 'testapp/user_logout.html'

class MyOtherView(LoginRequiredMixin, TemplateView): # 他ユーザー情報の表示するクラス
    template_name = 'testapp/other.html'

    def get_context_data(self, **kwargs): # コンテキストを設定するためのメソッド
        context = super().get_context_data(**kwargs) # ここまでがテンプレ
        context['other'] = User.objects.exclude(username=self.request.user.username)
        # exclude関数で、User.objects(Userモデルの中身)を選別して、コンテキストに代入。
        return context

def testmethod(request):
    return render(request, 'testapp/other_page.html')

class ForeignKeyTest(FormView):
    template_name = 'testapp/home.html'


class TryListView(ListView):
    template_name = 'testapp/other.html'
    model = Self_Introduction

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = DirectMessageModelForm()
        print(form)
        return context
    
    def post(self, request):
        liked_user = int(request.GET['q'])
        if LikedBool.objects.filter(tweet=liked_user) == None: # いいねした投稿が存在しなかったら。
            LikedBool.objects.create(byuser=self.request.user, tweet=liked_user, like_bool=False) # いいねした投稿をデータベースに保存
            LBobj = LikedBool.objects.get(tweet=liked_user) # 多分エラーここ
        return HttpResponse('hi')











