from dataclasses import field
from django import forms
from App_post.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image', 'caption']
        