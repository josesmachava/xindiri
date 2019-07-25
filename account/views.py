from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import BusinessForm


def signin(request):
    if request.method == 'POST':
        phone_number = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=phone_number, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "E-mail e senha não correspodem.")
    return render(request, 'account/signin.html')


def businesssignup(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('index')

    else:
        form = BusinessForm()
    return render(request, 'account/signup.html', {'form': form})


@login_required()
def logout_view(request):
    logout(request)
    # Redirect to a succe
