# モデルのインスンス化は、for文の外では、適応されない気がする。

for lbobj in LBobj: 
    CDobj = CommentData.objects.get(pk=lbobj.tweet)
    CDobj['good_bool'] = True
    CDobj.save() 





