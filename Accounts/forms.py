from django.contrib.auth.models import User
from .models import UserProfile
from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import BadHeaderError,mail_managers



class ContactForm(forms.Form):
    FEEDBACK ='F'
    CORRECTION ='C'
    SUPPORT ='S'
    REASON_CHOICES =(
      (FEEDBACK,'Feedback'),
      (CORRECTION,'Correction'),
      (SUPPORT,'Support'),
    )
    reason=forms.ChoiceField(choices=REASON_CHOICES,initial=FEEDBACK)
    email = forms.EmailField(initial='abc@domain.com')
    text=forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        return self.cleaned_data['email'].lower()

    def send_mail(self):
        reason = self.cleaned_data.get('reason')
        reason_dict = dict(self.REASON_CHOICES)
        full_reason = reason_dict.get(reason)
        email = self.cleaned_data.get('email')
        text = self.cleaned_data.get('text')
        body = 'Message From: {}\n\n{}\n'.format(email, text)

        try:
            # shortcut for send_mail
            mail_managers(full_reason, body)
        except BadHeaderError:
            self.add_error(
                None,
                ValidationError(
                    'Could Not Send Email.\n'
                    'Extra Headers not allowed '
                    'in email body.',
                    code='badheader'))
            return False
        else:
            return True


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=['first_name','last_name','email','username','password',]

class UserProfileForm(forms.ModelForm):
    class Meta():
        model=UserProfile
        fields=['profile_pic','bio']

class ProfileUpdate(forms.ModelForm):
    class Meta():
        model=User
        fields=['first_name','last_name','email',]

class PasswordUpdate(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['password']