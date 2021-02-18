from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email,RegexValidator,validate_integer
from .models import *
from core.forms import BaseForm
from django_select2 import forms as s2forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from core.models import District

class OfficeForm(BaseForm,forms.ModelForm):

    class Meta:
        model = Office
        fields = "__all__"
        exclude = ("created_at","slug",)
        widgets = {
        }


    def __init__(self, *args, **kwargs):
        super(OfficeForm, self).__init__(*args, **kwargs)




class EmployeeForm(BaseForm,forms.ModelForm):

    class Meta:
        model = Employee
        fields = "__all__"
        exclude = ("created_at","slug")
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields["office"].initial = Office.objects.get(id=1)
        self.fields["office"].widget = forms.HiddenInput()
        self.fields["office"].widget.attrs["readonly"] = True
    
        instance = kwargs.get("instance")
        if not instance:
            self.fields["district"].choices = District.objects.none()
        else:
            self.fields["district"].choices = District.objects.filter(city=instance.city).values_list('id', 'name')


    #
    # def clean_email(self):
    #     if self.cleaned_data['email'] != None:
    #         data = self.cleaned_data['email']
    #         if not validate_email(data):
    #             raise ValidationError("Geçerli bir mail adresi giriniz")
    #         return data
    #     else:
    #         return self.cleaned_data['email']

    def clean_salary(self):
        numeric = RegexValidator(r'^[0-9+]', 'Tutarı Sayı Olarak Giriniz')
        numeric(self.cleaned_data['salary'])
        return self.cleaned_data['salary']

