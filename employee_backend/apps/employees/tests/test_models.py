from django.test import TestCase

from apps.employees.factories import EmployeeFactory, SkillFactory


class EmployeeSkillModelTestCase(TestCase):
    def test_employee_id_is_unique(self):
        """Test that each created employee has a unique ID."""
        employee1 = EmployeeFactory()
        employee2 = EmployeeFactory()
        self.assertNotEqual(employee1.employee_code, employee2.employee_code)

    def test_string_representation(self):
        """Test the string representation of the EmployeeSkill model."""
        employee = EmployeeFactory()
        skill = SkillFactory()
        self.assertEqual(str(employee), f"{employee.first_name} {employee.last_name}")
        self.assertEqual(str(skill), f"{skill.name}")

