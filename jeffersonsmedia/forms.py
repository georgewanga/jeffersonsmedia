from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class AddItemForm(forms.Form):    
    category = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Item Category'
        }))
    title = forms.CharField(widget=forms.TextInput(attrs={
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
