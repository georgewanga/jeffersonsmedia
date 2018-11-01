from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'username'
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'password'
        }))
        

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'username'
        }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Your email'
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'password'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Confirm password'
        }),label='Confirm password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('username is taken')
        return username


    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('email is taken')
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError('passwords must match.')
        return data


class AddItemForm(forms.Form):
    category = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Item Category'
        }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Item Name'
        }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'rows':'4',
        'placeholder':'Item Description'
        }))
    size = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Size'
        }))
    price = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Unit Price'
        }))
    bulk = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Minimum number to consider as bulk'
        }))
    image = forms.ImageField()

    def clean_bulk(self):
        bulk = self.cleaned_data.get('bulk')
        try:
            int(bulk)
        except ValueError:
            raise forms.ValidationError('bulk has to be a positive integer')
        return bulk