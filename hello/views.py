from django.shortcuts import render
from .models import Greeting
# from django.http import HttpResponse
# Create your views here.
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def blog(request):
    template = loader.get_template('blog.html')
    context = {}
    return HttpResponse(template.render(context, request))

def blog_page(request, id):
    print ('showing you blog page ', id)
    template = loader.get_template('blog_page_' + str(id) + '.html')
    context = {}
    return HttpResponse(template.render(context, request))


def publication(request):
    template = loader.get_template('publication.html')
    context = {}
    return HttpResponse(template.render(context, request))


def workshop(request):
    template = loader.get_template('workshop.html')
    context = {}
    return HttpResponse(template.render(context, request))
