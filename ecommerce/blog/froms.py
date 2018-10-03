from django import forms
from .models import Post



class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            "title",
            "description",
            "slug",
        ]



class PostEditForm(forms.ModelForm):

    class Meta :
        model = Post

        fields = ["title",
                  "description",
                  'slug'
         ]