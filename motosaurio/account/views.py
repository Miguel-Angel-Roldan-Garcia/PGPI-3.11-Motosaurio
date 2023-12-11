from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, UserProfileForm
from motosaurio.models import MiUsuario
from django import forms

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()  
    return render(request, 'account/login.html', {'form': form})

#@login_required
#def dashboard(request):
    #return render(request, 'account/dashboard.html',{'section':'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            return render(request,
                        'account/register_done.html',
                        {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                'account/register.html',
                {'user_form': user_form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        try:
            if form.is_valid():
                user = request.user
                user.direccion =form.direccion_invalida()
                user.codigo =form.codigo_invalido()
                user.save()
                return render(request,
                            'account/profile_updated.html', 
                            {'user': request.user}) 
        except forms.ValidationError as e:
            error_message = 'Tanto la dirección como el código postal deben estar cumplimentados'
            return render(request, 'account/error.html', {'error_message': error_message}) 
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'account/profile.html', {'form': form})