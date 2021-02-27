import datetime, time
import core.helper as hlp
from user_calendar.models import Event
from django.contrib.auth.decorators import login_required


def get_events(request):
    events = []
    events_count = 0
    today=datetime.date.today()
    events = Event.objects.filter(start__year=today.year, start__month=today.month, start__day=today.day,is_active=True).order_by('start')
    events_past = Event.objects.filter(start__lte=today,is_active=True).order_by('is_read')
    events_count = len(events)
    is_not_read = Event.objects.filter(start__year=today.year, start__month=today.month, start__day=today.day,is_active=True,is_read=False).count()
    return {'cp_events_result': events, 'cp_events_count': events_count, 'is_not_read':is_not_read, 'events_past':events_past}

