from django.contrib import admin
from blog.models import Post, Blog, Comment

admin.site.register([Blog, Post, Comment])

