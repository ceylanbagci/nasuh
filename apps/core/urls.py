from django.urls import path
from . import views


urlpatterns = [
    path("get_districts_from_city/<int:city_id>", views.get_districts_from_city, name="get_districts_from_city"),
]
