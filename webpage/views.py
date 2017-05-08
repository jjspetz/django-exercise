from django.contrib.staticfiles.templatetags.staticfiles import static

from django.template.response import TemplateResponse
def index (request):
    context = {
    
    }
    return TemplateResponse(request, 'index.html', context)
def about (request):
    context = {

    }
    return TemplateResponse(request, 'about.html', context)
def work (request):
    context = {

    }
    return TemplateResponse(request, 'work.html', context)
def resume (request):
    context = {

    }
    return TemplateResponse(request, 'resume.html', context)
