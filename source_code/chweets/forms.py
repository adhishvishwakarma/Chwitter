from django import forms

from .models import Chweet


class ChweetModelForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'placeholder': "Your message",
                   "class": "form-control",
                   "maxlength": "140"}))

    class Meta:
        model = Chweet
        fields = ('content',)

