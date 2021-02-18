from django.urls import path
from . import views


urlpatterns = [
    path("report_list", views.report_list, name="report_list"),
    path("end_of_the_day", views.end_of_the_day, name="end_of_the_day"),
    path("end_of_the_month", views.end_of_the_month, name="end_of_the_month"),
    path("end_of_the_year", views.end_of_the_year, name="end_of_the_year"),
    path("get_with_day", views.get_with_day, name="get_with_day"),
    path("get_with_month", views.get_with_month, name="get_with_month"),
    path("get_with_day", views.get_with_day, name="get_with_day"),
    path("get_with_year", views.get_with_year, name="get_with_year"),
    path("get_case_list_report", views.get_case_list_report, name="get_case_list_report"),
    path("get_client_list_report", views.get_client_list_report, name="get_client_list_report"),
    path("get_partner_list_report", views.get_partner_list_report, name="get_partner_list_report"),
    path("get_employee_list_report", views.get_employee_list_report, name="get_employee_list_report"),
    path("<str:slug>/get_case_report", views.get_case_report, name="get_case_report"),
    path("<str:slug>/get_client_report", views.get_client_report, name="get_client_report"),
    path("<str:slug>/get_partner_report", views.get_partner_report, name="get_partner_report"),
    path("<str:slug>/get_employee_report", views.get_employee_report, name="get_employee_report"),
    path("<str:slug>/get_single_expense_report", views.get_single_expense_report, name="get_single_expense_report"),
    path("get_expense_report", views.get_expense_report, name="get_expense_report"),

]


