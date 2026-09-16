from django import forms
from . import models


class MessageForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Your subject',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your email',
            }),
            'text': forms.Textarea(attrs={
                'placeholder': 'Your message',
            }),
        }
