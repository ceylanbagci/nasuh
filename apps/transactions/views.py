from django.shortcuts import render,redirect
from .forms import*
from django.contrib import messages
import core.custom_messages as custom_messages
import core.helper as hlp
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from expense.models import Expense
from office.models import Employee
from case.models import Case
from django.http import JsonResponse, HttpResponse
import transactions.charts as charts
from django.contrib.auth.decorators import login_required

@login_required
def new(request,slug):
    instance = hlp.get_or_none(Expense, slug=slug)
    if request.method=="POST":
        form = TransactionForm(request.POST,initial={'instance':instance})
        if form.is_valid():
            form.save()
            messages.success(request,custom_messages.CREATE_SUCCESS)
            return redirect('/expense/%s/view_expense'% instance.id)
        else:
            messages.error(request,custom_messages.CREATE_ERROR)
    else:
        form = TransactionForm(initial={'instance':instance})
    return render(request,'transactions/new.html',locals())

@login_required
def delete(request,id):
    coming_url = request.META.get("HTTP_REFERER")
    try:
        hlp.delete_object(Transaction, id=id)
        messages.success(request, custom_messages.DELETE_SUCCESS)
    except Exception as e:
        messages.error(request, custom_messages.DELETE_ERROR)
    return redirect(coming_url)

@login_required
def salary(request,slug):
    instance = hlp.get_or_none(Employee, slug=slug)
    expense = hlp.get_or_none(Expense, title='Maaş')
    if request.method == "POST":
        form = SalaryForm(request.POST, initial={'expense':expense,'employee':instance})
        if form.is_valid():
            form.save()
            messages.success(request, custom_messages.UPDATE_SUCCESS)
            return redirect("/office/%s/view_employee" % instance.slug)
        else:
            messages.error(request, custom_messages.UPDATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = SalaryForm(initial={'expense':expense,'employee':instance})
    return render(request, 'transactions/new_salary.html',{"form": form,"instance": instance})

@login_required
def expense_salary(request):
    expense = hlp.get_or_none(Expense, title='Maaş')
    if request.method == "POST":
        form = ExpenseSalaryForm(request.POST, initial={'expense':expense})
        if form.is_valid():
            form.save()
            messages.success(request, custom_messages.UPDATE_SUCCESS)
            return redirect("/expense/%s/view_expense" % expense.id)
        else:
            messages.error(request, custom_messages.UPDATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = ExpenseSalaryForm(initial={'expense':expense})
    return render(request, 'transactions/new_salary.html',{"form": form,"instance": expense})

@login_required
def case_expense_one(request,slug):
    instance = hlp.get_or_none(Case, slug=slug)
    if request.method == "POST":
        form = ExpenseCaseFormOne(request.POST, initial={'case':instance})
        if form.is_valid():
            form.save()
            messages.success(request, custom_messages.UPDATE_SUCCESS)
            return redirect("/case/%s/view_case" % instance.slug)
        else:
            messages.error(request, custom_messages.UPDATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = ExpenseCaseFormOne(initial={'case':instance})
    return render(request, 'transactions/new_case_expense.html',{"form": form,"instance": instance})

@login_required
def case_expense(request,slug):
    instance = hlp.get_or_none(Expense, slug=slug)
    if request.method == "POST":
        form = ExpenseCaseForm(request.POST, initial={'expense':instance})
        if form.is_valid():
            trans = form.save()
            messages.success(request, custom_messages.UPDATE_SUCCESS)
            return redirect("/expense/%s/view_expense" % trans.expense.id)
        else:
            messages.error(request, custom_messages.UPDATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = ExpenseCaseForm(initial={'expense':instance})
    return render(request, 'transactions/new_case_expense.html',{"form": form,"instance": instance})

@login_required
def get_chart_case(request,slug):
    return JsonResponse( {'data':charts.get_chart_case(slug=slug)},safe=False)

@login_required
def get_chart_client(request,slug):
    return JsonResponse( {'data':charts.get_chart_client(slug=slug)},safe=False)

@login_required
def get_chart_partner(request,slug):
    return JsonResponse( {'data':charts.get_chart_partner(slug=slug)},safe=False)

@login_required
def get_chart_expense(request,slug):
    return JsonResponse( {'data':charts.get_chart_expense(slug=slug)},safe=False)

@login_required
def get_chart_office(request,slug):
    return JsonResponse( {'data':charts.get_chart_office(slug=slug)},safe=False)

@login_required
def get_chart_tax(request,slug):
    return JsonResponse( {'data':charts.get_chart_tax(slug=slug)},safe=False)

@login_required
def get_chart_other(request,slug):
    return JsonResponse( {'data':charts.get_chart_other(slug=slug)},safe=False)

@login_required
def get_chart_employee(request,slug):
    return JsonResponse( {'data':charts.get_chart_employee(slug=slug)},safe=False)

