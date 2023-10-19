# データベース、フィールド == None の条件分岐
# Noneは役にたたないので、True の分岐を使いましょう。

# -- views.py -- # 

obj = Self_Introduction.objects.filter(user='炭治郎')
if obj:
    print('何か入ってる。')