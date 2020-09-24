from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Business, Token
from django.db import transaction
from django.forms import ModelForm


class BusinessSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='Nome',  required=True, widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    last_name = forms.CharField(max_length=30, label='Apelido', required=True    , widget=forms.TextInput(attrs={'placeholder': 'Apelido'}))
    email = forms.EmailField(max_length=254, label='Email',  widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    password1 = forms.CharField(label='Palavra passe',  widget=forms.PasswordInput(attrs={'placeholder': 'Palavra Passe'}))
    password2 = forms.CharField(label='Repitir Palavra Passe ',  widget=forms.PasswordInput(attrs={'placeholder': 'Repitir Palavra Passe  '}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1')
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)

        user.save()

        business = Business.objects.create(user=user)
        token = Token.objects.create(user=user)

        user.is_active = False
        user.is_business = False
        return user


class BusinessForm(ModelForm):
    phone_number = forms.CharField(max_length=30, label='Número de telefone', required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Número de telefone'}))
    company_name = forms.CharField(max_length=30, label='Nome comercial', required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Nome comercial'}))
    nuit = forms.CharField(max_length=30, label='Nuit', required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Nuit'}))
    website = forms.CharField(max_length=30, label='Website', required=True,
                              widget=forms.TextInput(attrs={'placeholder': 'Website'}))
    address = forms.CharField(max_length=30, label='Endereço', required=True,
                              widget=forms.TextInput(attrs={'placeholder': 'Endereço'}))
    province = forms.CharField(max_length=30, label='Província', required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Província'}))
    location = forms.CharField(max_length=30, label='Localidade', required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Localidade'}))

    class Meta:
        model = Business
        fields = ('phone_number', 'company_name', 'nuit', 'website', 'address', 'province', 'location')
