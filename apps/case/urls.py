from django.urls import path
from . import views
from django.views.i18n import JavaScriptCatalog


urlpatterns = [
    path("case_list", views.case_list, name="case_list"),
    path("create", views.create, name="create"),
    path("<str:slug>/update", views.update, name="update"),
    path("<str:slug>/delete", views.delete, name="delete"),
    path("<str:slug>/view_case", views.view_case, name="view_case"),
    path("client_list", views.client_list, name="client_list"),
    path("create_client", views.create_client, name="create_client"),
    path("<str:slug>/view_client", views.view_client, name="view_client"),
    path("<str:slug>/update_client", views.update_client, name="update_client"),
    path("<str:slug>/delete_client", views.delete_client, name="delete_client"),
    path("partner_list", views.partner_list, name="partner_list"),
    path("<str:slug>/view_partner", views.view_partner, name="view_partner"),
    path("create_partner", views.create_partner, name="create_partner"),
    path("<str:slug>/update_partner", views.update_partner, name="update_partner"),
    path("<str:slug>/delete_partner", views.delete_partner, name="delete_partner"),
    path("expense_list", views.expense_list, name="expense_list"),
    path("create_expense", views.create_expense, name="create_expense"),
    path("<str:slug>/update_expense", views.update_expense, name="update_expense"),
    path("<str:slug>/delete_expense", views.delete_expense, name="delete_expense"),
]