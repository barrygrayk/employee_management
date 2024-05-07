import re
import unittest
from apps.employees.utils import generate_employee_code


class TestGenerateEmployeeCode(unittest.TestCase):
    def test_generate_employee_code(self):
        """Test that generate_employee_code produces a string."""
        code = generate_employee_code()
        self.assertTrue(isinstance(code, str))

    def test_employee_id_format(self):
        """Test that each created employee ID is 2 random uppercased letters
        followed by 4 random numbers."""
        code = generate_employee_code()
        self.assertTrue(re.match(r"[A-Z]{2}\d{4}", code))
        self.assertTrue(len(code), 6)
