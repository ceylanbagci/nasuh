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
def view_other(request,id=1):
    other = hlp.get_or_none(Other, id=id)
    transactions = []
    for expense in other.expenses.all():
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

    return render(request, 'other/view_other.html', {"results": response, "other": other,
                                                 "next_page_params": "&" + request.GET.urlencode().replace(
                                                     "page=", "empty_param=")})

@login_required
def create(request):
    if request.method == "POST":
        form = OtherForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, custom_messages.CREATE_SUCCESS)
            return redirect("/other/%s/view_other"%instance.id)
        else:
            messages.error(request, custom_messages.CREATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = OtherForm()
    return render(request, 'other/new.html',{"form": form})

@login_required
def update(request,slug):
    instance = hlp.get_or_none(Other, slug=slug)
    if request.method == "POST":
        form = OtherForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, custom_messages.UPDATE_SUCCESS)
            return redirect("/other/%s/view_other" % instance.id)
        else:
            messages.error(request, custom_messages.UPDATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = OtherForm(instance=instance)
    return render(request, 'other/new.html',{"form": form,"instance": instance})

@login_required
def delete(request,slug):
    coming_url = request.META.get("HTTP_REFERER")
    try:
        hlp.delete_object(Other, slug=slug)
        messages.success(request, custom_messages.DELETE_SUCCESS)
    except Exception as e:
        messages.error(request, custom_messages.DELETE_ERROR)
    return redirect(coming_url)

@login_required
def expense_list(request):
    results = Expense.objects.filter(other__id=1)
    return render(request, 'expense/expense_list.html',locals())


