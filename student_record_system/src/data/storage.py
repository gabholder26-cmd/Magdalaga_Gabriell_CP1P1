"""
Storage Module
Handles saving and loading student data from a JSON file.
"""

import json
import os

DATA_FILE = "data/students.json"

def load_students():
    """Load students from JSON file. Returns empty list if file doesn't exists."""
    if not os.path.exists(DATA_FILE):
        print("No saved records found. Starting new.")
        return []
    
    try:
        with open(DATA_FILE, "r") as f:
            content = f.read()
            if not content.strip():
                print("No saved records found. Starting new.")
                return []
            data = json.loads(content)
            print(f"Loaded {len(data)} student records.")
            return data
    except (json.JSONDecodeError, ValueError):
        print("Warning: Save file is corrupted. Check the student data file.")
        return []

def save_students(students):
    """Save students list to JSON file."""
    os.makedirs("data", exist_ok=True)
    
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(students, f, indent=4)
    except Exception as e:
        print(f"Warning: Could not save records: {e}")