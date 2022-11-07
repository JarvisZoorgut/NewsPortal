from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'author']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")

        if title == content:
            raise ValidationError(
                "Заголовок не должен быть идентичен содержанию."
            )

        return cleaned_data
