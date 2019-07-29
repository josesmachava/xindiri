from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Business, Token
from django.db import transaction
from django.forms import ModelForm


class BusinessForm(UserCreationForm):
    phone_number = forms.CharField(max_length=30, label='', required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Numero de telefone'}))

    first_name = forms.CharField(max_length=30, label='', required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    last_name = forms.CharField(max_length=30, label='', required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Apelido'}))
    email = forms.EmailField(max_length=254, label='',  widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Repitir Senha'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('phone_number', 'first_name', 'last_name', 'email', 'password1')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_active = False
        user.is_business = True

        user.save()

        business = Business.objects.create(user=user)
        token  = Token.objects.create(user=user)
        return user


class StudentSignUpdateForm(ModelForm):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Nome'}), max_length=30,
                                 required=False, help_text='Optional.')
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Apelido'}), max_length=30,
                                required=False, help_text='Optional.')
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'placeholder': 'E-mail'}), max_length=254,
                             help_text='Required. Inform a valid email address.')
    location = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'loacal'}), max_length=30,
                               required=False)
    phone_number = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Número de telefone'}),
                                   max_length=30)
    description = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Sobre me'}), max_length=30)
    educational_institution = forms.CharField(label="",
                                              widget=forms.TextInput(attrs={'placeholder': 'Instituição de ensino'}),
                                              max_length=30)
    birth_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'location', 'birth_date', 'phone_number', 'description',
                  'educational_institution')


