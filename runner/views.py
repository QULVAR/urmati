from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json  # Для обработки POST-запросов
from .main import urmati
from django.views.decorators.csrf import csrf_exempt

# Отображение HTML-страницы
@csrf_exempt
def index(request):
    return render(request, 'index.html')

# Обработка данных из формы и выполнение логики
@csrf_exempt
def run_script(request):
    if request.method == 'POST':
        # Получаем данные из POST-запроса
        data = json.loads(request.body)
        u = data.get('param1', '')
        matrix = data.get('param2', '')

        # Выполняем логику
        result = urmati(u, matrix)

        # Возвращаем текстовый ответ, не пытаясь интерпретировать его как HTML
        return JsonResponse({'status': '', 'message': result})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})