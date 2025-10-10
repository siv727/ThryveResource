from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)  # Authenticate with email
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'home')  # Redirect to the 'next' URL or 'home' by default
            return redirect(next_url)
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'landing/home.html')
