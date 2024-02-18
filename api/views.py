from django.http import JsonResponse
from django.shortcuts import render
def test(request):
    return JsonResponse({'hello': 'world'})
# Create your views here.
