from django.contrib import admin
from .models import Post, Comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'author', 'date_posted']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'date_commented']
    list_filter = ['date_commented']
    search_fields = ['name', 'email', 'content']

    def post_title(self, obj):
        return obj.post.title
    
    post_title.short_description = 'Post Title'
