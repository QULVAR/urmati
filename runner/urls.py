from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница с формой
    path('run-script/', views.run_script, name='run_script'),  # Обработчик данных
]