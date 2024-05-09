from django.contrib import admin
from apps.employees.models import Employee, Skill


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("skills",)


class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "years_of_experience", "seniority")
    search_fields = ("name",)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Skill, SkillAdmin)
