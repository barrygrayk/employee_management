from enum import Enum


class SeniorityLevel(Enum):
    """
    Enum representing the seniority level of a skill.

    - JUNIOR: Represents a junior level skill.
    - INTERMEDIATE: Represents an intermediate level skill.
    - SENIOR: Represents a senior level skill.
    """
    JUNIOR = "JR"
    INTERMEDIATE = "IN"
    SENIOR = "SR"


SENIORITY_CHOICES = [(level.value, level.name) for level in SeniorityLevel]
