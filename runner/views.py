from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads
from .main import urmati

# Отображение HTML-страницы
@csrf_exempt
def index(request):
    return render(request, 'index.html')

# Обработка данных из формы и выполнение логики
@csrf_exempt
def run_script(request):
    if request.method == 'POST':
        data = loads(request.body)
        u = data.get('param1', '')
        matrix = data.get('param2', '')
        mode = data.get('mode', '')
        result = urmati(u, matrix, mode)
        return JsonResponse({'status': '', 'message': result})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})