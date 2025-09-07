


from django import forms
from .models import Snippet

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['snippet_type', 'title', 'content', 'language', 'tags', 'is_favorite']
        widgets = {
            'snippet_type': forms.Select(attrs={
                'class': 'w-full p-2 rounded-md bg-gray-900 text-white'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded-md bg-gray-900 text-white',
                'placeholder': 'Enter snippet title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full p-2 rounded-md bg-gray-900 text-white',
                'placeholder': 'Write your code, note, or idea here...'
            }),
            'language': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded-md bg-gray-900 text-white',
                'placeholder': 'Language (if code)'
            }),
            'tags': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded-md bg-gray-900 text-white',
                'placeholder': 'Add tags separated by commas'
            }),
            'is_favorite': forms.CheckboxInput(attrs={
                'class': 'mr-2'
            }),
        }