from django.template.response import TemplateResponse
def homepage (request):
    context = {
        'page_title': 'Home Page',
        'name': 'JJ Spetseris',
        'reply': ['s','w','e','e','t'],
        'num': [0,1,2,3,4]
    }
    return TemplateResponse(request, 'homepage.html', context)
