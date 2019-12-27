from django.contrib.auth.decorators import login_required
from django.urls import path
from blog.views import BlogListView, BlogDetailView, BlogCreateView
from blog.views import PostListView, PostDetailView, PostCreateView
from blog.views import CommentCreateView

urlpatterns = [
    # path('', BlogListView.as_view(), name='home'),
    path('', BlogListView.as_view(), name='blog-list'),
    path('blog/create/', login_required(BlogCreateView.as_view()), name='blog-create'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),

    path('<str:slug>/', PostListView.as_view(), name='post-list'),
    path('post/create/', login_required(PostCreateView.as_view()), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('<int:post_id>/comment/create/', login_required(CommentCreateView.as_view()), name='comment-create')
]