from django import forms
from . import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'email', 'body']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی'}),
            'email': forms.EmailInput(attrs={'placeholder': 'آدرس ایمیل'}),
            'body': forms.Textarea(attrs={
                'placeholder': 'اینجا بنویس ...',
                'cols': 40,
                'rows': 5,
            }),
        }
