from django.forms import Form, ModelForm
from . import models


class PostForm(ModelForm):
    class Meta:
            model = models.Post
            fields = ['title', 'text', 'author', 'status']