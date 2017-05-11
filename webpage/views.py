from django import http
from django.template.response import TemplateResponse
from django.core.mail import send_mail
import forms


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
def contact (request):
    contact_form  = forms.ContactMeForm(request.POST or None)

    if request.method == 'POST':
        if contact_form.is_valid():
            send_mail(
                'A message from ' + contact_form.cleaned_data['name'],
                contact_form.cleaned_data['question'] + '\n' + contact_form.cleaned_data['email'],
                'grofter@yahoo.com',
                ['grofter@yahoo.com'],
                fail_silently=False,
            )
            return http.HttpResponseRedirect('/thanks')
    context = {'form': contact_form}

    return TemplateResponse(request, 'contact.html', context)
def thankyou (request):
    context = {

    }
    return TemplateResponse(request, 'thankyou.html', context)
