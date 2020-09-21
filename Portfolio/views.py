from django.http import HttpResponse


def home (request):
    return HttpResponse("This is our Home page")

def about(request):
    return HttpResponse("This is About page")

def contact(request):
    return HttpResponse("This is Contact page")