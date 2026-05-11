"""
Storage Module
Handles loading and saving student data using SQLite.
"""

import sqlite3
import os

# Always save the database next to main.py to make it work in every device
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_FILE = os.path.join(BASE_DIR, "students.db")


def get_connection():
    """Connect to the SQLite database."""
    return sqlite3.connect(DB_FILE)


def initialize_db():
    """Create the students table if it does not exist yet."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id    TEXT PRIMARY KEY,
            name  TEXT NOT NULL,
            age   INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def load_students():
    """Load all students from the database."""
    initialize_db()

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age FROM students")
    rows = cursor.fetchall()
    conn.close()

    students = []
    for row in rows:
        students.append({
            'id':   row[0],
            'name': row[1],
            'age':  row[2]
        })

    if students:
        print(f"Loaded {len(students)} student record(s) from database.")
    else:
        print("No existing records found. Starting fresh.")

    return students


def save_student(student_dict):
    """Insert one student into the database."""
    initialize_db()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (id, name, age) VALUES (?, ?, ?)",
        (student_dict['id'], student_dict['name'], student_dict['age'])
    )

    conn.commit()
    conn.close()
    print(f"Saved: {student_dict['id']} | {student_dict['name']} | Age {student_dict['age']}")


def delete_student(student_id):
    initialize_db()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()
    print(f"Deleted: {student_id}")