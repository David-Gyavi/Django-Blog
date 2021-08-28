from django.shortcuts import render
from . forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

# Create your views here.
