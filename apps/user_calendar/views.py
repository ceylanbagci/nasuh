from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import core.custom_messages as custom_messages
from .forms import *
import core.helper as hlp
from django.http import HttpResponse, JsonResponse
import json
import datetime
# Create your views here.
def calendar(request):
    return render(request,'user_calendar/calendar.html')


@login_required
def new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request,custom_messages.CREATE_SUCCESS)
            return redirect("/user_calendar/%s/update" % instance.slug)
        else:
            messages.error(request, custom_messages.CREATE_ERROR)

    else:
        form = EventForm()
    return render(request,'user_calendar/new.html',locals())

@login_required
def update(request,slug):
    instance = Event.objects.get(slug=slug)
    if request.method == "POST":
        form = EventForm(request.POST,instance=instance)
        if form.is_valid():
            print('1'*30)
            print(form.cleaned_data['backgroundColor'])
            k = form.save()
            print(k.backgroundColor)
            messages.success(request,custom_messages.UPDATE_SUCCESS)
            return redirect("/user_calendar/%s/update" % instance.slug)
        else:
            messages.error(request, custom_messages.UPDATE_ERROR)

    else:
        form = EventForm(instance=instance)
    return render(request,'user_calendar/new.html',locals())


@login_required
def delete(request,slug):
    coming_url = request.META.get("HTTP_REFERER")
    try:
        hlp.delete_object(Event, slug=slug)
        messages.success(request, custom_messages.DELETE_SUCCESS)
    except Exception as e:
        messages.error(request, custom_messages.DELETE_ERROR)
    return redirect('/user_calendar/calendar')



@login_required
def all_events(request):
    queryset = hlp.get_list(Event)
    result = []
    for event in queryset:
        result.append(
            {
                "id":event.id,
                "slug":event.slug,
                "url":'/user_calendar/%s/update'%event.slug,
                "publicId":event.id,
                "title":event.title,
                "start":event.start,
                "end":event.end,
                "backgroundColor":event.backgroundColor,
                "borderColor":event.borderColor,
                "editable":event.editable,
            }
        )
    return JsonResponse(result, safe=False)

def is_read(request):
    today = datetime.date.today()
    Event.objects.filter(start__year=today.year, start__month=today.month, start__day=today.day,is_active=True).update(is_read=True)
    return HttpResponse(json.dumps({"result": True}), content_type="application/json")

def past_is_read(request):
    today = datetime.date.today()
    Event.objects.filter(start__lte=today,is_active=True).update(is_read=True)
    return HttpResponse(json.dumps({"result": True}), content_type="application/json")