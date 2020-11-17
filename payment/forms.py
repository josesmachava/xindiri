from django import forms

from .models import Payment


#class CommentForm(forms.ModelForm):
#    class Meta:
#        model = Comment
#        fields = ('body', )



class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('número_de_telefone',)


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)