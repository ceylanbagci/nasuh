from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
from core import email_operation
from django.template.loader import render_to_string
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    MASTER = 1
    USER_TYPE_CHOICES = (
        (MASTER, 'Sistem Yöneticisi'),
        
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, blank=True, default=MASTER)
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    class Meta:
        db_table = "auth_user"

    def __str__(self):
        return "%s %s %s"%(self.first_name,self.last_name,self.email)


    @property
    def is_master(self):
        return self.user_type == User.MASTER or self.is_superuser


    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def save(self,*args,**kwargs):
        if not self.username:
            self.username = get_random_string(length=15)

        if not self.id:
            self.is_active = False
        super().save(*args, **kwargs)

    def send_activation_key(self):

        message = render_to_string("authentication/activation_email.html", {"key": self.guid,"email_server": settings.EMAIL_SERVER})
        email_operation.send_email(message=message, subject="Sistem Aktivasyon Kodu",to_mail_list=[self.email,])

    def make_active(self):
        self.is_active = True
        self.save()
        return True

    def send_email(self):
        email_template = render_to_string("authentication/new_password_email.html",{"email_server":settings.EMAIL_SERVER,"key":self.guid})
        email_operation.send_email(message=email_template, subject="Sistem Şifre Yenileme", to_mail_list=[self.email,])