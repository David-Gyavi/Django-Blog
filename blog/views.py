from django.shortcuts import render

def homepage(request):
    return render(request, 'blog/homepage.html', {'title': 'Home Django project'})

def about(request):
    return render(request, 'blog/about.html', {'title':'About Django project'})    

# Create your views here.
