# データベースからフィールドをviews.pyでとってきて、
# render関数でテンプレートにfor文を使って埋め込んで、返した。

# --views.py--#

from django.shortcuts import render
from .models import BulletinBoard

def document01(request):
    person = BulletinBoard.objects.all()
    context = {'features': person}
    return render(request, 'testapp/sakuhin.html', context)

# ------ #

# ----sakuhin.html----#

<body>
    <h1>ここから物語が始まります。</h1>
    {% for feature in features %}
    {{feature}}
    {% endfor %}
</body>

# ------- #

