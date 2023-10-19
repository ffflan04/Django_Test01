# CBV(クラスベースビュー)の、
# get_context_dataメソッドで、
# テンプレートに(現在の時刻の)値を渡してみた。

# ---- views.py ------ #

from django.utils import timezone

class Tryclassview(TemplateView):
    template_name = 'testapp/sakuhin.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

# ----- テンプレートファイル ------ #

    {{now}}