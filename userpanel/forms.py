from django import forms
from adminpanel.models import Profile,Blog,Comment,User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(label='Profile Image', widget=forms.ClearableFileInput(attrs={
        'class': 'form-control',
        }))
    id_proof = forms.ImageField(label='id_proof', widget=forms.ClearableFileInput(attrs={
        'class': 'form-control',
        }))
    profile_description = forms.CharField(label='Profile Description', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Profile Description'
    }))
    phone = forms.CharField(label='Phone',max_length=13, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Enter phone number'
    }))
    class Meta:
        model = Profile
        fields =['profile_image','id_proof','profile_description','phone']


class BlogForm(forms.ModelForm):
    title = forms.CharField(label='Blog Title', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter The Blog Title'
    }))
    content = forms.CharField(label='Blog Content', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Blog Content'
    }))
    blog_image = forms.ImageField(label='Blog Image', widget=forms.ClearableFileInput(attrs={
        'class': 'form-control',
    }))
    status = forms.ChoiceField(label='Status', choices=[
        ('draft', 'Draft'),
        ('published', 'Published')
    ], widget=forms.Select(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = Blog
        fields = ['title','content','blog_image','status']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='Comment', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Comment'
    }))
    class Meta:
        model = Comment
        fields = ['comment']


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Name'
    }))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Name'
    }))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Username'
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your email address'
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your password'
    }))
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Re-enter Your password'
    }))
    class Meta:
        model = User
        fields =['first_name','last_name','username','email','password1','password2']


class LoginForm(forms.Form):
    username = forms.CharField(label = 'Usename',
                               max_length = 100,
                               required = True,
                               widget = forms.TextInput(attrs={
        'class':'form-control','placeholder':'Enter Your Username'
    }))
    password = forms.CharField(label = 'Password',
                               max_length = 100,
                               required = True,
                               widget = forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Password'
    })) 


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your old password'
        })
    )
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your new password'
        })
    )
    new_password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your new password'
        })
    )

    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']
