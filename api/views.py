from django.http import JsonResponse
from .models import *


def get_users(request):
    queryset = User.objects.all()
    data_list = list(queryset.values())
    return JsonResponse(data_list, safe=False)


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
