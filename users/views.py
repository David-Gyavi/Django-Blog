from django.shortcuts import render, redirect
from . forms import UserRegistrationForm, UserProfileForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Registration success for {username}')
            return redirect('blog-homepage')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Profile updated for the user {username}')
            return redirect('users-profile')
    else:
        form = UserProfileForm()
    return render(request, 'users/profile.html', {'form': form})

