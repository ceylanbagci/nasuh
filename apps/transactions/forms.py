from django import forms
from core.forms import *
from .models import *
from office.models import Employee
from case.models import Case
from expense.models import Expense

class TransactionForm(BaseForm,forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ("amount","type",'expense','date','description')
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        initial = kwargs.pop('initial')
        self.fields["expense"].initial = initial['instance']



class SalaryForm(BaseForm,forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ("amount","type",'expense','date','description','employee')
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super(SalaryForm, self).__init__(*args, **kwargs)
        initial = kwargs.pop('initial')
        # expense = kwargs.pop('expense')
        self.fields["employee"].initial = initial['employee']
        self.fields["expense"].initial = initial['expense']
        self.fields["employee"].disabled = True
        self.fields["expense"].disabled = True



class ExpenseSalaryForm(BaseForm,forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ("amount","type",'expense','date','description','employee')
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super(ExpenseSalaryForm, self).__init__(*args, **kwargs)
        initial = kwargs.pop('initial')
        print(initial)
        self.fields["expense"].disabled = True
        self.fields["expense"].initial = initial['expense']


class ExpenseCaseForm(BaseForm,forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ("amount","type",'expense','date','description','case')
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super(ExpenseCaseForm, self).__init__(*args, **kwargs)
        initial = kwargs.pop('initial')
        self.fields["case"].queryset = Case.objects.all().order_by('-created_at')
        self.fields["expense"].initial = initial['expense']
        self.fields["expense"].disabled = True


class ExpenseCaseFormOne(BaseForm,forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ("amount","type",'expense','date','description','case')
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super(ExpenseCaseFormOne, self).__init__(*args, **kwargs)
        initial = kwargs.pop('initial')
        self.fields["expense"].queryset = Expense.objects.exclude(office__isnull=False).exclude(tax__isnull=False).exclude(other__isnull=False).order_by('-created_at')
        self.fields["case"].initial = initial['case']
        self.fields["case"].disabled = True
