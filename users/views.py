from django.shortcuts import render, redirect
from . forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            return redirect('blog-homepage')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

# Create your views here.
