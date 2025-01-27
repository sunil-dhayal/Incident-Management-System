from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .registration import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')
            return redirect('users:login')
        else:
            for error in form.errors.values():
                messages.error(request, error)

    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

class UserLoginView(LoginView):
    template_name = 'users/login.html'  # Specify your template
    next_page = 'users:profile' # Redirect to profile after login

@login_required # Protects the view, only logged in users can access
def profile(request):
    return render(request, 'users/profile.html')

def logout_view(request):
    logout(request)  # This is crucial for clearing the session
    messages.success(request, "You have been successfully logged out.") #Optional message
    return redirect('users:login')
    # return render(request, 'users/login.html')
