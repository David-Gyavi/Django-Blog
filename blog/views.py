from django.shortcuts import render
from . models import Blog
from django.views.generic import ListView

#def homepage(request):
#    blogs = Blog.objects.all()
#    content = {'title': 'Home Django project', 'blog': blogs}


#    return render(request, 'blog/homepage.html', content)

class HomeListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    extra_context = {'title': 'Home Django project'}
    template_name = 'blog/homepage.html'      

def about(request):
    return render(request, 'blog/about.html', 
                 {'title': 'About Django project'})    


