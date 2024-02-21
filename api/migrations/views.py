from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
import json

from django.views.generic import *

from .forms import *
from .models import *


def get_users(request):
    queryset = User.objects.all()
    data_list = list(queryset.values())
    return JsonResponse(data_list, safe=False)


def get_user(request, id):
    user = User.objects.get(id=id)
    data = {
        'id': user.id,
        'name': user.name,
        's_name': user.s_name,
        'birth': user.birth,
        'gender': user.gender,
        'login': user.login,
        'password': user.password,
        'balance': user.balance,
    }
    return JsonResponse(data, safe=False)


def get_checks(request):
    queryset = Checks.objects.all()
    data_list = list(queryset.values())
    return JsonResponse(data_list, safe=False)


def get_recipes(request):
    queryset = Recipes.objects.all()
    data_list = list(queryset.values())
    return JsonResponse(data_list, safe=False)


def get_meds(request):
    queryset = Medicine.objects.all()
    data_list = list(queryset.values())
    return JsonResponse(data_list, safe=False)

@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        sn = request.POST.get('s_name')
        password = request.POST.get('password')
        birth = request.POST.get('birth')
        gender = request.POST.get('gender')
        login = request.POST.get('login')

        if password is not None and not any(char.isdigit() for char in password):
            return JsonResponse({'error': 'Пароль должен содержать хотя бы одну цифру'})
        if User.objects.filter(login=login).exists():
            return JsonResponse({'error': 'Некорректный логин'})
        if not username:
            return JsonResponse({'error': "нет имени пользователя"})
        try:
            user = User.objects.create(name=username, s_name=sn, password=password, balance=0, gender=gender,
                                       birth=birth, role=1, login=login)
            user.save()
            return JsonResponse({'success': f'Пользователь {username} успешно создан'})
        except ValidationError as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Метод запроса должен быть POST'})

@csrf_exempt
def add_recipes(request):
    if request.method == 'POST':
        try:
            json_file = request.FILES['json_file']
            data = json.loads(json_file.read())
            print(data)
        except KeyError:
            return JsonResponse({'error': 'Некорректный JSON'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Ошибка декодирования JSON'})

        required_fields = ['pat_id', 'm_id', 'r_dose', 'since', 'until']
        for field in required_fields:
            if field not in data:
                return JsonResponse({'error': f'Отсутствует обязательное поле: {field}'})

        # Получаем данные из JSON
        pat_id = data['pat_id']
        m_id = data['m_id']
        r_dose = data['r_dose']
        since = data['since']
        until = data['until']

        # Проверяем существование пользователя и лекарства
        if not User.objects.filter(id=pat_id).exists():
            return JsonResponse({'error': 'Пользователь с указанным ID не найден'})
        if not Medicine.objects.filter(id=m_id).exists():
            return JsonResponse({'error': 'Лекарство с указанным ID не найдено'})

        # Создаем рецепт
        recipe = Recipes.objects.create(pat_id_id=pat_id, m_id_id=m_id, r_dose=r_dose, since=since, until=until)
        recipe.save()

        return JsonResponse({'success': 'Рецепт успешно создан'})
    else:
        return JsonResponse({'error': 'Метод запроса должен быть POST'})

@csrf_exempt
def update_user(request, id):
    if request.method == 'PUT':
        body= json.loads(request.body.decode("utf-8"))
        print(body)
        user = get_object_or_404(User, id=id)
        user.name = body['name']
        user.s_name = body['s_name']
        user.birth = body['birth']
        user.gender = body['gender']
        user.login = body['login']
        user.password = body['password']
        user.balance = body['balance']
        user.save()
        data = {
            'id': user.id,
            'name': user.name,
            's_name': user.s_name,
            'birth': user.birth,
            'gender': user.gender,
            'login': user.login,
            'password': user.password,
            'balance': user.balance,
        }
        return JsonResponse(data)

class MedicineDeleteView(DeleteView):
    model = Medicine
    template_name = 'delete_form.html'

class MedicineUpdateView(UpdateView):
    model = Medicine
    template_name = 'form.html'
    form_class = MedicineForm
    success_url = reverse_lazy('meds-list')
    # fields =['med_n', 'dose', 'price', 'until', 'dev', 'effect', 'others', 'amount']


def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return JsonResponse({'message': 'User deleted successfully'})

def buy(request, med_id, us_id):
    med: Medicine = get_object_or_404(Medicine, id=med_id)
    user: User = get_object_or_404(User, id=us_id)
    if user.balance >= med.price:
        user.balance -= med.price
        med.amount -= 1
        user.save()
        med.save()
        Checks.objects.create(pat_id=user, sum=med.price)
        return JsonResponse({'message': 'Bought successfully'})


