from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
import forms

from blog.models import Blog, Post, Poll, Choice

def blog_index(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    posts = Post.objects.filter(blog=blog)

    context = {
        'blog': blog,
        'posts': posts,
    }
    return TemplateResponse(request, 'blog.html', context)

def blog_post(request, blog_slug, post_slug):
    context = {
        'post': get_object_or_404(Post, slug=post_slug, blog__slug=blog_slug)
    }
    return TemplateResponse(request, 'blog_post.html', context)

def poll(request, poll_slug):
    poll = get_object_or_404(Poll, slug=poll_slug)
    answers = Choice.objects.filter(poll=poll)
    print(answers)

    form = forms.PizzaPoll(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            for answer in answers:
                print(answer)
                if answer.answer == form.cleaned_data['choice']:
                    answer.votes += 1
                    answer.save()
            context = {
                'results': answers,
            }

            return TemplateResponse(request, 'results.html', context)

    context = {
        'form' : form,
        'poll' : poll,
    }
    return TemplateResponse(request, 'polls.html', context)
