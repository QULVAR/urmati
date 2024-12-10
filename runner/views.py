from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from markdown_katex import KatexExtension
from markdown import markdown
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
        result = urmati(u, matrix, 'SR')
        return JsonResponse({'status': '', 'message': result})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})