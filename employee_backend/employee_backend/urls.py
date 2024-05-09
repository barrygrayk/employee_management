from apps.employees.views import EmployeeViewSet, SkillViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"employees", EmployeeViewSet)
router.register(r"skills", SkillViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
]
