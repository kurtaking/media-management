from django import forms
from .models import Vinyl


class AddVinylForm(forms.ModelForm):
    class Meta:
        model = Vinyl
        fields = ['artist', 'title', 'year', 'genre', 'label', 'format_size', 'isbn']
        widgets = {
            'artist': forms.TextInput(
                attrs={'id': 'artist', 'class': 'form-control'}
            ),
            'title': forms.TextInput(
                attrs={'id': 'title', 'class': 'form-control'}
            ),
            'year': forms.TextInput(
                attrs={'id': 'year', 'class': 'form-control'}
            ),
            'genre': forms.TextInput(
                attrs={'id': 'genre', 'class': 'form-control'}
            ),
            'label': forms.TextInput(
                attrs={'id': 'label', 'class': 'form-control'}
            ),
            'format_size': forms.TextInput(
                attrs={'id': 'format_size', 'class': 'form-control'}
            ),
            'isbn': forms.TextInput(
                attrs={'id': 'isbn', 'class': 'form-control'}
            ),
        }