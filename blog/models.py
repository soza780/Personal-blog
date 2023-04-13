from django.db import models
from account.models import CustomUser
from django.urls import reverse

user = CustomUser


# Create your models here.


class Post(models.Model):
    """
    __str__ -> self.title

    get_absolute_url -> reverse to post-detail (post.pk)
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, null=True)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})
