# デバッグに使える知識

# サーバー起動した状態で、
# httpリクエストを飛ばしたら、コンソールに、
# [19/Jul/2023 10:13:47] "GET /testapp/tryLV HTTP/1.1" 200 283
# こういう表記がでてきます。

# これはListViewクラスのget_context_dataのcontext変数の中身をprintします。
# views.pyの中とかに、print()メソッドを実装して、
# 実行させると、コンソールに、
# {
# 'paginator': None, 'page_obj': None, 
# 'is_paginated': False, 
# 'object_list': <QuerySet [<BulletinBoard: BulletinBoard object (1)>, <BulletinBoard: BulletinBoard object (2)>]>,
# 'bulletinboard_list': <QuerySet [<BulletinBoard: BulletinBoard object (1)>, <BulletinBoard: BulletinBoard object (2)>]>, 
# 'view': <testapp.views.TryListView object at 0x102ca6600>
# }
# っていう記述がでるから是非確認してみて。