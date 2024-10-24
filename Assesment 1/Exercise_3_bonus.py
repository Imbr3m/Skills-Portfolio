import tkinter as tk
from tkinter import messagebox, ttk

# Create the main Tkinter root
root = tk.Tk()
root.title("Student Manager")
root.configure(bg='black')

# FUNCTIONSS

# Read and parse the data from studentMarksBonus.txt
def load_student_data():
    # Open the studentMarksBonus.txt file for reading
    with open("Assets/studentMarksBonus.txt", "r") as file:
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
            grade = calculate_grade(overall_percentage)
            
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

def calculate_grade(percentage):
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

def sort_students(order):
    students.sort(key=lambda s: s['percentage'], reverse=(order == "Descending"))
    view_all_students()

def add_student():
    def submit_new_student():
        name = entry_name.get()
        number = int(entry_number.get())
        coursework_marks = [int(entry_mark1.get()), int(entry_mark2.get()), int(entry_mark3.get())]
        exam_mark = int(entry_exam.get())

        coursework_total = sum(coursework_marks)
        overall_percentage = ((coursework_total + exam_mark) / 160) * 100
        grade = calculate_grade(overall_percentage)

        new_student = {
            "number": number,
            "name": name,
            "coursework": coursework_total,
            "exam": exam_mark,
            "percentage": overall_percentage,
            "grade": grade
        }

        students.append(new_student)
        save_students()
        add_window.destroy()
        view_all_students()

    add_window = tk.Toplevel(root)
    add_window.title("Add Student")

    tk.Label(add_window, text="Name:").grid(row=0, column=0)
    entry_name = tk.Entry(add_window)
    entry_name.grid(row=0, column=1)

    tk.Label(add_window, text="Number:").grid(row=1, column=0)
    entry_number = tk.Entry(add_window)
    entry_number.grid(row=1, column=1)

    tk.Label(add_window, text="Coursework Mark 1:").grid(row=2, column=0)
    entry_mark1 = tk.Entry(add_window)
    entry_mark1.grid(row=2, column=1)

    tk.Label(add_window, text="Coursework Mark 2:").grid(row=3, column=0)
    entry_mark2 = tk.Entry(add_window)
    entry_mark2.grid(row=3, column=1)

    tk.Label(add_window, text="Coursework Mark 3:").grid(row=4, column=0)
    entry_mark3 = tk.Entry(add_window)
    entry_mark3.grid(row=4, column=1)

    tk.Label(add_window, text="Exam Mark:").grid(row=5, column=0)
    entry_exam = tk.Entry(add_window)
    entry_exam.grid(row=5, column=1)

    tk.Button(add_window, text="Submit", command=submit_new_student).grid(row=6, columnspan=2)

def delete_student():
    selected = student_var.get()
    global students
    students = [student for student in students if student['name'] != selected]
    save_students()
    view_all_students()

def update_student():
    selected = student_var.get()
    for student in students:
        if student['name'] == selected:
            update_window = tk.Toplevel(root)
            update_window.title("Update Student")

            tk.Label(update_window, text="Update Name:").grid(row=0, column=0)
            entry_name = tk.Entry(update_window)
            entry_name.insert(0, student['name'])
            entry_name.grid(row=0, column=1)

            tk.Label(update_window, text="Update Number:").grid(row=1, column=0)
            entry_number = tk.Entry(update_window)
            entry_number.insert(0, student['number'])
            entry_number.grid(row=1, column=1)

            tk.Label(update_window, text="Update Coursework Mark 1:").grid(row=2, column=0)
            entry_mark1 = tk.Entry(update_window)
            entry_mark1.insert(0, student['coursework'] // 3)  # Assuming equal distribution
            entry_mark1.grid(row=2, column=1)

            tk.Label(update_window, text="Update Coursework Mark 2:").grid(row=3, column=0)
            entry_mark2 = tk.Entry(update_window)
            entry_mark2.insert(0, student['coursework'] // 3)
            entry_mark2.grid(row=3, column=1)

            tk.Label(update_window, text="Update Coursework Mark 3:").grid(row=4, column=0)
            entry_mark3 = tk.Entry(update_window)
            entry_mark3.insert(0, student['coursework'] // 3)
            entry_mark3.grid(row=4, column=1)

            tk.Label(update_window, text="Update Exam Mark:").grid(row=5, column=0)
            entry_exam = tk.Entry(update_window)
            entry_exam.insert(0, student['exam'])
            entry_exam.grid(row=5, column=1)

            def submit_update():
                student['name'] = entry_name.get()
                student['number'] = int(entry_number.get())
                coursework_marks = [int(entry_mark1.get()), int(entry_mark2.get()), int(entry_mark3.get())]
                student['coursework'] = sum(coursework_marks)
                student['exam'] = int(entry_exam.get())
                student['percentage'] = ((student['coursework'] + student['exam']) / 160) * 100
                student['grade'] = calculate_grade(student['percentage'])
                save_students()
                update_window.destroy()
                view_all_students()

            tk.Button(update_window, text="Submit", command=submit_update).grid(row=6, columnspan=2)
            return

def save_students():
    with open("Assets/studentMarksBonus.txt", "w") as file:
        file.write(f"{len(students)}\n")
        for student in students:
            file.write(f"{student['number']},{student['name']},{student['coursework']},{student['exam']}\n")

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

frame = tk.Frame(root, bg='green')
frame.grid(row=2, column=0, padx=10, pady=5)

student_var = tk.StringVar()
student_menu = tk.OptionMenu(frame, student_var, *[s['name'] for s in students])
student_menu.config(bg='black', fg='green', activebackground='green', activeforeground='black', borderwidth=0, highlightbackground='green')
student_menu["menu"].config(bg='black', fg='green')
student_menu.pack()

btn_view_individual = tk.Button(root, text="View Record", command=view_individual_student, bg='black', fg='green')
btn_view_individual.grid(row=2, column=1, padx=10, pady=5)

btn_sort_asc = tk.Button(root, text="Sort Ascending", command=lambda: sort_students("Ascending"), bg='black', fg='green')
btn_sort_asc.grid(row=3, column=0, padx=10, pady=5)

btn_sort_desc = tk.Button(root, text="Sort Descending", command=lambda: sort_students("Descending"), bg='black', fg='green')
btn_sort_desc.grid(row=3, column=1, padx=10, pady=5)

btn_add_student = tk.Button(root, text="Add Student Record", command=add_student, bg='black', fg='green')
btn_add_student.grid(row=3, column=2, padx=10, pady=5)

btn_delete_student = tk.Button(root, text="Delete Student Record", command=delete_student, bg='black', fg='green')
btn_delete_student.grid(row=4, column=0, padx=10, pady=5)

btn_update_student = tk.Button(root, text="Update Student Record", command=update_student, bg='black', fg='green')
btn_update_student.grid(row=4, column=1, padx=10, pady=5)

text_area = tk.Text(root, height=15, width=60, bg='black', fg='green', borderwidth=2, relief='solid')
text_area.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
