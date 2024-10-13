from django import forms
from .models import Profile,Blog,Comment,User


class BlogForm(forms.ModelForm):
    title = forms.CharField(label='Blog Title', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter The Blog Title'
    }))
    content = forms.CharField(label='Blog Content', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Blog Content'
    }))
    class Meta:
        model = Blog
        fields ='__all__'