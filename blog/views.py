from django.shortcuts import render
from . models import Blog
from django.views.generic import ListView, TemplateView


class HomeListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    extra_context = {'title': 'Home Django project'}
    template_name = 'blog/homepage.html'      


class AboutTemplateView(TemplateView):
     extra_context = {'title': 'About Django project'}
     template_name = 'blog/about.html'  


