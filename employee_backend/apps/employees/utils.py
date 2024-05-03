import random
import string


def generate_employee_code() -> str:
    """Generate an ID consisting of 2 random uppercase letters and 4 random digits."""
    return "".join(random.choices(string.ascii_uppercase, k=2)) + "".join(
        random.choices(string.digits, k=4)
    )
