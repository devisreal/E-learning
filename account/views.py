
from django.shortcuts import redirect, render
from .forms import UserForm, ProfileForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Account created successfully!')            
            return redirect('login')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'account/register.html', context)

def login(request):
    return render(request, 'account/login.html')