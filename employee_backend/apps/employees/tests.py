import re
import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from apps.employees.factories import EmployeeFactory, SkillFactory
from apps.employees.models import Skill
from apps.employees.utils import generate_employee_code


class SkillViewSetTestCase(APITestCase):
    """
    Test case for the SkillViewSet
    """

    def setUp(self):

        self.skill = SkillFactory()

    def test_get_all_skills(self):
        """
        Test that a GET request to /skills/ returns a 200 status code
        """
        response = self.client.get("/skills/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_skill_not_allowed(self):
        """
        Test that a POST request to /skills/ returns a 405 status code
        (Method Not Allowed)
        """
        data = {"name": "Python", "years_of_experience": 1, "seniority": "JR"}
        response = self.client.post("/skills/", data=data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_skill_not_found(self):
        """
        Test that a GET request to /skills/{id}/ returns a 404 status code
        when the skill does not exist
        """
        response = self.client.get("/skills/999999/")  # Use an ID that does not exist
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class EmployeeViewSetTestCase(APITestCase):
    """
    Test case for the EmployeeViewSet
    """

    def setUp(self):
        self.employee = EmployeeFactory()

    def test_get_all_employees(self):
        """
        Test that a GET request to /employees/ returns a 200 status code
        """
        response = self.client.get("/employees/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_employee(self):
        """
        Test that a GET request to /employees/{id}/ returns the correct
        employee
        """
        response = self.client.get(f"/employees/{self.employee.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], self.employee.first_name)
        self.assertEqual(response.data["last_name"], self.employee.last_name)
        self.assertEqual(response.data["email_address"], self.employee.email_address)

    def test_create_employee(self):
        """
        Test that a POST request to /employees/ creates an employee and returns a 201 Created status code
        """
        employee_data = {
            "first_name": "Ben",
            "last_name": "Mulala",
            "mobile_number": "1234567890",
            "email_address": "ben.doe@example.com",
            "street_address": "123 Main St",
            "city": "Anytown",
            "postal_code": "12345",
            "country": "Zambia",
            "skills": [{"name": "test", "years_of_experience": 1, "seniority": "JR"}],
        }
        response = self.client.post(
            "/employees/",
            data=json.dumps(employee_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_employee(self):
        """
        Test that a PUT request to /employees/{id}/ updates an employee
        and returns a 200 OK status code
        """
        employee = EmployeeFactory()
        updated_employee_data = {
            "first_name": "Sammy",
            "last_name": "Kapili",
            "mobile_number": "0987654321",
            "email_address": "sammy.doe@example.com",
            "street_address": "456 Main St",
            "city": "Anytown",
            "postal_code": "54321",
            "country": "Zambia",
            "skills": [{"name": "Python", "years_of_experience": 1, "seniority": "JR"}],
        }
        response = self.client.put(
            f"/employees/{employee.id}/",
            data=json.dumps(updated_employee_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], "Sammy")
        self.assertEqual(response.data["last_name"], "Kapili")

    def test_delete_employee(self):
        """
        Test that a DELETE request to /employees/{id}/ deletes an employee and
        returns a 204 No Content status code
        """
        employee = EmployeeFactory()
        response = self.client.delete(f"/employees/{employee.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_employee_with_missing_fields(self):
        """
        Test that a POST request to /employees/ with missing fields returns a
        400 Bad Request status code
        """
        employee_data_with_missing_fields_1 = {
            "first_name": "John",
            "last_name": "Doe",
            "email_address": "john.doe@example.com",
            "city": "Anytown",
            "postal_code": "12345",
        }
        response = self.client.post(
            "/employees/",
            data=json.dumps(employee_data_with_missing_fields_1),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        employee_data_with_missing_fields_2 = {
            "first_name": "Sammy",
            "last_name": "Kapili",
            "mobile_number": "0987654321",
            "email_address": "sammy.doe@example.com",
            "street_address": "456 Main St",
            "city": "Anytown",
            "postal_code": "54321",
            "country": "Zambia",
        }
        response = self.client.post(
            "/employees/",
            data=json.dumps(employee_data_with_missing_fields_2),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_search_employees(self):
        """
        Test that a GET request to /employees/ with a search query returns the correct employees
        """
        EmployeeFactory(
            first_name="John", last_name="Doe", email_address="john.doe@example.com"
        )
        EmployeeFactory(
            first_name="Jane", last_name="Doe", email_address="jane.doe@example.com"
        )
        response = self.client.get("/employees/", {"search": "john"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["first_name"], "John")

    def test_filter_employees(self):
        """
        Test that a GET request to /employees/ with a filter query returns the correct employees
        """
        EmployeeFactory(
            first_name="John", last_name="Doe", email_address="john.doe@example.com"
        )
        EmployeeFactory(
            first_name="Jane", last_name="Doe", email_address="jane.doe@example.com"
        )
        response = self.client.get(
            "/employees/", {"email_address": "john.doe@example.com"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_create_employees_with_same_skill(self):
        """
        Test that a POST request to /employees/ creates employees with the
        same skill but only one instance shoudl exists
        """
        skill = SkillFactory()  # Create a skill
        employee_data_1 = {
            "first_name": "Ellah",
            "last_name": "Cooper",
            "mobile_number": "0987654321",
            "email_address": "sammy.doe@example.com",
            "street_address": "456 Main St",
            "city": "Anytown",
            "postal_code": "54321",
            "country": "Zambia",
            "skills": [
                {
                    "name": skill.name,
                    "years_of_experience": skill.years_of_experience,
                    "seniority": skill.seniority,
                }
            ],
        }
        employee_data_2 = {
            "first_name": "Lala",
            "last_name": "Cooper",
            "mobile_number": "0987654321",
            "email_address": "sammy.doe@example.com",
            "street_address": "456 Main St",
            "city": "Anytown",
            "postal_code": "54321",
            "country": "Zambia",
            "skills": [
                {
                    "name": skill.name,
                    "years_of_experience": skill.years_of_experience,
                    "seniority": skill.seniority,
                }
            ],
        }
        response_1 = self.client.post(
            "/employees/", data=employee_data_1, format="json"
        )
        response_2 = self.client.post(
            "/employees/", data=employee_data_2, format="json"
        )
        self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Skill.objects.count(), 1)


class EmployeeCodeTestCase(TestCase):
    def test_employee_id_is_unique(self):
        """Test that each created employee has a unique ID."""
        employee1 = EmployeeFactory()
        employee2 = EmployeeFactory()
        self.assertNotEqual(employee1.employee_code, employee2.employee_code)

    def test_employee_id_format(self):
        """Test that each created employee ID is 2 random uppercased letters
        followed by 4 random numbers."""
        employee = EmployeeFactory()
        self.assertTrue(re.match(r'[A-Z]{2}\d{4}', employee.employee_code))