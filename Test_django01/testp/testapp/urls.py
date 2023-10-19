from . import views
from django.urls import path

# 知らねーけど、'testform'っていうurlだと、Page not found になる。
# 'other_profile/<str:other>/' のurl設定するときは、末尾に'/'入れないと、ダメね。

urlpatterns = [
    path('check', views.testmethod), # テストメソッド
    path('check01', views.ForeignKeyTest.as_view()), # テストメソッド
    path('check02', views.TryListView.as_view()), # テストメソッド
    path('check03', views.ImageDealingView.as_view()), # テストメソッド
    path('', views.HomeListView.as_view(), name='home'), # ホーム画面
    path('mypage', views.myprofile.as_view(), name='mypage'), # マイプロフィール画面を表示
    path('<int:pk>/delete', views.MemberDeleteView.as_view(), name='delete'), # ツイート削除のメソッド
    path('tweet_set', views.tweet_set), # ツイート画面の表示、送信
    path('signup', views.MySignupView.as_view(), name='signup'), # 会員登録ページのパス
    path('login', views.MyLoginView.as_view(), name='login'), # ログインページ表示
    path('logout', views.MyLogoutView.as_view(), name='logout'), # ログアウトページ表示
    path('other', views.MyOtherView.as_view(), name='other'), # 他ユーザー情報、表示
    path('other_profile/<str:other>/', views.OtherProfile.as_view()), # 他ユーザーページへの表示。
    path('directmessage/<str:touser>/', views.DirectMessageView.as_view()), # 個チャのメソッド
    path('change_icon', views.EditProfileView.as_view()) # 死んでるメソッド
]