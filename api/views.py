from django.http import JsonResponse
from .models import *


def get_users(request):
    # Получение списка объектов из базы данных
    queryset = User.objects.all()

    # Преобразование объектов в список словарей
    data_list = list(queryset.values())

    # Возврат данных в формате JSON с помощью JsonResponse
    return JsonResponse(data_list, safe=False)


def get_checks(request):
    # Получение списка объектов из базы данных
    queryset = Checks.objects.all()

    # Преобразование объектов в список словарей
    data_list = list(queryset.values())

    # Возврат данных в формате JSON с помощью JsonResponse
    return JsonResponse(data_list, safe=False)


def get_recipes(request):
    # Получение списка объектов из базы данных
    queryset = Recipes.objects.all()

    # Преобразование объектов в список словарей
    data_list = list(queryset.values())

    # Возврат данных в формате JSON с помощью JsonResponse
    return JsonResponse(data_list, safe=False)


def get_meds(request):
    # Получение списка объектов из базы данных
    queryset = Medicine.objects.all()

    # Преобразование объектов в список словарей
    data_list = list(queryset.values())

    # Возврат данных в формате JSON с помощью JsonResponse
    return JsonResponse(data_list, safe=False)
# Create your views here.
