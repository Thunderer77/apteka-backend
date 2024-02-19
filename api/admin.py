from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 's_name', 'birth', 'gender', 'login', 'password', 'role', 'balance')

@admin.register(Checks)
class ChecksAdmin(admin.ModelAdmin):
    list_display = ('id', 'pat_id', 'sum')

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('id', 'med_n', 'dose', 'price', 'until', 'dev', 'effect', 'others', 'amount')


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ('id', 'pat_id', 'm_id', 'r_dose', 'since', 'until')