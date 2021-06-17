from django.contrib import admin
from rest_framework_api_key.admin import APIKeyModelAdmin
from .models import Employee, EmployeeAPIKey


def reset_salary_paid(modeladmin, request, queryset):
    queryset.update(salary_paid=0)
reset_salary_paid.short_description = 'Очистить поле "Выплаченная зарплата"'


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['fio', 'position', 'chief', 'salary_amount', 'salary_paid']
    list_filter = ['position', 'level']
    actions = [reset_salary_paid]
admin.site.register(Employee, EmployeeAdmin)


@admin.register(EmployeeAPIKey)
class EmployeeAPIKeyModelAdmin(APIKeyModelAdmin):
    pass