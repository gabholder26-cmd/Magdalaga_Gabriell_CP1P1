"""
Student Manager
Handles all CRUD operations for student records.
This is the Application Logic layer between the GUI and the Database.
"""

from src.models.student import Student
from src.data import storage


class StudentManager:
    def __init__(self):
        # Load existing records from the database when the app starts
        raw_data = storage.load_students()
        self.students = [Student.from_dict(d) for d in raw_data]

    def add_student(self, student):
        """
        Add a Student object to the system.
        Returns True if successful, False if ID already exists.
        """
        if self.find_by_id(student.id):
            return False

        self.students.append(student)
        storage.save_student(student.to_dict())
        return True

    def find_by_id(self, student_id):
        """
        Find and return a Student by ID.
        Returns None if not found.
        """
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def get_all(self):
        """Return a copy of all students."""
        return self.students.copy()

    def delete_student(self, student_id):
        """
        Delete a student by ID.
        Returns True if deleted, False if not found.
        """
        student = self.find_by_id(student_id)
        if not student:
            return False

        self.students.remove(student)
        storage.delete_student(student_id)
        return True

    def count(self):
        """Return the total number of students."""
        return len(self.students)