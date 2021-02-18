from django.urls import path
from . import views


urlpatterns = [
    path("create", views.create, name="create"),
    path("<str:slug>/update", views.update, name="update"),
    path("<str:slug>/delete", views.delete, name="delete"),
    path("<int:id>/view_tax", views.view_tax, name="view_tax"),
    path("expense_list", views.expense_list, name="expense_list"),

]


