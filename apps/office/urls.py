from django.urls import path
from . import views


urlpatterns = [
    # path("", views.office, name="office"),
    path("create", views.create, name="create"),
    path("<str:slug>/update", views.update, name="update"),
    path("<str:slug>/delete", views.delete, name="delete"),
    path("<int:id>/view_office", views.view_office, name="view_office"),
    path("create_employee", views.create_employee, name="create_employee"),
    path("employee_list", views.employee_list, name="employee_list"),
    path("<str:slug>/update_employee", views.update_employee, name="update_employee"),
    path("<str:slug>/delete_employee", views.delete_employee, name="delete_employee"),
    path("<str:slug>/view_employee", views.view_employee, name="view_employee"),
    path("expense_list", views.expense_list, name="expense_list"),

]
