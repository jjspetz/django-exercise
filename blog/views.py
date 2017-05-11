from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404

from blog.models import Blog, Post

def blog_index(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    posts = Post.objects.filter(blog=blog)

    context = {
    'blog': blog,
    'posts': posts,
    }
    return TemplateResponse(request, 'blog.html', context)
