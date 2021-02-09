"""Email ile Kimlik Doğrulama
Django'nun varsayılan kimlik doğrulaması, kullanıcı adı ve şifre ile çalışır.
E-posta kimlik doğrulaması, e-posta ve şifreye göre kullanıcıların kimliğini doğrular.
"""
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

class EmailAuthenticationBackend(BaseBackend):
    """
    Email ile kimlik doğrulama için geliştirilen özel arka uç
    """
    def authenticate(self, request, username=None, password=None):
        User = get_user_model()
        try:
            user = User.objects.get(email=username)
            if check_password(password, user.password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            User = get_user_model()
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
