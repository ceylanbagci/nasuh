from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("<str:slug>/new",views.new,name="new"),
    path("<int:id>/delete",views.delete,name="delete"),
    path("<str:slug>/salary", views.salary, name="salary"),
    path("expense_salary", views.expense_salary, name="expense_salary"),
    path("<str:slug>/case_expense", views.case_expense, name="case_expense"),
    path("<str:slug>/case_expense_one", views.case_expense_one, name="case_expense_one"),
    path("<str:slug>/get_chart_case", views.get_chart_case, name="get_chart_case"),
    path("<str:slug>/get_chart_client", views.get_chart_client, name="get_chart_client"),
    path("<str:slug>/get_chart_partner", views.get_chart_partner, name="get_chart_partner"),
    path("<str:slug>/get_chart_expense", views.get_chart_expense, name="get_chart_expense"),
    path("<str:slug>/get_chart_office", views.get_chart_office, name="get_chart_office"),
    path("<str:slug>/get_chart_tax", views.get_chart_tax, name="get_chart_tax"),
    path("<str:slug>/get_chart_other", views.get_chart_other, name="get_chart_other"),
    path("<str:slug>/get_chart_employee", views.get_chart_employee, name="get_chart_employee"),

]