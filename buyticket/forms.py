from django import forms
from django.contrib.auth.forms import UserCreationForm , SetPasswordForm
from django.contrib.auth.models import User
from django.forms import ModelForm 
from .models import Payment
from django.contrib.auth import get_user_model


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(help_text=None , max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    def __init__(self,*arg,**kwarg):
        super(RegisterUserForm,self).__init__(*arg,**kwarg)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
        for fieldname in ['username']:
            self.fields[fieldname].help_text = "<div class=\"alert alert-warning alert-dismissible fade show\" role=\"alert\"><p>User name should be less or equal 50 characters</p><button type=\"button\" class=\"btn-close btn-outline-warning\" data-bs-dismiss=\"alert\" aria-label=\"close\"></button></div>"
        for fieldname in ['password1']:
            self.fields[fieldname].help_text = "<div class=\"alert alert-warning alert-dismissible fade show\" role=\"alert\"><ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul><button type=\"button\" class=\"btn-close btn-outline-warning\" data-bs-dismiss=\"alert\" aria-label=\"close\"></button></div>"
        for fieldname in ['password2']:
            self.fields[fieldname].help_text = "<div class=\"alert alert-warning alert-dismissible fade show\" role=\"alert\"><p>Retype previous password for confirmation...</p><button type=\"button\" class=\"btn-close btn-outline-warning\" data-bs-dismiss=\"alert\" aria-label=\"close\"></button></div>"




class SetPasswordForm(SetPasswordForm):
    class meta:
        model = get_user_model()
        fields = ['password1','password2']


#
        
        

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ("contact","email","quantity")
    def __init__(self,*arg,**kwarg):
        super(PaymentForm,self).__init__(*arg,**kwarg)
        self.fields['contact'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['quantity'].widget.attrs['class']='form-control'
        for fieldname in ['email']:
            self.fields[fieldname].help_text = "<div class=\"alert alert-warning alert-dismissible fade show\" role=\"alert\"><p>Enter A Valid/Active Email To Recieve Reciept</p><button type=\"button\" class=\"btn-close btn-outline-warning\" data-bs-dismiss=\"alert\" aria-label=\"close\"></button></div>"
        for fieldname in ['contact']:
            self.fields[fieldname].help_text = "<div class=\"alert alert-warning alert-dismissible fade show\" role=\"alert\"><p>Contact should be in format (e.g  +234-000-000-0000)</p><button type=\"button\" class=\"btn-close btn-outline-warning\" data-bs-dismiss=\"alert\" aria-label=\"close\"></button></div>"
        for fieldname in ['quantity']:
            self.fields[fieldname].help_text = "<div class=\"alert alert-warning alert-dismissible fade show\" role=\"alert\"><p>Select Ticket Quantity</p><button type=\"button\" class=\"btn-close btn-outline-warning\" data-bs-dismiss=\"alert\" aria-label=\"close\"></button></div>"
