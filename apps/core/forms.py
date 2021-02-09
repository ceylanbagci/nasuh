from django import forms
from .models import *

class BaseForm():
    """
    Html elementlerini tema ile uyumlu hale getirmek için kullanılır. Uygulamadaki tüm django formları
    bu base formdan türetilir.
    """
    error_css_class = 'is_invalid'
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():

            visible.field.error_messages = {
                "required": 'Bu alan boş bırakılamaz',
                "invalid": "Geçerli bir değer girilmelidir"
            }
            visible.field.widget.attrs["autocomplete"] = "off"
            visible.field.widget.attrs['placeholder'] = visible.label
            visible.field.widget.attrs['class'] = 'form-control'

            if "class" in visible.field.widget.attrs.keys():
                visible.field.widget.attrs["class"] += " prompt srch_explore"
            else:
                visible.field.widget.attrs.update({'class':'prompt srch_explore'})

            if type(visible.field)==forms.fields.DateTimeField:
                visible.field.widget.attrs["class"] += " datetimepicker-input"
            elif type(visible.field)==forms.fields.DateField:
                visible.field.widget.attrs["class"] += " datepicker-input"
            elif type(visible.field)==forms.fields.TypedChoiceField or type(visible.field)==forms.models.ModelChoiceField or type(visible.field)==forms.ChoiceField:
                visible.field.widget.attrs["class"] += " ui dropdown cntry152"
            elif type(visible.field)==forms.fields.ImageField:
                visible.field.widget.attrs["class"] += " image"
            elif type(visible.field)==forms.fields.TimeField:
                visible.field.widget.attrs["class"] += " time"

