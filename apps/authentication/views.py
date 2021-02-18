from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login,logout,get_user_model,update_session_auth_hash
from .forms import *
from django.contrib import messages
import core.custom_messages as custom_messages
import core.helper as hlp
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from core import email_operation

@csrf_protect
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            form.instance.send_activation_key()
            messages.success(request, custom_messages.SIGNUP_SUCCESS)
            return redirect("login")
        else:
            messages.error(request, custom_messages.SIGNUP_ERROR)
    else:
        form = SignUpForm()
    return render(request,'authentication/signup.html',locals())

@csrf_protect
def log_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            try:
                login(request, user)
                if request.user.is_master:
                    return redirect("/case/case_list")
            except Exception as e:
                messages.error(request, custom_messages.LOGIN_ERROR)
        else:
            messages.error(request, custom_messages.AUTHENTICATION_ERROR)
    form = LoginForm()
    return render(request, 'authentication/login.html', locals())

@csrf_protect
def log_out(request):
    logout(request)
    return redirect("/auth/login")


def login_activation(request):
    user = hlp.get_or_none(User,guid=request.GET['key'])
    user.make_active()
    messages.success(request, custom_messages.ACTIVISED_SUCCESS)
    return redirect('login')

@csrf_protect
def forgot_password(request):
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            forgot = form.save()
            forgot.send_email()
            messages.success(request,custom_messages.FORGOT_PASSWORD_SUCCESS)
            return redirect("login")
        else:
            messages.error(request,custom_messages.FORGOT_PASSWORD_ERROR)
    else:
        form = ForgotPasswordForm()
    return render (request,"authentication/login_forgot.html",locals())

def password_recovery(request,key):
    user = hlp.get_last(User  ,guid=key)
    if request.method == "POST":
        form = PasswordRecoveryForm(user=user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,custom_messages.PASSWORD_RECOVERY_SUCCESS)
            return redirect("login")
        else:
            messages.error(request,custom_messages.PASSWORD_RECOVERY_ERROR)
    else:
        form = PasswordRecoveryForm(user=user)
    return render (request,"authentication/password_recovery.html",locals())


@login_required
def password_change(request):
    if request.method == "POST":
        form = UpdatePasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,custom_messages.PASSWORD_CHANGE_SUCCESS)
            update_session_auth_hash(request, form.user)
            redirect_uri = request.GET.get("redirect_uri")
            return redirect(redirect_uri)
        else:
            messages.error(request,custom_messages.PASSWORD_CHANGE_ERROR)
    else:
        form = UpdatePasswordForm(user=request.user)
    return render (request,"authentication/password_change.html",locals())