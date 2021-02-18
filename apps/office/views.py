from django.shortcuts import render,redirect
from .forms import*
from django.contrib import messages
import core.custom_messages as custom_messages
import core.helper as hlp
from django.http import JsonResponse
# from .filters import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from expense.models import Expense
from django.contrib.auth.decorators import login_required


@login_required
def view_office(request,id=1):
    office = hlp.get_or_none(Office, id=id)
    transactions = []
    for expense in office.expenses.all():
        for trans in expense.transactions.all():
            transactions.append(trans)
    paginator = Paginator(transactions, 10)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    return render(request, 'office/view_office.html', {"results": response, "office": office,
                                                   "next_page_params": "&" + request.GET.urlencode().replace(
                                                       "page=", "empty_param=")})


@login_required
def create(request):
    if request.method == "POST":
        form = OfficeForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, custom_messages.CREATE_SUCCESS)
            return redirect("/office/%s/view_office"%instance.id)
        else:
            messages.error(request, custom_messages.CREATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = OfficeForm()
    return render(request, 'office/new.html',{"form": form})

@login_required
def update(request,slug):
    instance = hlp.get_or_none(Office, slug=slug)
    if request.method == "POST":
        form = OfficeForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, custom_messages.UPDATE_SUCCESS)
            return redirect("/office/%s/view_office" % instance.id)
        else:
            messages.error(request, custom_messages.UPDATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = OfficeForm(instance=instance)
    return render(request, 'office/new.html',{"form": form,"instance": instance})

@login_required
def delete(request,slug):
    coming_url = request.META.get("HTTP_REFERER")
    try:
        hlp.delete_object(Office, slug=slug)
        messages.success(request, custom_messages.DELETE_SUCCESS)
    except Exception as e:
        messages.error(request, custom_messages.DELETE_ERROR)
    return redirect(coming_url)

@login_required
def view_employee(request,slug):
    employee = hlp.get_or_none(Employee, slug=slug)
    transactions = employee.transactions.all().order_by('-date')
    paginator = Paginator(transactions, 10)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    return render(request, 'office/view_employee.html', {"results": response, "employee": employee,
                                                         "next_page_params": "&" + request.GET.urlencode().replace(
                                                             "page=", "empty_param=")})

@login_required
def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, custom_messages.CREATE_SUCCESS)
            return redirect("/office/%s/view_employee"%instance.slug)
        else:
            messages.error(request, custom_messages.CREATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = EmployeeForm()
    return render(request, 'office/new_employee.html',{"form": form})

@login_required
def update_employee(request,slug):
    instance = hlp.get_or_none(Employee, slug=slug)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, custom_messages.UPDATE_SUCCESS)
            return redirect("/office/%s/view_employee" % instance.slug)
        else:
            messages.error(request, custom_messages.UPDATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = EmployeeForm(instance=instance)
    return render(request, 'office/new_employee.html',{"form": form,"instance": instance})

@login_required
def delete_employee(request,slug):
    coming_url = request.META.get("HTTP_REFERER")
    try:
        hlp.delete_object(Employee, slug=slug)
        messages.success(request, custom_messages.DELETE_SUCCESS)
    except Exception as e:
        messages.error(request, custom_messages.DELETE_ERROR)
    return redirect(coming_url)

@login_required
def employee_list(request):
    employee_filter = Employee.objects.all()
    paginator = Paginator(employee_filter, 10)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    return render(request, 'office/employee_list.html', {"results": response, "filter": employee_filter,
                                                         "next_page_params": "&" + request.GET.urlencode().replace(
                                                             "page=",
                                                             "empty_param=")})

@login_required
def expense_list(request):
    results = Expense.objects.filter(office__id=1)
    return render(request, 'expense/expense_list.html',locals())
