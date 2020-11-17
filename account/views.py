from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import BusinessSignUpForm, BusinessForm
from .models import Startup


def signin(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            if not request.user.is_business:
                return redirect('active',  request.user.startup.id)
            return redirect('index')
        else:
            messages.error(request, "E-mail ou palavra-passe não correspodem.")
    return render(request, 'account/signin.html')


def businesssignup(request):
    if request.method == 'POST':
        form = BusinessSignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = form.save()

            user = authenticate(username=email, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('active', request.user.startup.id)

    else:
        form = BusinessSignUpForm()
    return render(request, 'account/business_account.html', {'form': form})


login_required()


class EditCompany(UpdateView):
    # template_name_suffix = 'account/edit.html'
    template_name = "account/edit.html"
    model = Startup
    form_class = BusinessForm
    success_url = reverse_lazy('index')


login_required()


def logout_view(request):
    logout(request)
    # Redirect to a succe
