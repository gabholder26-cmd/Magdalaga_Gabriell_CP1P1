"""
Student Model
Represents a single student as an object.
"""

class Student:
    def __init__(self, student_id, name, age, email, grades=None):
        self.id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.grades = grades if grades is not None else []

    def to_dict(self):
        """Convert Student object to dictionary (for saving to JSON)."""
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'email': self.email,
            'grades': self.grades
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Student object from a dictionary (for loading from JSON)."""
        return cls(
            student_id=data['id'],
            name=data['name'],
            age=data['age'],
            email=data['email'],
            grades=data.get('grades', [])
        )