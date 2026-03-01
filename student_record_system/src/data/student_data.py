"""
Student Data Module
Manages student data storage (in-memory for now).
"""

from src.data import storage

#In-memory storage
students = storage.load_students()

def add_student(student):
    
    """
    Add a student to the data base.

    Args:
        student (dict): Student dictionary

    Returns:
    bool: True if added successfully
    """
    #Check for duplicate ID
    if find_student_by_id(student['id']):
        return False
    
    students.append(student)
    storage.save_students(students)
    return True

def find_student_by_id(student_id):
    """
    Find student by ID.

    Args:
        student_id (str): Student ID to search

    Returns:
    dict or None: Student dictionary if found, None otherwise
    """
    for student in students:
        if student['id'] == student_id:
            return student
    return None

def get_all_students():
    """Return list of all students."""
    return students.copy()

def update_student(student_id, updated_data):
    """
    Update student information.

    Args:
        student_id (str): Student ID 
        updated_data (dict): Dictionary with fields to update

    Returns:
        bool: True if updated successfully
    """
    student = find_student_by_id(student_id)
    if not student:
        return False
    
    student.update(updated_data)
    storage.save_students(students)
    return True
def delete_student(student_id):
    """"
    Delete student.

    Args:
        student_id (str): Student ID 

    Returns:
        bool: True if deleted successfully
    """
    student = find_student_by_id(student_id)
    if not student:
        return False
    
    students.remove(student)
    storage.save_students(students)
    return True

def get_student_count():
    """Return total number of students."""
    return len(students)

def save_on_extit():
    """Save students to file before exiting."""
    storage.save_students(students)
    print("Records saved. Goodbye!")
  