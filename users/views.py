from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import UserSignupForm, EmailLoginForm


def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Update to your desired post-signup page
    else:
        form = UserSignupForm()
    return render(request, 'users/signup.html', {'form': form})


class EmailLoginView(LoginView):
    authentication_form = EmailLoginForm
    template_name = 'users/login.html'
