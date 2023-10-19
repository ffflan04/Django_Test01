# request.GET/POST について
# やっと、request.POST、値をとれました。
# 今回とれた値は、送信したフォームの、'user'の部分ですね。

# -- home.html -- #

<form action="" method="post">
    {% csrf_token %}
    {{test.as_p}}
    <button type="submit">送信</button>
</form>

# -- views.py -- #

def testform(request):
    if request.method == 'POST':
        print(request.POST['user'])
        return HttpResponse('返り値')