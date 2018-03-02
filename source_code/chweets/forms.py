from django import forms

from .models import Chweet


class ChweetModelForm(forms.ModelForm):

    class Meta:
        model = Chweet
        fields = ('content',)

