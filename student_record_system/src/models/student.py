"""
Student Model
"""

class Student:
    def __init__(self, student_id, name, age):
        self.id = student_id
        self.name = name
        self.age = age

    def to_dict(self):
        """Convert Student object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Student object from a dictionary."""
        return cls(
            student_id=data['id'],
            name=data['name'],
            age=data['age']
        )