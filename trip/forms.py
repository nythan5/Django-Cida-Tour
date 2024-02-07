from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        labels = {'title': 'Título'}
        help_texts = {'title': 'Insira o título para a nova categoria.'}
        widgets = {'title': forms.TextInput(
            attrs={'placeholder': 'Ex.: Econômica | All-incluse...', 'class': 'input text-input'})}
