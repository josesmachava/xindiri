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
from .models import  Business

def signin(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

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
    return render(request, 'account/businessAccount.html', {'form': form})

class   EditCompany(UpdateView):
    # template_name_suffix = 'account/edit.html'
    template_name = "account/edit.html"
    form_class = BusinessForm
    model = Business
    success_url = reverse_lazy('index')

@login_required()
def logout_view(request):
    logout(request)
    # Redirect to a succe
