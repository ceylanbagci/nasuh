from django import forms
from core.forms import *
from .models import *
from django.contrib import messages
import core.custom_messages as custom_messages
from case.models import*
from django.core.exceptions import ValidationError

class EventForm(BaseForm,forms.ModelForm):

    class Meta:
        model = Event
        fields = "__all__"
        exclude = ('created_at','slug', 'editable')
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields["client"].queryset = Client.objects.all()
        self.fields["case"].queryset = Case.objects.all()
        self.fields["backgroundColor"].widget = forms.HiddenInput()
        self.fields["borderColor"].widget = forms.HiddenInput()



    def clean(self):
        cleaned_data = super().clean()
        end = cleaned_data.get("end")
        start = cleaned_data.get("start")
        print(end)
        print(type(end))
        print(end > start)
        if end < start:
            raise ValidationError(
                "Bitiş Tarihi Önce Olamaz"
            )
        return cleaned_data