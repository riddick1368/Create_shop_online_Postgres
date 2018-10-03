from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm,RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required



# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            redirect_url = request.GET.get('next', 'home')
            return redirect(redirect_url)
        else :
            messages.error(request,"Bad username or password")

    return render(request,"login.html",context={})



def user_logout(request):
        logout(request)
        return redirect("home")


def register_user(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password_1']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username,password=password,email=email)
            messages.success(request,"Thank for your register {}".format(user.username))
            user = authenticate(username = form.cleaned_data['username'],
                                password= form.cleaned_data["password_1"])
            login(request,user)
            return redirect("home")
    else :
        form = RegisterForm()
    return render(request,"register_user.html",context={'form':form})


# Password Rest
# def password_reset(request,
#                    template_name='registration/password_reset_form.html',
#                    email_template_name='registration/password_reset_email.html',
#                    subject_template_name='registration/password_reset_subject.txt',
#                    password_reset_form=PasswordResetForm,
#                    #...):
#
# def password_reset_done(request,
#                         template_name='registration/password_reset_done.html',
#                         extra_context=None):
#
# def password_reset_confirm(request, uidb64=None, token=None,
#                            template_name='registration/password_reset_confirm.html',
#                            token_generator=default_token_generator,
#                            #...):
#
# def password_reset_complete(request,
#                             template_name='registration/password_reset_complete.html',
#                             extra_context=None):

# doesn't work correct!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@login_required()
def Change_Password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request, _('Your password was successfully updated!'))
            return redirect('home')
        else:
            return redirect('accounts:change_password')
    else :
        form = PasswordChangeForm(user=request.user)
    return render(request,"change_password.html",context={'form':form})