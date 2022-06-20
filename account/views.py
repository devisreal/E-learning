from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import ProfileForm, UserForm

# Create your views here.
# =========================================================== REGISTER ===========================================================
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']        

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email Taken')
                    return redirect('register')                    
                else:
                    user = User.objects.create_user(
                        username=username, 
                        first_name=firstname, 
                        last_name=lastname,
                        email=email, 
                        password=password                    
                    )
                    auth.login(request, user)
                    messages.success(request, 'Account created successfully, please complete your profile')
                    return redirect('edit_profile')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')        

    context = {

    }
    return render(request, 'account/register.html', context)


# =========================================================== EDIT PROFILE ===========================================================

def edit_profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST or None, instance = request.user)
        profile_form = ProfileForm(request.POST or None, request.FILES or None, instance = request.user.profile ) 

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('login')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)   

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'account/edit_profile.html', context)

# =========================================================== LOGIN ===========================================================
def login(request):
    return render(request, 'account/login.html')