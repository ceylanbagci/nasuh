"""
Kullanıcı tiplerine göre yetkili olunan işlevleri; kullanıcıların neleri yapabileceklerini ve neleri görebileceklerini
kontrol etmek için oluşturulan dekoratörlerdir.

"""

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from functools import wraps
from django.contrib.auth.views import redirect_to_login

def customer_required(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        if not (request.user.is_active and request.user.is_customer) or (kwargs.get("username") and not request.user.username == kwargs.get("username")):
            path = request.build_absolute_uri()
            return redirect_to_login(path, settings.LOGIN_URL, settings.LOGIN_REDIRECT_URL)
        return func(request, *args, **kwargs)
    return inner


def master_required(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        if not (request.user.is_active and request.user.is_master) or (kwargs.get("username") and not request.user.username == kwargs.get("username")):
            path = request.build_absolute_uri()
            return redirect_to_login(path, settings.LOGIN_URL, settings.LOGIN_REDIRECT_URL)
        return func(request, *args, **kwargs)
    return inner

