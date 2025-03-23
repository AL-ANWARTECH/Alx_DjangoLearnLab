from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post

# User Registration Form (Extends UserCreationForm)
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# User Profile Update Form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']


# Profile Picture Update Form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']  # Includes 'bio' for a more personalized profile


# Post Form (For Creating & Updating Posts)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
