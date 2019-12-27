from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from blog.forms import PostForm, BlogForm, CommentForm
from blog.models import Post, Blog, Comment



# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'home.html', context)

# BLOGS

class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# POSTS

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs.get('slug'))
        blog = Blog.objects.get(user=user)
        return self.model.objects.filter(blog=blog)


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog-list')

    def form_valid(self, form):
        blog = Blog.objects.get(user=self.request.user)
        form.instance.blog = blog
        return super().form_valid(form)


# COMMENTS

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    # success_url = reverse_lazy('post-detail', args=[self.kwargs.get('post_id')])

    def form_valid(self, form):
        post = Post.objects.get(id=self.kwargs.get('post_id'))
        form.instance.post = post
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):         
        if  kwargs != None:
            return reverse_lazy('post-detail', args=[self.kwargs.get('post_id')])