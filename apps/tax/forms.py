from django import forms
from .models import *
from core.forms import BaseForm


class TaxForm(BaseForm,forms.ModelForm):

    class Meta:
        model = Tax
        fields = "__all__"
        exclude = ("created_at","slug",)

