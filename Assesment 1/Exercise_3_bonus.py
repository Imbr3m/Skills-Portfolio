import tkinter as tk
from tkinter import *

# create tkinter root
root = Tk()
root.title("Student Manager")

# sets the background color of the root window
root.configure(bg='black')

# FUNCTIONSS
# reads and parse the data from studentMarks.txt
def load_student_data():
    # Open the studentMarks.txt file for reading
    with open("Assesment 1\Assets\studentMarksBonus.txt", "r") as file:
        students = []  #create an empty list to store student data
        
        #readss the number of students from the first line
        num_students = int(file.readline().strip())
        
        # Loops through each line in the file to read student records
        for line in file:
            parts = line.strip().split(',')  # splits by commas
            
            # Extract student information from parts
            student_number = int(parts[0])  # cconverts the first part to an integer
            student_name = parts[1]         #second part is the name
            coursework_marks = list(map(int, parts[2:5]))  # convert again to int
            
            # calculate the total courseworrk score
            coursework_total = sum(coursework_marks)
            exam_mark = int(parts[5])  # Convert the exam mark to an integer
            
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

def view_individual_student():
    #gets the student name from dropdown
    selected = student_var.get()

    # loop through klist to find name
    for student in students:
        if student['name'] == selected:
            # formats the student's details into a string
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
    display_student_info(top_student)

def show_lowest_score():
    low_student = min(students, key=lambda s: s['percentage']) # same as the other one but this one displays the low student
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
    text_area.config(state=NORMAL)
    text_area.delete(1.0, END)
    text_area.insert(END, output)
    text_area.config(state=DISABLED)

def sort_students(order):
    students.sort(key=lambda s: s['percentage'], reverse=(order == "Descending"))
    view_all_students()



# ADD STUDDDNT FUNTION
def add_student():
    # creates a new window to input data
    def tkinter_new_student():
        name = entry_name.get()
        number = int(entry_number.get())
        coursework_marks = [int(entry_mark1.get()), int(entry_mark2.get()), int(entry_mark3.get())]
        exam_mark = int(entry_exam.get())

        coursework_total = sum(coursework_marks)
        overall_percentage = ((coursework_total + exam_mark) / 160) * 100
        grade = student_score_level(overall_percentage)

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

    add_window = Toplevel(root)#opens a new tkinter window
    add_window.title("Add Student")
    add_window.configure(bg='black')#change bg color

    # some labels and buttons
    Label(add_window, text="Name:", bg='black', fg='green').grid(row=0, column=0)
    entry_name = Entry(add_window, bg='black', fg='green')  
    entry_name.grid(row=0, column=1)

    Label(add_window, text="Number:", bg='black', fg='green').grid(row=1, column=0)
    entry_number = Entry(add_window, bg='black', fg='green')  
    entry_number.grid(row=1, column=1)

    Label(add_window, text="Coursework Mark 1:", bg='black', fg='green').grid(row=2, column=0)
    entry_mark1 = Entry(add_window, bg='black', fg='green')  
    entry_mark1.grid(row=2, column=1)

    Label(add_window, text="Coursework Mark 2:", bg='black', fg='green').grid(row=3, column=0)
    entry_mark2 = Entry(add_window, bg='black', fg='green')  
    entry_mark2.grid(row=3, column=1)

    Label(add_window, text="Coursework Mark 3:", bg='black', fg='green').grid(row=4, column=0)
    entry_mark3 = Entry(add_window, bg='black', fg='green')  
    entry_mark3.grid(row=4, column=1)

    Label(add_window, text="Exam Mark:", bg='black', fg='green').grid(row=5, column=0)
    entry_exam = Entry(add_window, bg='black', fg='green')  
    entry_exam.grid(row=5, column=1)

    Button(add_window, text="Submit", command=tkinter_new_student, bg='green', fg='black').grid(row=6, columnspan=2)  # Set Button background and text color

# DELETTE STUDENT FUNCTION
def delete_student():
    # i remve the selected student from the list and update the display
    selected = student_var.get()
    global students
    students = [student for student in students if student['name'] != selected]
    save_students()
    view_all_students()

# UPDATE STUDENT FUNCTION
def update_student():
    selected = student_var.get()  #gets the name of the selected student from the dropdown
    for student in students:
        if student['name'] == selected:
            
            update_window = Toplevel(root) 
            #createss a new window for updating student details
            update_window.title("Update Student")
            update_window.configure(bg='black')  #bg

            # labels, entrys and buttoon
            Label(update_window, text="Update Name:", bg='black', fg='green').grid(row=0, column=0)
            entry_name = Entry(update_window, bg='black', fg='green')
            entry_name.insert(0, student['name'])  # fill in the currnt name so the user can edit it
            entry_name.grid(row=0, column=1)

            # label and entry for updating the student's number
            Label(update_window, text="Update Number:", bg='black', fg='green').grid(row=1, column=0)
            entry_number = Entry(update_window, bg='black', fg='green')
            entry_number.insert(0, student['number'])  # pre-fill with the current student number
            entry_number.grid(row=1, column=1)

            # labels and entries for coursework marks
            Label(update_window, text="Update Coursework Mark 1:", bg='black', fg='green').grid(row=2, column=0)
            entry_mark1 = Entry(update_window, bg='black', fg='green')
            entry_mark1.insert(0, student['coursework'] // 3)  #distribute current coursework equally for editing
            entry_mark1.grid(row=2, column=1)

            Label(update_window, text="Update Coursework Mark 2:", bg='black', fg='green').grid(row=3, column=0)
            entry_mark2 = Entry(update_window, bg='black', fg='green')
            entry_mark2.insert(0, student['coursework'] // 3)  
            entry_mark2.grid(row=3, column=1)

            Label(update_window, text="Update Coursework Mark 3:", bg='black', fg='green').grid(row=4, column=0)
            entry_mark3 = Entry(update_window, bg='black', fg='green')
            entry_mark3.insert(0, student['coursework'] // 3)  
            entry_mark3.grid(row=4, column=1)

            # label and entry for the exam mark
            Label(update_window, text="Update Exam Mark:", bg='black', fg='green').grid(row=5, column=0)
            entry_exam = Entry(update_window, bg='black', fg='green')
            entry_exam.insert(0, student['exam'])  
            entry_exam.grid(row=5, column=1)

            #button function to handle what happens when the user submits the updated info
            def submit_update():
                # updates the old data with the new one
                student['name'] = entry_name.get() 
                student['number'] = int(entry_number.get())  
                coursework_marks = [int(entry_mark1.get()), int(entry_mark2.get()), int(entry_mark3.get())]  
                student['coursework'] = sum(coursework_marks)  
                student['exam'] = int(entry_exam.get())  
                student['percentage'] = ((student['coursework'] + student['exam']) / 160) * 100 
                student['grade'] = student_score_level(student['percentage'])  
                save_students() 
                update_window.destroy()  # close the update window
                view_all_students()  #refreshing the displayed list of students to show the new studen


            Button(update_window, text="Submit", command=submit_update, bg='black', fg='green').grid(row=6,columnspan=2)
            return  #exit the function after setting up the update window

# SAVE STUDENT
def save_students():
    # overwtires and saves the txt file
    with open("Assets/studentMarksBonus.txt", "w") as file:
        file.write(f"{len(students)}\n")
        for student in students:
            file.write(f"{student['number']},{student['name']},{student['coursework']},{student['exam']}\n")


# TKINTERR

# made a variable to load the data
students = load_student_data()

#title
title_label = Label(root, text="Student Manager", font=("Arial", 16, "bold"), bg='black', fg='green')
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# buttons for different functionalities
btn_view_all = Button(root, text="View All Student Records", command=view_all_students, bg='black', fg='green')
btn_view_all.grid(row=1, column=0, padx=10, pady=5)

btn_highest = Button(root, text="Show Highest Score", command=show_highest_score, bg='black', fg='green')
btn_highest.grid(row=1, column=1, padx=10, pady=5)

btn_lowest = Button(root, text="Show Lowest Score", command=show_lowest_score, bg='black', fg='green')
btn_lowest.grid(row=1, column=2, padx=10, pady=5)

# a frame to hold the names of students to choose 
frame = Frame(root, bg='green')
frame.grid(row=2, column=0, padx=10, pady=5)

# Variable to hold the selected student name
student_var = StringVar()

# Drop down for selecting the students
student_menu = OptionMenu(frame, student_var, *[s['name'] for s in students])
student_menu.config(bg='black', fg='green', activebackground='green', activeforeground='black', borderwidth=0, highlightbackground='green')
student_menu["menu"].config(bg='black', fg='green')
student_menu.pack()

# view student btn
student_view_button = Button(root, text="View Record", command=view_individual_student, bg='black', fg='green')
student_view_button.grid(row=2, column=1, padx=10, pady=5)

ascending_students = Button(root, text="Sort Ascending", command=lambda: sort_students("Ascending"), bg='black', fg='green')
ascending_students.grid(row=3, column=0, padx=10, pady=5)

descending_students = Button(root, text="Sort Descending", command=lambda: sort_students("Descending"), bg='black', fg='green')
descending_students.grid(row=3, column=1, padx=10, pady=5)

adding_students = Button(root, text="Add Student Record", command=add_student, bg='black', fg='green')
adding_students.grid(row=3, column=2, padx=10, pady=5)

deleting_students = Button(root, text="Delete Student Record", command=delete_student, bg='black', fg='green')
deleting_students.grid(row=4, column=0, padx=10, pady=5)

updating_students = Button(root, text="Update Student Record", command=update_student, bg='black', fg='green')
updating_students.grid(row=4, column=1, padx=10, pady=5)

# text area for the outputt
text_area = Text(root, height=15, width=60, bg='black', fg='green', borderwidth=2, relief='solid')
text_area.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
