"""
Main Window
GUI Student Record Management System.
Built using CustomTkinter.
"""

import customtkinter as ctk
from src.data.student_manager import StudentManager
from src.models.student import Student
from src.utils.validators import validate_student_id, validate_name, validate_age


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Connect to the application logic layer
        self.manager = StudentManager()

        # Window setup
        self.title("Student Record Management System")
        self.geometry("620x560")
        self.resizable(False, False)

        self.build_ui()


    def build_ui(self):

        # Title
        ctk.CTkLabel(
            self,
            text="Student Record Management System",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(pady=(20, 5))

        ctk.CTkLabel(
            self,
            text="Version 4.0",
            font=ctk.CTkFont(size=11),
            text_color="gray60"
        ).pack(pady=(0, 15))

        # Input Fields
        form = ctk.CTkFrame(self)
        form.pack(padx=30, fill="x")

        # Student ID
        ctk.CTkLabel(
            form, text="Student ID:",
            anchor="w", width=100
        ).grid(row=0, column=0, padx=(15, 5), pady=10, sticky="w")

        self.id_entry = ctk.CTkEntry(
            form, width=340,
            placeholder_text="Format: YYYY-SS-NNNN  e.g. 2526-01-0001"
        )
        self.id_entry.grid(row=0, column=1, padx=(0, 15), pady=10)

        # Name
        ctk.CTkLabel(
            form, text="Name:",
            anchor="w", width=100
        ).grid(row=1, column=0, padx=(15, 5), pady=10, sticky="w")

        self.name_entry = ctk.CTkEntry(
            form, width=340,
            placeholder_text="e.g. Juan Dela Cruz"
        )
        self.name_entry.grid(row=1, column=1, padx=(0, 15), pady=10)

        # Age
        ctk.CTkLabel(
            form, text="Age:",
            anchor="w", width=100
        ).grid(row=2, column=0, padx=(15, 5), pady=10, sticky="w")

        self.age_entry = ctk.CTkEntry(
            form, width=340,
            placeholder_text="Must be between 17 and 100"
        )
        self.age_entry.grid(row=2, column=1, padx=(0, 15), pady=10)

        # Buttons
        buttons = ctk.CTkFrame(self, fg_color="transparent")
        buttons.pack(pady=15)

        ctk.CTkButton(
            buttons, text="Add Student",
            command=self.add_student,
            width=130, height=38
        ).grid(row=0, column=0, padx=6)

        ctk.CTkButton(
            buttons, text="View Students",
            command=self.view_students,
            width=130, height=38
        ).grid(row=0, column=1, padx=6)

        ctk.CTkButton(
            buttons, text="Search Student",
            command=self.search_student,
            width=130, height=38
        ).grid(row=0, column=2, padx=6)

        ctk.CTkButton(
            buttons, text="Delete Student",
            command=self.delete_student,
            width=130, height=38,
            fg_color="#c0392b",
            hover_color="#a93226"
        ).grid(row=0, column=3, padx=6)

        # Output Area
        ctk.CTkLabel(
            self, text="Output:",
            font=ctk.CTkFont(size=13, weight="bold"),
            anchor="w"
        ).pack(padx=30, anchor="w")

        self.output = ctk.CTkTextbox(
            self, height=200,
            font=ctk.CTkFont(size=13)
        )
        self.output.pack(padx=30, pady=(5, 20), fill="both", expand=True)
        self.output.configure(state="disabled")


    def add_student(self):
        student_id = self.id_entry.get().strip()
        name       = self.name_entry.get().strip()
        age        = self.age_entry.get().strip()

        # Validate ID
        if not student_id:
            self.show("ERROR: Student ID cannot be empty.")
            return
        if not validate_student_id(student_id):
            self.show("ERROR: Invalid ID format.\nUse YYYY-SS-NNNN  e.g. 2526-01-0001")
            return

        # Validate Name
        if not name:
            self.show("ERROR: Name cannot be empty.")
            return
        if not validate_name(name):
            self.show("ERROR: Name must be at least 2 characters\nand contain letters only.")
            return

        # Validate Age
        if not age:
            self.show("ERROR: Age cannot be empty.")
            return
        if not age.isdigit():
            self.show("ERROR: Age must be a number.")
            return
        if not validate_age(age):
            self.show("ERROR: Age must be between 17 and 100.")
            return

        if self.manager.find_by_id(student_id):
            self.show(f"ERROR: Student ID {student_id} already exists.")
            return

        student = Student(student_id, name.title(), int(age))
        self.manager.add_student(student)

        self.show(
            f"SUCCESS: Student added!\n\n"
            f"ID: {student_id} | Name: {name.title()} | Age: {age}"
        )
        self.clear_inputs()

    def view_students(self):
        students = self.manager.get_all()

        if not students:
            self.show("No students found in the system.")
            return

        lines = [f"Total Students: {len(students)}\n"]
        lines.append("-" * 48)
        for s in students:
            lines.append(f"ID: {s.id} | Name: {s.name} | Age: {s.age}")
        lines.append("-" * 48)

        self.show("\n".join(lines))

    def search_student(self):
        student_id = self.id_entry.get().strip()

        if not student_id:
            self.show("ERROR: Please type a Student ID in the ID field.")
            return

        student = self.manager.find_by_id(student_id)

        if student:
            self.show(
                f"Student Found!\n\n"
                f"ID:   {student.id}\n"
                f"Name: {student.name}\n"
                f"Age:  {student.age}"
            )
        else:
            self.show(f"Student ID '{student_id}' was not found.")

    def delete_student(self):
        student_id = self.id_entry.get().strip()

        if not student_id:
            self.show("ERROR: Please type a Student ID in the ID field.")
            return

        student = self.manager.find_by_id(student_id)

        if not student:
            self.show(f"ERROR: Student ID '{student_id}' was not found.")
            return

        self.manager.delete_student(student_id)
        self.show(
            f"Student successfully deleted!\n\n"
            f"ID: {student.id} | Name: {student.name} | Age: {student.age}\n\n"
            f"The record has been removed."
        )
        self.clear_inputs()


    def show(self, message):
        """Display a message in the output area."""
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("end", message)
        self.output.configure(state="disabled")

    def clear_inputs(self):
        """Clear all three input fields."""
        self.id_entry.delete(0, "end")
        self.name_entry.delete(0, "end")
        self.age_entry.delete(0, "end")