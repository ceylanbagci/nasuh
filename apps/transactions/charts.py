from .models import Transaction
from case.models import Case,Client,Partner
from expense.models import Expense
from office.models import Office,Employee
from tax.models import Tax
from other.models import Other
import core.helper as hlp
from itertools import chain

def get_chart_case(slug):
    case = Case.objects.get(slug=slug)
    transactions = hlp.get_list(Transaction, case=case).values('amount','type','date').order_by('-date')[:7]
    return list(transactions)

def get_chart_client(slug):
    client = Client.objects.get(slug=slug)
    transactions = hlp.get_list(Transaction, case__client=client).values('amount','type','date').order_by('-date')[:7]
    return list(transactions)

def get_chart_partner(slug):
    partner = Partner.objects.get(slug=slug)
    transactions = hlp.get_list(Transaction, case__partner=partner).values('amount','type','date').order_by('-date')[:7]
    return list(transactions)

def get_chart_expense(slug):
    expense = Expense.objects.get(slug=slug)
    transactions = hlp.get_list(Transaction, expense=expense).values('amount','type','date').order_by('-date')[:7]
    return list(transactions)

def get_chart_office(slug):
    office = Office.objects.get(slug=slug)
    transactions = hlp.get_list(Transaction, expense__office=office).values('amount','type','date').order_by('-date')[:7]
    return list(transactions)

def get_chart_tax(slug):
    tax = Tax.objects.get(slug=slug)
    transactions = hlp.get_list(Transaction, expense__tax=tax).values('amount','type','date').order_by('-date')[:7]
    return list(transactions)

def get_chart_other(slug):
    other = Other.objects.get(slug=slug)
    transactions = hlp.get_list(Transaction, expense__other=other).values('amount','type','date').order_by('-date')[:7]
    return list(transactions)

def get_chart_employee(slug):
    employee = Employee.objects.get(slug=slug)
    transactions = hlp.get_list(Transaction, employee=employee).values('amount','type','date').order_by('-date')[:7]
    return list(transactions)
