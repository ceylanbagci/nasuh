from django.shortcuts import render,redirect
from .forms import*
from django.contrib import messages
import core.custom_messages as custom_messages
import core.helper as hlp
from django.http import JsonResponse
from .filters import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from expense.models import Expense
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def view_case(request,slug):
    case = hlp.get_or_none(Case, slug=slug)
    # from faker import Faker
    # from transactions.models import Transaction
    # fake = Faker()
    # for i in range(11):
    #     trans = Transaction()
    #     trans.expense = Expense.objects.get(id=1)
    #     trans.case = case
    #     trans.amount = 350
    #     trans.save()

    transactions = case.transactions.all().order_by('-date')
    paginator = Paginator(transactions, 10)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    return render(request, 'case/view_case.html', {"results": response, "case": case,
                                                         "next_page_params": "&" + request.GET.urlencode().replace(
                                                             "page=", "empty_param=")})

@login_required
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

@login_required
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

@login_required
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

@login_required
def delete(request,slug):
    coming_url = request.META.get("HTTP_REFERER")
    try:
        hlp.delete_object(Case, slug=slug)
        messages.success(request, custom_messages.DELETE_SUCCESS)
    except Exception as e:
        messages.error(request, custom_messages.DELETE_ERROR)
    return redirect(coming_url)

@login_required
def view_client(request,slug):
    client = hlp.get_or_none(Client, slug=slug)
    transactions = []
    for case in client.cases.all():
        for trans in case.transactions.all():
            transactions.append(trans)
    paginator = Paginator(transactions, 10)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    return render(request, 'case/view_client.html', {"results": response, "client": client,
                                                   "next_page_params": "&" + request.GET.urlencode().replace(
                                                       "page=", "empty_param=")})


@login_required
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
@login_required
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

@login_required
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

@login_required
def delete_client(request,slug):
    coming_url = request.META.get("HTTP_REFERER")
    try:
        hlp.delete_object(Client, slug=slug)
        messages.success(request, custom_messages.DELETE_SUCCESS)
    except Exception as e:
        messages.error(request, custom_messages.DELETE_ERROR)
    return redirect(coming_url)

@login_required
def view_partner(request,slug):
    partner = hlp.get_or_none(Partner, slug=slug)
    case_list = partner.cases.all()
    transactions = []
    for case in partner.cases.all():
        for trans in case.transactions.all():
            transactions.append(trans)
    paginator = Paginator(transactions, 10)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    return render(request, 'case/view_partner.html', {"results": response, "partner": partner, "case_list": case_list,
                                                     "next_page_params": "&" + request.GET.urlencode().replace(
                                                         "page=", "empty_param=")})


@login_required
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

@login_required
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

@login_required
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

@login_required
def determine_share(request,partner,case):
    partner = hlp.get_or_none(Partner, slug=partner)
    case = hlp.get_or_none(Case, slug=case)
    if request.method == "POST":
        form = ShareForm(request.POST, initial={'partner':partner,'case':case,})
        if form.is_valid():
            form.save()
            messages.success(request, custom_messages.CREATE_SUCCESS)
            if partner:
                return redirect("/case/%s/view_partner" % partner.slug)
            else:
                return redirect("/case/%s/view_case" % case.slug)

        else:
            error = form.errors['__all__'].as_data()
            for e in error:
                messages.error(request, e.message)

    else:
        form = ShareForm(initial={'partner':partner,'case':case ,})
    return render(request, 'case/new_share.html',locals())

@login_required
def delete_partner(request,slug):
    coming_url = request.META.get("HTTP_REFERER")
    try:
        hlp.delete_object(Partner, slug=slug)
        messages.success(request, custom_messages.DELETE_SUCCESS)
    except Exception as e:
        messages.error(request, custom_messages.DELETE_ERROR)
    return redirect(coming_url)

@login_required
def partnership_delete(request,id):
    coming_url = request.META.get("HTTP_REFERER")
    try:
        hlp.delete_object(Partnership, id=id)
        messages.success(request, custom_messages.DELETE_SUCCESS)
    except Exception as e:
        messages.error(request, custom_messages.DELETE_ERROR)
    return redirect(coming_url)


@login_required
def expense_list(request):
    results = Expense.objects.exclude(other__id=1).exclude(tax__id=1).exclude(office__id=1)
    return render(request, 'expense/expense_list.html',locals())