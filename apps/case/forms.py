from django import forms
from .models import *
from core.forms import BaseForm
from django_select2 import forms as s2forms
from core.models import District
from case.models import Partnership
import core.custom_messages as custom_messages
import core.helper as hlp

class CaseForm(BaseForm,forms.ModelForm):

    class Meta:
        model = Case
        fields = "__all__"
        exclude = ("created_at","slug",)
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2}),
            # "client":FilteredSelectMultiple('Müvekkiller', is_stacked=False),
            "client": s2forms.Select2MultipleWidget(),
            "partner": s2forms.Select2MultipleWidget(),

        }


    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'data-target': 'kt_datetimepicker_1'})
        self.fields['client'].widget.attrs.update({'data-language': 'tr'})
        self.fields['partner'].widget.attrs.update({'data-language': 'tr'})
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

class ShareForm(BaseForm,forms.ModelForm):

    class Meta:
        model = Partnership
        fields = "__all__"
        exclude = ("created_at",)


    def __init__(self, *args, **kwargs):
        super(ShareForm, self).__init__(*args, **kwargs)
        initial = kwargs.get("initial")
        self.fields["partner"].initial = initial['partner']
        self.fields['case'].initial = initial['case']

    def clean_share(self):
        share = self.cleaned_data['share']
        if share < 1 or share > 100:
            raise forms.ValidationError(
                "1 ile 100 arasında bir değer girilmelidir."
            )
        return share


    def clean(self):
        cleaned_data = self.cleaned_data
        case = self.cleaned_data['case']
        partner = self.cleaned_data['partner']
        if hlp.get_or_none(Partnership, case=case, partner=partner):
            raise forms.ValidationError('Bu ortak ve dava dosyası ile ilgili bir kayıt var.')
        return cleaned_data