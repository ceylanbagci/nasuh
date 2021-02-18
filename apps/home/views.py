from django.shortcuts import render
from django.db.models import Q
import django.db.models
from case.models import Case,Client,Partner
from office.models import Employee
from expense.models import Expense
from transactions.models import Transaction
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request,'home/index.html',locals())


@login_required
def search(request):
    print(request.POST)
    print(request.POST['search'])
    search_models = [Case,Transaction,Client,Employee,Expense,Partner]  # Add your models here, in any way you find best.
    search_results = []
    for model in search_models:
        fields = [x for x in model._meta.fields if isinstance(x, django.db.models.CharField)]
        search_queries = [Q(**{x.name + "__contains": request.POST['search']}) for x in fields]
        q_object = Q()
        for query in search_queries:
            q_object = q_object | query

        results = model.objects.filter(q_object)
        search_results.append(results)
    print('+'*30)
    print(search_results)
    print(len(search_results))
    return render(request,'home/search-results.html',locals())