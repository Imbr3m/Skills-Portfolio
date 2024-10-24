import tkinter as tk
from tkinter import *
from tkinter import ttk

# Create the main Tkinter root
root = tk.Tk()
root.title("Student Manager")

# Set the background color of the root window
root.configure(bg='black')

# FUNCTIONSS
# Read and parse the data from studentMarks.txt
def load_student_data():
    # Open the studentMarks.txt file for reading
    with open("Assets/studentMarks.txt", "r") as file:
        students = []  # Create an empty list to store student data
        
        # Read the number of students from the first line
        num_students = int(file.readline().strip())
        
        # Loop through each line in the file to read student records
        for line in file:
            parts = line.strip().split(',')  # Split the line by commas
            
            # Extract student information from parts
            student_number = int(parts[0])  # Convert the first part to an integer
            student_name = parts[1]          # Second part is the name
            coursework_marks = list(map(int, parts[2:5]))  # Convert coursework marks to integers
            
            # Calculate the total coursework score
            coursework_total = sum(coursework_marks)
            exam_mark = int(parts[5])  # Convert the exam mark to an integer
            
            # Calculate overall percentage
            overall_percentage = ((coursework_total + exam_mark) / 160) * 100
            
            # Determine the grade based on the percentage
            grade = student_score_level(overall_percentage)
            
            # Create a simple dictionary for the student record
            student_record = {
                "number": student_number,
                "name": student_name,
                "coursework": coursework_total,
                "exam": exam_mark,
                "percentage": overall_percentage,
                "grade": grade
            }
            
            # Add the student record to the list of students
            students.append(student_record)  
            
    return students  # Return the list of student records

def student_score_level(percentage):
    if percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'

def view_all_students():
    output = ""
    for student in students:
        output += (
            f"Name: {student['name']}\n"
            f"Number: {student['number']}\n"
            f"Coursework Total: {student['coursework']}\n"
            f"Exam Mark: {student['exam']}\n"
            f"Overall Percentage: {student['percentage']:.2f}%\n"
            f"Grade: {student['grade']}\n\n"
        )
    display_output(output)

def view_individual_student():
    selected = student_var.get()
    for student in students:
        if student['name'] == selected:
            output = (
                f"Name: {student['name']}\n"
                f"Number: {student['number']}\n"
                f"Coursework Total: {student['coursework']}\n"
                f"Exam Mark: {student['exam']}\n"
                f"Overall Percentage: {student['percentage']:.2f}%\n"
                f"Grade: {student['grade']}\n"
            )
            display_output(output)
            return

def show_highest_score():
    top_student = max(students, key=lambda s: s['percentage'])
    display_student_info(top_student)

def show_lowest_score():
    low_student = min(students, key=lambda s: s['percentage'])
    display_student_info(low_student)

def display_student_info(student):
    output = (
        f"Name: {student['name']}\n"
        f"Number: {student['number']}\n"
        f"Coursework Total: {student['coursework']}\n"
        f"Exam Mark: {student['exam']}\n"
        f"Overall Percentage: {student['percentage']:.2f}%\n"
        f"Grade: {student['grade']}\n"
    )
    display_output(output)

def display_output(output):
    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, output)
    text_area.config(state=tk.DISABLED)

# TKINTERR

# Load student data from the file
students = load_student_data()

# Title Label
title_label = tk.Label(root, text="Student Manager", font=("Arial", 16, "bold"), bg='black', fg='green')
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Buttons for different functionalities
btn_view_all = tk.Button(root, text="View All Student Records", command=view_all_students, bg='black', fg='green')
btn_view_all.grid(row=1, column=0, padx=10, pady=5)

btn_highest = tk.Button(root, text="Show Highest Score", command=show_highest_score, bg='black', fg='green')
btn_highest.grid(row=1, column=1, padx=10, pady=5)

btn_lowest = tk.Button(root, text="Show Lowest Score", command=show_lowest_score, bg='black', fg='green')
btn_lowest.grid(row=1, column=2, padx=10, pady=5)

# Frame to hold the OptionMenu with a green border
frame = Frame(root, bg='green')
frame.grid(row=2, column=0, padx=10, pady=5)

# Variable to hold the selected student name
student_var = StringVar()

# OptionMenu to select individual student
student_menu = OptionMenu(frame, student_var, *[s['name'] for s in students])
student_menu.config(bg='black', fg='green', activebackground='green', activeforeground='black', borderwidth=0, highlightbackground= 'green')
student_menu["menu"].config(bg='black', fg='green')
student_menu.pack()

btn_view_individual = tk.Button(root, text="View Record", command=view_individual_student, bg='black', fg='green')
btn_view_individual.grid(row=2, column=1, padx=10, pady=5)

# Text area to display the output
text_area = tk.Text(root, height=15, width=60, bg='black', fg='green', borderwidth=2, relief='solid')
text_area.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
