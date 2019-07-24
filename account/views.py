from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import SignUpForm, StudentSignUpForm, StudentSignUpdateForm
from kutiva.views import index
from .models import *

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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('index')

    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})


def sudentsignup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('index')

    else:
        form = StudentSignUpForm()
    return render(request, 'account/student_signup.html', {'form': form})



class StudentPerfile(UpdateView):
    template_name = "account/perfile.html"
    form_class = StudentSignUpdateForm
    model = User
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()

        # user.student.location = form.cleaned_data.get('location')
        # user.student.location = form.cleaned_data.get('description')
        # user.student.location = form.cleaned_data.get('birth_date_year')
        # user.student.location = form.cleaned_data.get('phone_number')
        # user.student.location = form.cleaned_data.get('educational_institution')
        user.student.save()
        return redirect('index')



@login_required()
def logout_view(request):
    logout(request)
    # Redirect to a succe
