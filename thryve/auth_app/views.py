from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

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

@login_required
def logout(request):
    from django.contrib.auth import logout as auth_logout
    auth_logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'landing/home.html')
