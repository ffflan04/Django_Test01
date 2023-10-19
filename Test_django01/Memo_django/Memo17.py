# forms.Formを使うと、フィールドをforms.pyで定義できるらしい。
# 実際、forms.ModelForm、で事足りるらしい。

# myapp/forms.py
from django import forms


class BookForm(forms.Form):
    title = forms.CharField(
        label='本のタイトル',
        max_length=100,
        required=True,
        help_text='必須',
    )
    description = forms.CharField(
        label='本の説明文',
        widget=forms.Textarea,
        required=False,
        help_text='*任意',
    )