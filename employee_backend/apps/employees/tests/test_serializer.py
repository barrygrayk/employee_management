from apps.employees.serializers import EmployeeSerializer, SkillSerializer
from django.test import TestCase

from apps.employees.factories import EmployeeFactory, SkillFactory


class TestEmployeeSerializer(TestCase):
    def setUp(self):
        self.serializer_data = EmployeeSerializer().data
        self.employee = EmployeeFactory()
        self.skill = SkillFactory(name="Python")

    def test_contains_expected_fields(self):
        """Test that the serializer includes the correct fields."""
        self.assertEqual(
            set(self.serializer_data.keys()),
            set(
                [
                    "first_name",
                    "last_name",
                    "email_address",
                    "mobile_number",
                    "postal_code",
                    "skills",
                    "city",
                    "street_address",
                    "country",
                    "date_of_birth",
                ]
            ),
        )

    def test_add_employee_skills(self):
        """Test that add_employee_skills adds the correct skills to an employee."""
        skill = [
            {
                "name": self.skill.name,
                "years_of_experience": self.skill.years_of_experience,
                "seniority": self.skill.seniority,
            }
        ]
        EmployeeSerializer.add_employee_skills(self.employee, skill)
        self.assertEqual(
            set(skill.name for skill in self.employee.skills.all()),
            set(skill_dict["name"] for skill_dict in skill),
        )


class TestSkillSerializer(TestCase):
    def setUp(self):
        self.serializer_data = SkillSerializer().data

    def test_contains_expected_fields(self):
        """Test that the serializer includes the correct fields."""
        self.assertEqual(
            set(self.serializer_data.keys()),
            set(
                [
                    "name",
                    "years_of_experience",
                    "seniority",
                ]
            ),
        )