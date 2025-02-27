from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('run-script/', views.run_script, name='run_script'),
    path('pizdecnahuyblyat/', views.registration_view, name='registration'),
    path('login/', views.login_view, name='login'),
    path('registrationB/', views.registrationB, name='registrationB'),
    path('loginB/', views.loginB, name='loginB'),
    path('logout/', views.logout_view, name='logout'),
]