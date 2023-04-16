from django import template
from blog.models import Post
from django.template.loader import get_template
register = template.Library()


@register.simple_tag
def recent_posts():
    posts = Post.objects.order_by('created_date')
    return {'posts': posts}

