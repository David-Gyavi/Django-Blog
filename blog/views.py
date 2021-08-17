from django.shortcuts import render

def homepage(request):
    return render(request, 'blog/homepage.html')

# Create your views here.
