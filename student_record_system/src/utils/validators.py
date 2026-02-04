"""
Validators Module
Provides validation functions for students data
"""

def validate_student_id(student_id):
    """
    Validate student ID format: YYYY-SS-NNNN

    Args:
        student_id (str): The student ID to validate

        Returns:
            bool: True if valid, False otherwise

        Examples:
            >>> validate_student_id("2526-01-1234")
            True
            >>> validate_student_id("2024-0001")
            False
            >>> validate_student_id("2526-1-1234")
            False
    """
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
    
def validate_grade(grade):
    """Validate student grade (60-100)."""
    try:
        grade = float(grade)
        return 60 <= grade <= 100
    except (ValueError, TypeError):
        return False
    
def validate_email(email):
    """
    Basic email validation.

    Rules:
    -Must have exactly one "@" symbol
    -Must have username before @
    -Must have domain with at least one dot after @
    -Cannot have spaces
    -Cannot have multiple @ sysmbols
    """

    if not email or not isinstance(email, str):
        return False
    
    email = email.strip().lower()

    #check for spaces
    if ' ' in email:
        return False
    
    #Must have exactly one @ symbol
    if email.count('@') != 1:
        return False
    
    #split by @
    parts = email.split('@')
    username, domain = parts[0], parts[1]

    #Username must not be empty
    if not username:
        return False
    
    #Domain must have at least one dot
    if '.' not in domain:
        return False
    
    #Domain must have content after the last dot
    domain_parts = domain.split('.')
    if not domain_parts[-1]: #Nothing after last dot
        return False
    
    return True
    

