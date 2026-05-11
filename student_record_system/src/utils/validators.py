"""
Validators Module
Provides validation functions for student data.
"""

def validate_student_id(student_id):
    """Validate student ID format: YYYY-SS-NNNN"""
    if not isinstance(student_id, str):
        return False

    parts = student_id.split("-")
    if len(parts) != 3:
        return False

    year, semester, number = parts

    if len(year) != 4 or not year.isdigit():
        return False

    if len(semester) != 2 or not semester.isdigit():
        return False

    if len(number) != 4 or not number.isdigit():
        return False

    return True


def validate_name(name):
    """Validate student name."""
    if not name or not isinstance(name, str):
        return False
    name = name.strip()
    if len(name) < 2:
        return False
    return all(c.isalpha() or c.isspace() for c in name)


def validate_age(age):
    """Validate student age (17-100)."""
    try:
        age = int(age)
        return 17 <= age <= 100
    except (ValueError, TypeError):
        return False