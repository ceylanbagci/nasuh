from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("login",views.log_in,name="login"),
    path("logout",views.log_out,name="logout"),
    path("signup",views.sign_up,name="signup"),
    path("login_activation",views.login_activation,name="login_activation"),
    path("forgot_password", views.forgot_password, name="forgot_password"),
    path("password_recovery/<str:key>",views.password_recovery,name="password_recovery"),
    path("password_change", views.password_change, name="password_change"),

]
