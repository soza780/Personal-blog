from django.contrib import admin

# Register your models here.
from blog.models import Post
from .forms import BlogForm


class BlogAdmin(admin.ModelAdmin):
    form = BlogForm
    list_display = ("title", "author", "created_date", "updated_date", "likes")
    list_filter = ("created_date", "updated_date", "likes")
    search_fields = ("title", "body", "created_date", "updated_date", "likes")
    date_hierarchy = "created_date"


admin.site.register(Post, BlogAdmin)
