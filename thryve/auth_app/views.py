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
    # from your model Listing(...) if you have one
    listings = []  # replace with Listing.objects.all()
    return render(request, 'landing/home.html', {'listings': listings})

@login_required
def community_feed(request):
    posts = [
        {
            "name": "Lisa Anderson",
            "org": "GreenTech Solutions",
            "date": "1/15/2024",
            "text": "Just completed a successful equipment swap with another SME! This platform is amazing for finding win-win deals. Saved us thousands on new machinery.",
            "likes": 24, "comments": 2, "avatar": "https://i.pravatar.cc/64?img=47",
        },
        {
            "name": "James Rodriguez",
            "org": "Digital Marketing Pro",
            "date": "1/14/2024",
            "text": "Looking for recommendations on industrial printers. Our current one is outdated and we need something reliable for high-volume printing. Budget around $10K.",
            "likes": 12, "comments": 1, "avatar": "https://i.pravatar.cc/64?img=12",
        },
        {
            "name": "Marcus Thompson",
            "org": "FoodTech Innovations",
            "date": "1/13/2024",
            "text": "Successfully traded our old packaging equipment for restaurant-grade kitchen appliances. Perfect for optimizing resources without cash flow issues!",
            "likes": 30, "comments": 5, "avatar": "https://i.pravatar.cc/64?img=33",
        },
        {
            "name": "Sarah Chen",
            "org": "EcoBuilders LLC",
            "date": "1/12/2024",
            "text": "Thrilled to announce our new partnership with GreenTech Solutions! Excited for the sustainable projects we'll embark on together.",
            "likes": 45, "comments": 7, "avatar": "https://i.pravatar.cc/64?img=5",
        },
    ]
    # template path you requested:
    return render(request, 'landing/community.html', {'posts': posts})
