from django import forms
from .models import Post, Comment

class PostForm( forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            max_size = 2 * 1024 * 1024
            if image.size > max_size:
                raise forms.ValidationError("Image size should not exceed 2MB.")
            
            valid_mime_types = ['image/jpeg', 'image/png', 'image/gif']
            if image.content_type not in valid_mime_types:
                raise forms.ValidationError("Invalid image format. Only JPEG, PNG, and GIF are allowed.")
        return image
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  
        fields = ['name', 'email', 'content']

