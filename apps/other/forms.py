from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email,RegexValidator,validate_integer
from .models import *
from core.forms import BaseForm
from django_select2 import forms as s2forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from core.models import District

class OtherForm(BaseForm,forms.ModelForm):

    class Meta:
        model = Other
        fields = "__all__"
        exclude = ("created_at","slug",)

