import tkinter as tk
from tkinter import *

# create tkinter root
root = Tk()
root.title("Student Manager")

# sets the background color of the root window
root.configure(bg='black')

#FUNCTIONSS
# reads and parse the data from studentMarks.txt
def load_student_data():
    # Open the studentMarks.txt file for reading
    with open("Assesment 1\Assets\studentMarks.txt", "r") as file:
        students = []  #create an empty list to store student data
        
        #readss the number of students from the first line
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
            exam_mark = int(parts[5])  # Converts the exam mark to an integer
            
            #overall percentage
            overall_percentage = ((coursework_total + exam_mark) / 160) * 100
            
            # gives the grade based on percentage
            grade = student_score_level(overall_percentage)
            
            # dictuionary for the record
            student_record = {
                "number": student_number,
                "name": student_name,
                "coursework": coursework_total,
                "exam": exam_mark,
                "percentage": overall_percentage,
                "grade": grade
            }
            
            # adds the information of student record to a list
            students.append(student_record)  
            
    return students  # Return the list of student records

# function to calculate the grade
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
    
    # loops through tge list of students to format their details
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

def view_student():
    #gets the student name from dropdown
    selected = student_var.get()

    # loop through klist to find name
    for student in students:
        if student['name'] == selected:
            # Format the student's details into a string
            output = (
                f"Name: {student['name']}\n"
                f"Number: {student['number']}\n"
                f"Coursework Total: {student['coursework']}\n"
                f"Exam Mark: {student['exam']}\n"
                f"Overall Percentage: {student['percentage']:.2f}%\n"
                f"Grade: {student['grade']}\n"
            )
            # then displays the records od that student
            display_output(output)
            return


def show_highest_score():
    # lamba looks at each student in the students list and uses the value percentage to compare
    top_student = max(students, key=lambda s: s['percentage']) #here it looks at the biggest prercentage and displyas the top student
    display_record(top_student)

def show_lowest_score():
    low_student = min(students, key=lambda s: s['percentage']) # same as the other one but this one displays the low student
    display_record(low_student)

def display_record(student):
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
    # enebles the editing
    text_area.config(state=NORMAL)
    #deletes any content if theres any
    text_area.delete(1.0, END)
    # inserts a new output
    text_area.insert(END, output)
    # disable the editing
    text_area.config(state=DISABLED)

# TKINTERR

# made a variable to load the data
students = load_student_data()

# title
title_label = Label(root, text="Student Manager", font=("Arial", 16, "bold"), bg='black', fg='green')
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# buttons for different functionalities
btn_view_all = Button(root, text="View All Student Records", command= view_all_students, bg='black', fg='green')
btn_view_all.grid(row=1, column=0, padx=10, pady=5)

btn_highest = Button(root, text="Show Highest Score", command= show_highest_score, bg='black', fg='green')
btn_highest.grid(row=1, column=1, padx=10, pady=5)

btn_lowest = Button(root, text="Show Lowest Score", command= show_lowest_score, bg='black', fg='green')
btn_lowest.grid(row=1, column=2, padx=10, pady=5)

# a frame to hold the names of students to choose 
frame = Frame(root, bg='green')
frame.grid(row=2, column=0, padx=10, pady=5)

# Variable to hold the selected student name
student_var = StringVar()

# Drop down for selecting the students
student_menu = OptionMenu(frame, student_var, *[s['name'] for s in students])
student_menu.config(bg='black', fg='green', activebackground='green', activeforeground='black', borderwidth=0, highlightbackground= 'green')
student_menu["menu"].config(bg='black', fg='green') #for changing the color of the box
student_menu.pack()

# view student btn
student_vuew_button = Button(root, text="View Record", command= view_student, bg='black', fg='green')
student_vuew_button.grid(row=2, column=1, padx=10, pady=5)

# text area for the outputt
text_area = Text(root, height=15, width=60, bg='black', fg='green', borderwidth=2, relief='solid')
text_area.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
