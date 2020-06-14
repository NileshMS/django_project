from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            # messages.success(request,f'Account created for {username}!')
            messages.success(request, f'{username} account has been created! now you are able to log in ')
            return redirect('login')
        else:
            return render(request, 'users/registration.html', {'form': form})
    else:
        form = UserRegisterForm()
        return render(request, 'users/registration.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
