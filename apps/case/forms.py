from django import forms
from .models import *
from core.forms import BaseForm
from django_select2 import forms as s2forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from core.models import District

class CaseForm(BaseForm,forms.ModelForm):

    class Meta:
        model = Case
        fields = "__all__"
        exclude = ("created_at","slug",)
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2}),
            # "client":FilteredSelectMultiple('Müvekkiller', is_stacked=False),
            "client": s2forms.Select2TagWidget(),
            "partner": s2forms.Select2TagWidget(),

        }


    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'data-target': 'kt_datetimepicker_1'})
        self.fields['client'].queryset = Client.objects.all()
        self.fields['partner'].queryset = Partner.objects.all()
        self.fields['partner'].required = False
        self.fields['client'].required = False


        instance = kwargs.get("instance")
        if not instance:
            self.fields["district"].choices = District.objects.none()
        else:
            self.fields["district"].choices = District.objects.filter(city=instance.city).values_list('id', 'name')


class ClientForm(BaseForm,forms.ModelForm):

    class Meta:
        model = Client
        fields = "__all__"
        exclude = ("created_at","slug")
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

        instance = kwargs.get("instance")
        if not instance:
            self.fields["district"].choices = District.objects.none()
        else:
            self.fields["district"].choices = District.objects.filter(city=instance.city).values_list('id', 'name')


class PartnerForm(BaseForm,forms.ModelForm):

    class Meta:
        model = Partner
        fields = "__all__"
        exclude = ("created_at","slug")
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super(PartnerForm, self).__init__(*args, **kwargs)

        instance = kwargs.get("instance")
        if not instance:
            self.fields["district"].choices = District.objects.none()
        else:
            self.fields["district"].choices = District.objects.filter(city=instance.city).values_list('id', 'name')


class ExpenseForm(BaseForm,forms.ModelForm):

    class Meta:
        model = Expense
        fields = "__all__"
        exclude = ("created_at","slug")
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['case'].required = False


