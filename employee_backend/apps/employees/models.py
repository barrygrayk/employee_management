import uuid

from apps.employees.enums import SENIORITY_CHOICES, SeniorityLevel
from apps.employees.utils import generate_employee_code
from django.db import models
from django.utils import timezone


class Skill(models.Model):
    """
    Skill model represents a particular skill that an employee can have.
    Each skill has a unique name, years of experience and a seniority level.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    years_of_experience = models.IntegerField()
    seniority = models.CharField(
        max_length=2, choices=SENIORITY_CHOICES, default=SeniorityLevel.JUNIOR.value
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    Employee model represents an employee in the company.
    Each employee has a first name, last name, mobile number, email address,
    street address, city, postal code, and country.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_code = models.CharField(
        max_length=6, unique=True, blank=True, editable=False
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=15)
    email_address = models.EmailField(max_length=254)
    street_address = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=timezone.now)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    skills = models.ManyToManyField(Skill)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.employee_code:  # if the model instance is being created
            self.employee_code = self.generate_unique_employee_id()
        super().save(*args, **kwargs)

    def generate_unique_employee_id(self):
        employee_code = generate_employee_code()
        if Employee.objects.filter(employee_code=employee_code).exists():
            return self.generate_unique_employee_id()
        return employee_code
