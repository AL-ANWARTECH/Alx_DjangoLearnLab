from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from taggit.forms import TagWidget  # ✅ Import TagWidget
from .models import Profile, Post, Comment

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


# ✅ Post Form (For Creating & Updating Posts with TagWidget)
class PostForm(forms.ModelForm):
    tags = forms.CharField(
        widget=TagWidget(attrs={'class': 'form-control', 'placeholder': 'Add tags separated by commas'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


# Comment Form (For Adding & Editing Comments)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Write a comment...'}),
        }

