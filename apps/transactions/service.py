from .models import *
import core.helper as hlp
from django.db.models import Sum, Q, Count
import datetime
from django.db.models.functions import TruncMonth,TruncDay
from datetime import date
from django.db.models import F, Func, Value, CharField
from office.models import Employee
import locale

def get_stats_expense(**kwargs):
    instance = kwargs.pop('instance')
    stats = {}
    qs = Transaction.objects.filter(expense=instance)
    stats["total_income"] = qs.aggregate(sum=Sum('amount', filter=Q(type=Transaction.INCOME)))
    stats["total_spent"] = qs.aggregate(sum=Sum('amount', filter=Q(type=Transaction.SPENT)))
    if stats["total_income"]['sum'] == None:
        stats["total_income"]['sum'] = 0
    if stats["total_spent"]['sum'] == None:
        stats["total_spent"]['sum'] = 0
    stats["get_difference"] = stats["total_income"]['sum'] + stats["total_spent"]['sum']
    stats["total"] = qs.count()
    return stats

def get_stats_employee(**kwargs):
    instance = kwargs.pop('instance')
    stats = {}
    qs = Transaction.objects.filter(employee=instance)
    stats["total_income"] = qs.aggregate(sum=Sum('amount', filter=Q(type=Transaction.INCOME)))
    stats["total_spent"] = qs.aggregate(sum=Sum('amount', filter=Q(type=Transaction.SPENT)))
    if stats["total_income"]['sum'] == None:
        stats["total_income"]['sum'] = 0
    if stats["total_spent"]['sum'] == None:
        stats["total_spent"]['sum'] = 0
    stats["get_difference"] = stats["total_income"]['sum'] + stats["total_spent"]['sum']
    stats["total"] = qs.count()
    return stats

def get_stats_case(**kwargs):
    instance = kwargs.pop('instance')
    stats = {}
    stats["total_income"] = instance.transactions.aggregate(sum=Sum('amount', filter=Q(type=Transaction.INCOME)))
    stats["total_spent"] = instance.transactions.aggregate(sum=Sum('amount', filter=Q(type=Transaction.SPENT)))
    if stats["total_income"]['sum'] == None:
        stats["total_income"]['sum'] = 0
    if stats["total_spent"]['sum'] == None:
        stats["total_spent"]['sum'] = 0
    stats["get_difference"] = stats["total_income"]['sum'] + stats["total_spent"]['sum']
    stats["total"] = len(instance.transactions.all())
    return stats

def get_stats_client(**kwargs):
    instance = kwargs.pop('instance')
    stats = {}
    qs = Transaction.objects.filter(case__client=instance)
    stats["total_income"] = qs.aggregate(sum=Sum('amount', filter=Q(type=Transaction.INCOME)))
    stats["total_spent"] = qs.aggregate(sum=Sum('amount', filter=Q(type=Transaction.SPENT)))
    if stats["total_income"]['sum'] == None:
        stats["total_income"]['sum'] = 0
    if stats["total_spent"]['sum'] == None:
        stats["total_spent"]['sum'] = 0
    stats["get_difference"] = stats["total_income"]['sum'] + stats["total_spent"]['sum']
    stats["total"] = qs.count()
    return stats

def get_stats_partner(**kwargs):
    instance = kwargs.pop('instance')
    stats = {}
    qs = Transaction.objects.filter(case__partner=instance)
    stats["total_income"] = qs.aggregate(sum=Sum('amount', filter=Q(type=Transaction.INCOME)))
    stats["total_spent"] = qs.aggregate(sum=Sum('amount', filter=Q(type=Transaction.SPENT)))
    if stats["total_income"]['sum'] == None:
        stats["total_income"]['sum'] = 0
    if stats["total_spent"]['sum'] == None:
        stats["total_spent"]['sum'] = 0
    stats["get_difference"] = stats["total_income"]['sum'] + stats["total_spent"]['sum']
    stats["total"] = qs.count()
    return stats

def get_stats_office(**kwargs):
    instance = kwargs.pop('instance')
    stats = {}
    temp = 0
    for expense in instance.expenses.all():
        temp_sum = expense.transactions.aggregate(sum=Sum('amount', filter=Q(type=Transaction.INCOME)))
        if not temp_sum['sum']:
            temp_sum['sum']=0
        temp += temp_sum['sum']
    stats["total_income"] = temp
    temp = 0

    for expense in instance.expenses.all():
        temp_sum = expense.transactions.aggregate(sum=Sum('amount', filter=Q(type=Transaction.SPENT)))
        if not temp_sum['sum']:
            temp_sum['sum'] = 0
        temp += temp_sum['sum']
    stats["total_spent"] = temp


    if stats["total_income"] == None:
        stats["total_income"] = 0
    if stats["total_spent"] == None:
        stats["total_spent"] = 0

    stats["get_difference"] = stats["total_income"] + stats["total_spent"]

    total = 0
    for expense in instance.expenses.all():
        for trans in expense.transactions.all():
            total += 1

    stats['total_employee'] = Employee.objects.all().count()
    stats["total"] = total
    print(stats)
    return stats

def get_stats_tax(**kwargs):
    instance = kwargs.pop('instance')
    stats = {}
    temp = 0
    for expense in instance.expenses.all():
        temp_sum = expense.transactions.aggregate(sum=Sum('amount', filter=Q(type=Transaction.INCOME)))
        if not temp_sum['sum']:
            temp_sum['sum']=0
        temp += temp_sum['sum']
    stats["total_income"] = temp
    temp = 0

    for expense in instance.expenses.all():
        temp_sum = expense.transactions.aggregate(sum=Sum('amount', filter=Q(type=Transaction.SPENT)))
        if not temp_sum['sum']:
            temp_sum['sum'] = 0
        temp += temp_sum['sum']
    stats["total_spent"] = temp


    if stats["total_income"] == None:
        stats["total_income"] = 0
    if stats["total_spent"] == None:
        stats["total_spent"] = 0

    stats["get_difference"] = stats["total_income"] + stats["total_spent"]

    total = 0
    for expense in instance.expenses.all():
        for trans in expense.transactions.all():
            total += 1

    stats['total_employee'] = Employee.objects.all().count()
    stats["total"] = total
    print(stats)
    return stats

def get_stats_other(**kwargs):
    instance = kwargs.pop('instance')
    stats = {}
    temp = 0
    for expense in instance.expenses.all():
        temp_sum = expense.transactions.aggregate(sum=Sum('amount', filter=Q(type=Transaction.INCOME)))
        if not temp_sum['sum']:
            temp_sum['sum']=0
        temp += temp_sum['sum']
    stats["total_income"] = temp
    temp = 0

    for expense in instance.expenses.all():
        temp_sum = expense.transactions.aggregate(sum=Sum('amount', filter=Q(type=Transaction.SPENT)))
        if not temp_sum['sum']:
            temp_sum['sum'] = 0
        temp += temp_sum['sum']
    stats["total_spent"] = temp


    if stats["total_income"] == None:
        stats["total_income"] = 0
    if stats["total_spent"] == None:
        stats["total_spent"] = 0

    stats["get_difference"] = stats["total_income"] + stats["total_spent"]

    total = 0
    for expense in instance.expenses.all():
        for trans in expense.transactions.all():
            total += 1

    stats['total_employee'] = Employee.objects.all().count()
    stats["total"] = total
    print(stats)
    return stats

def end_of_the_day(**kwargs):
    date = kwargs.pop('date')
    results={}
    results['qs'] = Transaction.objects.filter(date=date).order_by('date')
    results['title'] = 'Gün Sonu'
    results['date'] = date.strftime('%d.%m.%Y')
    results['income'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.INCOME)))
    results['spent'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.SPENT)))
    print(result)
    return results

def end_of_the_month(**kwargs):
    locale.setlocale(locale.LC_TIME, "tr_TR")
    date = kwargs.pop('date')
    results = {}
    results['qs'] = Transaction.objects.filter(date__month=date.month).order_by('date')
    results['title'] = 'Ay Sonu'
    results['date'] = date.strftime('%B %Y')
    results['income'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.INCOME)))
    results['spent'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.SPENT)))
    return results

def end_of_the_year(**kwargs):
    locale.setlocale(locale.LC_TIME, "tr_TR")
    date = kwargs.pop('date')
    results = {}
    results['qs'] = Transaction.objects.filter(date__year=date.year).order_by('date')
    results['title'] = 'Yıl Sonu'
    results['date'] = date.strftime('%Y')
    results['income'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.INCOME)))
    results['spent'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.SPENT)))
    return results

def get_case_list_report(**kwargs):
    import case.models as case_models
    results = {}
    results['qs'] = hlp.get_list(case_models.Case,).order_by('-date')
    results['title'] = 'Dava Listesi '
    results['date'] = datetime.date.today().strftime('%d.%m.%Y')
    results['total'] = results['qs'].count()
    return results

def get_client_list_report(**kwargs):
    import case.models as case_models
    results = {}
    results['qs'] = hlp.get_list(case_models.Client,).order_by('first_name')
    results['title'] = 'Müvekkil Listesi '
    results['date'] = datetime.date.today().strftime('%d.%m.%Y')
    results['total'] = results['qs'].count()
    return results

def get_partner_list_report(**kwargs):
    import case.models as case_models
    results = {}
    results['qs'] = hlp.get_list(case_models.Partner,).order_by('first_name')
    results['title'] = 'Ortak Listesi '
    results['date'] = datetime.date.today().strftime('%d.%m.%Y')
    results['total'] = results['qs'].count()
    return results

def get_employee_list_report(**kwargs):
    from office.models import Employee
    results = {}
    results['qs'] = hlp.get_list(Employee).order_by('first_name')
    results['title'] = 'Çalışan Listesi '
    results['date'] = datetime.date.today().strftime('%d.%m.%Y')
    results['total'] = results['qs'].count()
    return results

def get_case_report(**kwargs):
    instance = kwargs.pop('instance')
    results = {}
    results['qs'] = instance.transactions.all().order_by('-date')
    results['title'] = instance.title + ' Dosyasına Ait Hesap Hareketleri'
    results['date'] = datetime.date.today().strftime('%d.%m.%Y')
    results['income'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.INCOME)))
    results['spent'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.SPENT)))
    return results

def get_client_report(**kwargs):
    instance = kwargs.pop('instance')
    results = {}
    results['qs'] = Transaction.objects.filter(case__client=instance).order_by('-date')
    results['title'] = instance.full_name + ' Hesap Hareketleri'
    results['date'] = datetime.date.today().strftime('%d.%m.%Y')
    results['income'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.INCOME)))
    results['spent'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.SPENT)))
    return results

def get_partner_report(**kwargs):
    instance = kwargs.pop('instance')
    results = {}
    results['qs'] = Transaction.objects.filter(case__partner=instance).order_by('-date')
    results['title'] = instance.full_name + ' Hesap Hareketleri'
    results['date'] = datetime.date.today().strftime('%d.%m.%Y')
    results['income'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.INCOME)))
    results['spent'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.SPENT)))
    return results

def get_employee_report(**kwargs):
    instance = kwargs.pop('instance')
    results = {}
    results['qs'] = Transaction.objects.filter(employee=instance).order_by('-date')
    results['title'] = instance.full_name + ' Hesap Hareketleri'
    results['date'] = datetime.date.today().strftime('%d.%m.%Y')
    results['income'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.INCOME)))
    results['spent'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.SPENT)))
    return results

def get_single_expense_report(**kwargs):
    instance = kwargs.pop('instance')
    results = {}
    results['qs'] = Transaction.objects.filter(expense=instance).order_by('-date')
    results['title'] = instance.title + ' Hesap Hareketleri'
    results['date'] = datetime.date.today().strftime('%d.%m.%Y')
    results['income'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.INCOME)))
    results['spent'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.SPENT)))
    return results

def get_expense_report(**kwargs):
    object = kwargs.pop('object')
    results = {}
    if object == 'case':
        results['qs'] = Transaction.objects.filter(case__isnull=False).order_by('-date')
        results['title'] = 'Dava Dosyalarına Ait Hesap Hareketleri'
    elif object == 'office':
        results['qs'] = Transaction.objects.filter(expense__office__isnull=False).order_by('-date')
        results['title'] = 'Ofise Ait Hesap Hareketleri'
    elif object == 'tax':
        results['qs'] = Transaction.objects.filter(expense__tax__isnull=False).order_by('-date')
        results['title'] = 'Vergiye Ait Hesap Hareketleri'
    elif object == 'other':
        results['qs'] = Transaction.objects.filter(expense__other__isnull=False).order_by('-date')
        results['title'] = 'Diğer Harcamalara Ait Hesap Hareketleri'
    elif object == 'expense':
        results['qs'] = Transaction.objects.filter(expense__isnull=False).order_by('-date')
        results['title'] = 'Tüm Harcamalara Ait Hesap Hareketleri'
    results['date'] = datetime.date.today().strftime('%d.%m.%Y')
    results['income'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.INCOME)))
    results['spent'] = results['qs'].aggregate(sum=Sum('amount', filter=Q(type=Transaction.SPENT)))
    print(results['qs'].count())
    print('+'*30)
    return results

