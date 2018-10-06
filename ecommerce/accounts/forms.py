from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import ContactUs


class LoginForm(forms.Form):
    username = forms.CharField(max_length=120,widget=forms.TextInput(attrs={"class":'form-cotnrol'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))



class RegisterForm(forms.Form):
    username = forms.CharField(max_length=120,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    password_1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password_2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':"form-control"}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))


    def cleanEmail(self):
        email = self.cleaned_data['email']
        if not email :
            raise ValidationError("you don't enter a email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('this email already token ')
        return email

    ##### ravesh hai dg barai clean kardan password behtarin ravesh seda zadan tabe asli yani clean hast


    # def clean_password1(self):
    #     # this will raise a key error because it references password2 field
    #     # which is ran AFTER password1 validation
    #     p1 = self.cleaned_data['password1']
    #     p2 = self.cleaned_data['password2']
    #     if p1 != p2:
    #         raise ValidationError('Password1 Does Not Match Password2')
    #     return p1

    # def clean_password2(self):
    #     p1 = self.cleaned_data['password1']
    #     p2 = self.cleaned_data['password2']
    #     if p1 != p2:
    #         raise ValidationError('Password2 Does Not Match Password1')
    #     return p2


    def clean(self):
        cleaned_data = super().clean()
        p1 = self.cleaned_data['password_1']
        p2 = self.cleaned_data['password_2']
        if p1 and p2 :
            if p1 != p2:
                raise ValidationError("password dosen't match ")




class ContactForm(forms.ModelForm):
    message = forms.TextInput()


    class Meta :
        model = ContactUs
        fields = ['name','email','subject']