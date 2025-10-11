from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import BusinessProfile, ProfileCustomization
from .forms import BusinessProfileForm, ProfileCustomizationForm

@login_required
def business_profile_view(request):
    bp, _ = BusinessProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = BusinessProfileForm(request.POST, request.FILES, instance=bp)
        if form.is_valid():
            form.save()
            return redirect('business_profile')
    else:
        form = BusinessProfileForm(instance=bp)

    # 👇 use this template name because your file is under templates/profile_app/
    return render(request, 'profile_app/business_profile.html', {'form': form})


@login_required
def profile_customization_view(request):
    pc, _ = ProfileCustomization.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileCustomizationForm(request.POST, request.FILES, instance=pc)
        if form.is_valid():
            form.save()
            return redirect('profile_customization')
    else:
        form = ProfileCustomizationForm(instance=pc)

    # If this file is also under templates/profile_app/, use:
    return render(request, 'profile_app/profile_customization.html', {'form': form})

