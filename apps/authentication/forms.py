from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from .models import *
from core.forms import *
import core.custom_messages as custom_messages


class SignUpForm(BaseForm,UserCreationForm):
    is_informed_promotions = forms.BooleanField(required=False)
    error_css_class = 'is_invalid'
    class Meta:
        model = User
        fields = ("first_name", "last_name", "user_type", "email", "password1", "password2")


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["user_type"].widget = forms.HiddenInput()
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] += " form-control-solid h-auto py-6 px-6 rounded-lg font-size-h6"

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError(custom_messages.EMAIL_ALREADY_EXISTS)
        except User.DoesNotExist:
            return email


class LoginForm(BaseForm,AuthenticationForm):
    class Meta:
        model = User
        fields = ("username","password",)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] += " form-control-solid h-auto py-6 px-6 rounded-lg font-size-h6"


class ForgotPasswordForm(BaseForm, PasswordResetForm):
    email = forms.EmailField(max_length=254,widget=forms.TextInput(attrs={"placeholder":"Kayıtlı E-Posta Adresinizi girin"}))

    def __init__(self, *args, **kwargs):
        super(ForgotPasswordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] += " form-control-solid h-auto py-6 px-6 rounded-lg font-size-h6"


    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            self.user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError(custom_messages.EMAIL_DOES_NOT_EXISTS)
        return email

    def save(self):
        return self.user


class PasswordRecoveryForm(BaseForm,SetPasswordForm):
    def __init__(self,*args, **kwargs):
        super(PasswordRecoveryForm, self).__init__(*args, **kwargs)
        self.user = kwargs.get("user")
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] += " form-control-solid h-auto py-6 px-6 rounded-lg font-size-h6"


class UpdatePasswordForm(BaseForm,PasswordChangeForm):
    def __init__(self,*args, **kwargs):
        super(UpdatePasswordForm, self).__init__(*args, **kwargs)