from django.forms import ModelForm, TextInput, Textarea, NumberInput
from .models import Soft


class SoftForm(ModelForm):
    class Meta:
        model = Soft
        fields = ['title', 'author', 'text', 'published', 'count']
        witgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву'


            }),
            'author': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть автора'

            }),
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть опис'

            }),
            'published': TextInput(attrs={
                'class': 'col-xs-4',
                'id': 'ex1',
                'placeholder': 'Введіть рік видання'
            }),
            'count': NumberInput(attrs={
                'class': 'col-xs-2',
                'id': 'ex2',
                'placeholder': 'Введіть кількість книг'
            }),
        }