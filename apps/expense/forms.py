from django import forms
from .models import *
from core.forms import BaseForm
from django_select2 import forms as s2forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from core.models import District
from office.models import Office



class ExpenseForm(BaseForm,forms.ModelForm):

    class Meta:
        model = Expense
        fields = ("title","description","type","office","tax","other")
        exclude = ("created_at","slug")
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        url = kwargs.pop("url",None)
        if url != None:
            coming_url = url['coming_url']
        super(ExpenseForm, self).__init__(*args, **kwargs)
        if url!=None:
            if 'office' in coming_url:
                self.fields['office'].initial = [1]
            elif 'tax' in coming_url:
                self.fields['tax'].initial = [1]
            elif 'other' in coming_url:
                self.fields['other'].initial = [1]


