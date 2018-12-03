from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): # validate data
            form.save() # save data on database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has created!')
            return redirect('blog_home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required # user must be logged in to view this
def profile(request):
    return render(request, 'users/profile.html')