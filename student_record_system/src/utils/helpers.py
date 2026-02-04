"""
Helpers Module
Provides helper functions for common tasks.
"""

def get_valid_input(prompt, validation_func, error_mssg="Invalid input!"):
    """
    Get validated input from user.

    Args:
        prompt (str): Input prompt 
        validation_func (function): Function to validate input
        error_mssg (str): Error message for invalid input

    Returns:
        str: Validated user input
    """
    while True:
        user_input = input(prompt).strip()
        if validation_func(user_input):
            return user_input
        print(f"{error_mssg}")

def pause():
    """Pause and wait for user to press Enter."""
    input("\nPress Enter to continue...")

def clear_screen():
    """Clear the console screen."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_student_id(start_year, semester, number):
    """
    Generate student ID in format YYYY-SS-NNNN.

    Args:
        year (int): Year of enrollment Starting year of academic year (e.g., 2025 for 2025-2026)
         semester (int): Semester number (e.g., 1 for first semester)
         number (int): Student enrollee number

    Returns:
        str: Formatted student ID

    Examples:
        >>> generate_student_id(2025, 1, 1234)
        '2025-01-1234'
        >>> generate_student_id(2024, 2, 5)
        '2024-02-0005'
    """
    #Combine Last two digits of academic year
    year1 = start_year % 100
    year2 = (start_year + 1) % 100
    year_part = f"{year1:02d}{year2:02d}"

    #Format semester as 2 digrs
    semester_part = str(semester).zfill(2)

    #Format number as 4 digits
    number_part = str(number).zfill(4)
    return f"{year_part}-{semester_part}-{number_part}"