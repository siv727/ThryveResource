from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm  # Ensure you have a RegistrationForm

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate using email and password
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'home')  # Redirect to 'next' URL or 'home' if not present
            return redirect(next_url)
        else:
            # Invalid credentials, show an error message
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    
    # GET request, show login form
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the home page or any other page
    else:
        form = RegistrationForm()  # Show the registration form if it's a GET request

    return render(request, 'accounts/register.html', {'form': form})

@login_required
def logout(request):
    from django.contrib.auth import logout as auth_logout
    auth_logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'landing/home.html')
