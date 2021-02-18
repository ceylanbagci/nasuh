from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import*
from django.contrib import messages
import core.custom_messages as custom_messages
import core.helper as hlp
from django.http import JsonResponse
# from .filters import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from office.models import Office
from django.contrib.auth.decorators import login_required

@login_required
def view_expense(request,id=1):
    expense = hlp.get_or_none(Expense, id=id)
    transactions = expense.transactions.all().order_by('-date')
    paginator = Paginator(transactions, 10)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    return render(request, 'expense/view_expense.html', {"results": response, "expense": expense,
                                                         "next_page_params": "&" + request.GET.urlencode().replace(
                                                             "page=","empty_param=")})

@login_required
def create(request):
    coming_url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, custom_messages.CREATE_SUCCESS)
            return redirect("/expense/%s/view_expense"%instance.id)
        else:
            messages.error(request, custom_messages.CREATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = ExpenseForm(url={'coming_url':coming_url})
    return render(request, 'expense/new.html',{"form": form})

@login_required
def update(request,slug):
    instance = hlp.get_or_none(Expense, slug=slug)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, custom_messages.UPDATE_SUCCESS)
            return redirect("/expense/%s/view_expense" % instance.id)
        else:
            messages.error(request, custom_messages.UPDATE_ERROR)
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = ExpenseForm(instance=instance)
    return render(request, 'expense/new.html',{"form": form,"instance": instance})

@login_required
def delete(request,slug):
    instance = Expense.objects.get(slug=slug)
    try:
        hlp.delete_object(Expense, slug=slug)
        messages.success(request, custom_messages.DELETE_SUCCESS)
        if instance.office is not None:
            return redirect('/office/expense_list')
        elif instance.tax is not None:
            return redirect('/tax/expense_list')
        elif instance.other is not None:
            return redirect('/other/expense_list')
    except Exception as e:
        messages.error(request, custom_messages.DELETE_ERROR)
    return redirect('/case/expense_list')

@login_required
def expense_list_all(request):
    results = Expense.objects.all()
    return render(request, 'expense/expense_list.html',locals())