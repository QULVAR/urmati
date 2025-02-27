from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from json import loads, dumps
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.utils import timezone
from .main import urmati


@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'status': 'success', 'message': 'Вы успешно вышли'})
    return JsonResponse({'status': 'error', 'message': 'Неверный метод запроса'})


@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html')


# Обработка данных из формы и выполнение логики
@csrf_exempt
def run_script(request):
    if not request.user.is_authenticated:
        return JsonResponse({'status': 'error', 'message': 'Необходима авторизация'})
    if request.method == 'POST':
        data = loads(request.body)
        u = data.get('param1', '')
        matrix = data.get('param2', '')
        mode = data.get('mode', '')
        result = urmati(u, matrix, mode)
        return JsonResponse({'status': '', 'message': result})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


# Страница входа
def login_view(request):
    return render(request, 'login.html')


# Страница регистрации
def registration_view(request):
    return render(request, 'registration.html')


# Логика авторизации
@csrf_exempt
def loginB(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if username != 'qulvar':
                # Удаляем все сессии пользователя перед входом
                sessions = Session.objects.filter(expire_date__gte=timezone.now())
                for session in sessions:
                    data = session.get_decoded()
                    if data.get('_auth_user_id') == str(user.id):
                        session.delete()
                    
            # Логиним пользователя
            login(request, user)
            return returnJson(status='success', message='Успешный вход')
        
        return returnJson(status='error', message='Неверный логин или пароль')
    
    return returnJson(status='error', message='Неверный метод запроса')


@csrf_exempt
def registrationB(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return returnJson(status='error', message='Пользователь с таким логином уже существует')
        
        user = User.objects.create_user(username=username, password=password)
        user.save()
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return returnJson(status='success', message='Регистрация прошла успешно')
    
    return returnJson(status='error', message='Неверный метод запроса')


def returnJson(data={}, status='', message=''):
    if data == {}:
        data2 = {
            'status': status,
            'message': message
        }
    else:
        data2 = data
    return HttpResponse(dumps(data2, ensure_ascii=False), content_type='application/json')
