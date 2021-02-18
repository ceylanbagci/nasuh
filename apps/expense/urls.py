from django.urls import path
from . import views


urlpatterns = [
    path("create", views.create, name="create"),
    path("<str:slug>/update", views.update, name="update"),
    path("<str:slug>/delete", views.delete, name="delete"),
    path("<int:id>/view_expense", views.view_expense, name="view_expense"),
    path("expense_list_all", views.expense_list_all, name="expense_list_all"),

]
