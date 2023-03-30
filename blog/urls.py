from django.urls import path

from .views import PostList, PostDetailView, PostCreateView, PostUpdateView

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', PostCreateView.as_view(template_name='blog/post_create.html'), name='post-create'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(template_name='blog/post_update.html'), name='post-update'),
]
