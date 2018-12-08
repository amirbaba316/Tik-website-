from django import forms
from .models import Problem
from django.core.exceptions import ValidationError

class ProblemForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(
    attrs={
    'style': 'border-color:SteelBlue; border-radius: 7px; border-width: thin;',
    }))
    description=forms.CharField(widget=forms.Textarea(
        attrs={
    'style': 'border-color:SteelBlue; border-radius: 7px; border-width: thin;',
        }))
    answer=forms.CharField(widget=forms.TextInput(
        attrs={
    'style': 'border-color:SteelBlue; border-radius: 7px; border-width: thin;',
        }))
    slug=forms.SlugField(widget=forms.TextInput(
        attrs={
    'style': 'border-color:SteelBlue; border-radius: 7px; border-width: thin;',
        }))
    difficulty =forms.CharField(widget=forms.TextInput(
        attrs={
    'style': 'border-color:SteelBlue; border-radius: 7px; border-width: thin;',
        }))

    class Meta:
        model=Problem
        fields='__all__'

    def clean_p_name(self):
        return self.cleaned_data['p_name'].lower()
    def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError('Slug cannot be "create".')
        return new_slug

class AnswerForm(forms.Form):
    answer=forms.CharField(widget=forms.TextInput(attrs={
'style': 'border-color:black; border-radius: 7px; border-width: thin; background-color: #E8F8F5  ;' ,
    }))

    answer.widget.attrs.update(size='15')
