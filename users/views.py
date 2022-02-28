from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created succesfully for {username}! Now you can login using your username and password!")
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', context={'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')

