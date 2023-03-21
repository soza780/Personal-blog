from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from blog.models import Post


# Create your views here.

@login_required
def profile_view(request):
    """
    profile view function that renders user profile.
        * template tags : 'profile' , and 'posts'
        * url pattern -> 'profile/'

    :param:  request: GET
    :return: profile object of the user that have requested and the posts that user created.
    """
    queryset = UserProfile.objects.get(owner=request.user)
    user_posts = Post.objects.filter(author=request.user)
    return render(request, 'dashboard/index.html', {'profile': queryset, 'posts': user_posts})
