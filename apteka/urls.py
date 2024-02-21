from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', get_users),
    path('user/<int:id>/get/', get_user),
    path('user/<int:id>/', update_user, name='update_user'),
    path('user/add/', add_user, name='add'),
    path('user/<int:id>/delete/', delete_user, name='delete_user'),
    path('meds/<int:pk>/delete/', MedicineDeleteView.as_view(), name='medicine_delete'),
    path('meds/<int:pk>/update/', MedicineUpdateView.as_view(), name='upd_med'),
    path('meds/<int:med_id>/buyby/<int:us_id>/', buy, name='buy'),
    path('checks/', get_checks),
    path('recipes/', get_recipes),
    path('recipes/add', add_recipes),
    path('meds/', get_meds, name="meds-list"),
]
