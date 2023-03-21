from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from blog.models import Post


# Create your views here.


class PostList(ListView):
    """
    post list CBV.

    * fields -> title, author , body, created_date, updated_date, likes
    * template name =  blog/post_list.html

    """
    queryset = Post.objects.all()

    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'created_date', 'updated_date', 'likes')
        template_name = 'blog/post_list.html'


class PostDetailView(DetailView):
    """
    Post detail CBV

    template name : blog/post_detail.html
    """
    queryset = Post.objects.all()

    class Meta:
        model = Post
        template_name = 'blog/post_detail'


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    fields:
        * title, slug, author, img, body

    login required
    """
    queryset = Post.objects.all()
    fields = ('title', 'slug', 'author', 'img', 'body')
    model = Post
    # template_name = 'blog/post_create'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    fields:
        * title, slug, img, body
    success url:
        * localhost:8000/blog/

    test function tests post author is who requested or not

    login required
    """
    model = Post
    fields = ('title', 'slug', 'img', 'body')
    success_url = 'http://localhost:8000/blog/'

    def test_func(self):
        """
        checks requested user is author or not
        :return: BOOLEAN
        """
        author = self.get_object().author
        user = self.request.user
        return author == user


def about_view(request):
    """
    renders a html page for displaying about us view

    :param request:HTTP request GET
    :return: html template
    """
    return render(request, template_name='about_us.html')
