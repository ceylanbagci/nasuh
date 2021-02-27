from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("calendar", views.calendar, name="calendar"),
    path("new", views.new, name="new"),
    path("<str:slug>/update", views.update, name="update"),
    path("delete/<str:slug>", views.delete, name="delete"),
    path("all_events", views.all_events, name="all_events"),
    path("is_read", views.is_read, name="is_read"),
    path("past_is_read", views.past_is_read, name="past_is_read"),

]