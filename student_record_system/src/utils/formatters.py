"""
Formatters Module
Provides formatting functions for display output.
"""

def format_student_record(student):
    """
    Format a student record for display.

    Args:
        student (dict): Student dictionary with keys: Id, name, age, grades

    Returns:
        str: Formatted string
    """

    output = "\n" + "="*60 + "\n"
    output += f"Student ID: {student.get('id', 'N/A')}\n"
    output += f"Name: {student.get('name', 'N/A')}\n"
    output += f"Age: {student.get('age', 'N/A')}\n"
    
    grades = student.get('grades', [])
    if grades:
        output += f"Grades: {', '.join(map(str, grades))}\n"
        weighted_avg = (grades[0] * 0.20 + grades[1] * 0.20 + grades[2] * 0.20 + grades[3] * 0.40)
        output += f"Average: {weighted_avg:.2f}\n"
    else:
        output += "No grades recorded\n"

    output += "="*60 + "\n"
    return output

def format_table_header():
    """Return formatted table header for student list."""
    header = f"{'ID':<12}{'Name':<25}{'Age':<5}{'Grades':<10}\n"
    header += "-"*52 + "\n"
    return header

def format_table_row(student):
    """Format a single student record as a table row."""
    student_id = student.get('id', 'N/A')
    name = student.get("name","N/A")[:24] # Truncate long names
    age = student.get("age","N/A")

    grades = student.get("grades", [])
    weighted_avg = (grades[0] * 0.20 + grades[1] * 0.20 + grades[2] * 0.20 + grades[3] * 0.40) if grades else 0
    
    return f"{student_id:<12}{name:<25}{age:<5}{weighted_avg:<10.2f}\n"

