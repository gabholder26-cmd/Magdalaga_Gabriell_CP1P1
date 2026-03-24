"""
Student Manager
Handles all CRUD logic for student records using Student objects.
"""

from src.models.student import Student
from src.data import storage

class StudentManager:
    def __init__(self):
        raw_data = storage.load_students()
        self.students = [Student.from_dict(d) for d in raw_data]

    def add_student(self, student):
        """Add a Student object. Returns True if successful."""
        if self.find_by_id(student.id):
            return False
        self.students.append(student)
        storage.save_students([s.to_dict() for s in self.students])
        return True

    def find_by_id(self, student_id):
        """Find and return a Student by ID, or None if not found."""
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def get_all(self):
        """Return a list of all Student objects."""
        return self.students.copy()

    def update_student(self, student_id, updates):
        """Update a student, Returns True if successful."""
        student = self.find_by_id(student_id)
        if not student:
            return False
        for key, value in updates.items():
            setattr(student, key, value)
        storage.save_students([s.to_dict() for s in self.students])
        return True

    def delete_student(self, student_id):
        """Delete a student by ID. Returns True if successful."""
        student = self.find_by_id(student_id)
        if not student:
            return False
        self.students.remove(student)
        storage.save_students([s.to_dict() for s in self.students])
        return True

    def count(self):
        """Return total number of students."""
        return len(self.students)

    def save_on_exit(self):
        """Save all students to file before exiting."""
        storage.save_students([s.to_dict() for s in self.students])
        print("Records saved. Goodbye!")