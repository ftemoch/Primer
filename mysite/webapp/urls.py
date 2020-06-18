from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="inicio"),
    path('productos/', views.productos, name="productos"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name="user-page"),
    path('clientes/<str:pk_test>/', views.clientes, name="clientes"),
    path('crear_contrato1/', views.crearContrato1, name="crear_contrato1"),
    path('crear_contrato/<str:pk>/', views.crearContrato, name="crear_contrato"),
    path('actualizar_contrato/<str:pk>/', views.actualizarContrato, name="actualizar_contrato"),
    path('borrar_contrato/<str:pk>/', views.borrarContrato, name="borrar_contrato"),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name="webapp/password_reset.html"),
         name="password_reset"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="webapp/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/'
         , auth_views.PasswordResetConfirmView.as_view(template_name="webapp/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="webapp/password_reset_done.html"),
         name="password_reset_complete"),

]
"""
1. Envia Formulario - accounts/password_change/ [name='password_change']
2. Envia mensaje contraseña cambiada - accounts/password_change/done/ [name='password_change_done']
3. Enlaza la contraseña y el formumlario de reset - accounts/password_reset/ [name='password_reset']
4. Mensaje de contraseña satrisfactoriamente camabiad- accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']

"""
