from django.shortcuts import render,redirect
from .forms import*
from django.contrib import messages
import core.custom_messages as custom_messages
import core.helper as hlp
from django.http import JsonResponse
from .filters import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.

def view_case(request,slug):
    case = hlp.get_or_none(Case, slug=slug)
    return render(request, 'case/view_case.html',locals())

def case_list(request):
    customer_filter = CaseFilter(request.GET,queryset=Case.objects.all())
    paginator = Paginator(customer_filter.qs, 10)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    return render(request, 'case/case_list.html', {"results": response, "filter": customer_filter,
                                                         "next_page_params": "&" + request.GET.urlencode().replace(
                                                             "page=",
                                                             "empty_param=")})


def create(request):
    if request.method == "POST":
        form = CaseForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, custom_messages.CREATE_SUCCESS)
            return redirect("/case/%s/view_case"%instance.slug)
        else:
            messages.error(request, custom_messages.CREATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = CaseForm()
    return render(request, 'case/new.html',{"form": form})


def update(request,slug):
    instance = hlp.get_or_none(Case, slug=slug)
    if request.method == "POST":
        form = CaseForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, custom_messages.UPDATE_SUCCESS)
            return redirect("/case/%s/view_case" % instance.slug)
        else:
            messages.error(request, custom_messages.UPDATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = CaseForm(instance=instance)
    return render(request, 'case/new.html',{"form": form,"instance": instance})


def delete(request,slug):
    coming_url = request.META.get("HTTP_REFERER")
    try:
        hlp.delete_object(Case, slug=slug)
        messages.success(request, custom_messages.DELETE_SUCCESS)
    except Exception as e:
        messages.error(request, custom_messages.DELETE_ERROR)
    return redirect(coming_url)


def view_client(request,slug):
    client = hlp.get_or_none(Client, slug=slug)
    return render(request, 'case/view_client.html',locals())


def client_list(request):
    customer_filter = ClientFilter(request.GET,queryset=Client.objects.all())
    paginator = Paginator(customer_filter.qs, 10)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    return render(request, 'case/client_list.html', {"results": response, "filter": customer_filter,
                                                         "next_page_params": "&" + request.GET.urlencode().replace(
                                                             "page=",
                                                             "empty_param=")})

def create_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, custom_messages.CREATE_SUCCESS)
            return redirect("/case/%s/view_client" % instance.slug)
        else:
            messages.error(request, custom_messages.CREATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = ClientForm()
    return render(request, 'case/new_client.html',{"form": form})


def update_client(request,slug):
    instance = hlp.get_or_none(Client, slug=slug)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, custom_messages.UPDATE_SUCCESS)
            return redirect("/case/%s/view_client" % instance.slug)
        else:
            messages.error(request, custom_messages.UPDATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = ClientForm(instance=instance)
    return render(request, 'case/new_client.html',{"form": form,"instance": instance})


def delete_client(request,slug):
    coming_url = request.META.get("HTTP_REFERER")
    try:
        hlp.delete_object(Client, slug=slug)
        messages.success(request, custom_messages.DELETE_SUCCESS)
    except Exception as e:
        messages.error(request, custom_messages.DELETE_ERROR)
    return redirect(coming_url)


def view_partner(request,slug):

    partner = hlp.get_or_none(Partner, slug=slug)
    return render(request, 'case/view_partner.html',locals())

def partner_list(request):
    partner_filter = PartnerFilter(request.GET,queryset=Partner.objects.all())
    paginator = Paginator(partner_filter.qs, 10)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    return render(request, 'case/partner_list.html', {"results": response, "filter": partner_filter,
                                                         "next_page_params": "&" + request.GET.urlencode().replace(
                                                             "page=",
                                                             "empty_param=")})


def create_partner(request):
    if request.method == "POST":
        form = PartnerForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, custom_messages.CREATE_SUCCESS)
            return redirect("/case/%s/view_partner" % instance.slug)
        else:
            messages.error(request, custom_messages.CREATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = PartnerForm()
    return render(request, 'case/new_partner.html',{"form": form})


def update_partner(request,slug):
    instance = hlp.get_or_none(Partner, slug=slug)
    if request.method == "POST":
        form = PartnerForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("/case/%s/view_partner" % instance.slug)
            messages.success(request, custom_messages.UPDATE_SUCCESS)
        else:
            messages.error(request, custom_messages.UPDATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = PartnerForm(instance=instance)
    return render(request, 'case/new_partner.html',{"form": form,"instance": instance})


def delete_partner(request,slug):
    coming_url = request.META.get("HTTP_REFERER")
    try:
        hlp.delete_object(Partner, slug=slug)
        messages.success(request, custom_messages.DELETE_SUCCESS)
    except Exception as e:
        messages.error(request, custom_messages.DELETE_ERROR)
    return redirect(coming_url)

def create_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, custom_messages.CREATE_SUCCESS)
            return redirect('/case/create_expense')
        else:
            messages.error(request, custom_messages.CREATE_ERROR)
            print(form)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = ExpenseForm()
    return render(request, 'case/new_expense.html',{"form": form})


def update_expense(request,slug):
    instance = hlp.get_or_none(Expense, slug=slug)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, custom_messages.UPDATE_SUCCESS)
        else:
            messages.error(request, custom_messages.UPDATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = ExpenseForm(instance=instance)
    return render(request, 'case/new_expense.html',{"form": form,"instance": instance})


def delete_expense(request,slug):
    coming_url = request.META.get("HTTP_REFERER")
    try:
        hlp.delete_object(Expense, slug=slug)
        messages.success(request, custom_messages.DELETE_SUCCESS)
    except Exception as e:
        messages.error(request, custom_messages.DELETE_ERROR)
    return redirect(coming_url)

def expense_list(request):
    results = Expense.objects.all()
    return render(request, 'case/expense_list.html',locals())