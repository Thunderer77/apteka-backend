
from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', get_users),
    path('checks/', get_checks),
    path('recipes/', get_recipes),
    path('meds/', get_meds),
]
