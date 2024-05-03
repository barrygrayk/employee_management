from rest_framework import filters, viewsets

from apps.employees.models import Employee, Skill
from apps.employees.serializers import EmployeeSerializer, SkillSerializer


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows skills to be viewed.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    Provides filters for searching by first name, last name, and email address.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["first_name", "last_name", "email_address"]
