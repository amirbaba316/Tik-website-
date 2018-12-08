from django import forms
from .models import Discussion,Comments
from django.core.exceptions import ValidationError

class DiscussionForm(forms.ModelForm):
    class Meta:
        model=Discussion
        fields=['title','slug','argument']
class CommentsForm(forms.ModelForm):
  
    comment_text=forms.CharField(widget=forms.TextInput(attrs={
        'style': 'border-color:SteelBlue; border-radius: 7px; border-width: thin;',
        }))
    class Meta:
        model=Comments
        fields=['comment_text']
