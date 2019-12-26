from django import forms
from blog.models import Post, Blog, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description']
        widgets = {
            'user': forms.HiddenInput(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
