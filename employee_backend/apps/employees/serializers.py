import logging
from typing import Any, Dict, List

from apps.employees.models import Employee, Skill
from rest_framework import serializers

logger = logging.getLogger(__name__)


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["name", "years_of_experience", "seniority"]


class EmployeeSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)

    class Meta:
        model = Employee
        fields = [
            "id",
            "first_name",
            "last_name",
            "mobile_number",
            "email_address",
            "street_address",
            "date_of_birth",
            "city",
            "postal_code",
            "country",
            "skills",
            "created_at",
        ]

    def validate_skills(self, value: str) -> str:
        """
        Check that the skills list is not empty.
        """
        if not value:
            raise serializers.ValidationError("The skills list must not be empty.")
        return value

    def create(self, validated_data: Dict[str, Any]) -> Employee:
        skills_data = validated_data.pop("skills", None)
        employee = Employee.objects.create(**validated_data)
        employee = self.add_employee_skills(employee, skills_data)
        return employee

    def update(self, instance: Employee, validated_data: Dict[str, Any]) -> Employee:
        skills_data = validated_data.pop("skills", None)
        instance = super().update(instance, validated_data)
        if skills_data is not None:
            instance.skills.clear()
            instance = self.add_employee_skills(instance, skills_data)
        return instance

    @staticmethod
    def add_employee_skills(instance: Employee, skills: List[Dict[str, Any]]) -> Employee:
        for skill in skills:
            skill, created = Skill.objects.get_or_create(**skill)
            instance.skills.add(skill)

        return instance
