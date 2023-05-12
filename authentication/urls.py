from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm, SetPasswordForm

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('account-verification', views.account_verify, name='account-verification'),
    path('reset-password', auth_views.PasswordResetView.as_view(template_name='auth/reset_password.html', form_class=UserPasswordResetForm), name='reset-password'),
    path('reset-password-sent', auth_views.PasswordResetDoneView.as_view(template_name='auth/reset_password_send.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='auth/reset_password_form.html', form_class=SetPasswordForm),name='password_reset_confirm'),
    path('reset-password-complete', auth_views.PasswordResetCompleteView.as_view(template_name='auth/reset_password_complete.html'), name='password_reset_complete'),
]
