# Main GUI for this system.

import tkinter as tk
from tkinter import*
import pandas as pd
import chairGUI
import departmentGUI
import facultyGUI
import instructorGUI


def instructorLogin():
    global screen1
    screen1 = Toplevel(m)
    screen1.title("Instructor Login")
    screen1.geometry("500x300")

    username = StringVar()
    password = StringVar()

    global usernameEntry
    global passwordEntry

    label = tk.Label(screen1, text = "Please enter your UWO login credentials")
    label.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.2)

    usernameLabel = tk.Label(screen1, text="Username: ")
    usernameLabel.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.1)
    usernameEntry = tk.Entry(screen1, textvariable=username)
    usernameEntry.place(relx=0.3, rely=0.3, relwidth=0.5, relheight=0.1)

    passwordLabel = tk.Label(screen1, text="Password: ")
    passwordLabel.place(relx=0.1, rely=0.425, relwidth=0.2, relheight=0.1)
    passwordEntry = tk.Entry(screen1, textvariable=password, show='*')
    passwordEntry.place(relx=0.3, rely=0.425, relwidth=0.5, relheight=0.1)

    loginButton = tk.Button(screen1, text="Login", width=10, height=1, command=verifyInstructor)
    loginButton.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.15)

def chairLogin():
    global screen1
    screen1 = Toplevel(m)
    screen1.title("Undergraduate Chair Login")
    screen1.geometry("500x300")

    username = StringVar()
    password = StringVar()

    global usernameEntry
    global passwordEntry

    label = tk.Label(screen1, text = "Please enter your UWO login credentials")
    label.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.2)

    usernameLabel = tk.Label(screen1, text="Username: ")
    usernameLabel.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.1)
    usernameEntry = tk.Entry(screen1, textvariable=username)
    usernameEntry.place(relx=0.3, rely=0.3, relwidth=0.5, relheight=0.1)

    passwordLabel = tk.Label(screen1, text="Password: ")
    passwordLabel.place(relx=0.1, rely=0.425, relwidth=0.2, relheight=0.1)
    passwordEntry = tk.Entry(screen1, textvariable=password, show='*')
    passwordEntry.place(relx=0.3, rely=0.425, relwidth=0.5, relheight=0.1)

    loginButton = tk.Button(screen1, text="Login", width=10, height=1, command=verifyChair)
    loginButton.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.15)

def departmentLogin():
    global screen1
    screen1 = Toplevel(m)
    screen1.title("Department Login")
    screen1.geometry("500x300")

    username = StringVar()
    password = StringVar()

    global usernameEntry
    global passwordEntry

    label = tk.Label(screen1, text = "Please enter your UWO login credentials")
    label.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.2)

    usernameLabel = tk.Label(screen1, text="Username: ")
    usernameLabel.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.1)
    usernameEntry = tk.Entry(screen1, textvariable=username)
    usernameEntry.place(relx=0.3, rely=0.3, relwidth=0.5, relheight=0.1)

    passwordLabel = tk.Label(screen1, text="Password: ")
    passwordLabel.place(relx=0.1, rely=0.425, relwidth=0.2, relheight=0.1)
    passwordEntry = tk.Entry(screen1, textvariable=password, show='*')
    passwordEntry.place(relx=0.3, rely=0.425, relwidth=0.5, relheight=0.1)

    loginButton = tk.Button(screen1, text="Login", width=10, height=1, command=verifyDepartment)
    loginButton.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.15)

def facultyLogin():
    global screen1
    screen1 = Toplevel(m)
    screen1.title("Faculty Login")
    screen1.geometry("500x300")

    username = StringVar()
    password = StringVar()

    global usernameEntry
    global passwordEntry

    label = tk.Label(screen1, text = "Please enter your UWO login credentials")
    label.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.2)

    usernameLabel = tk.Label(screen1, text="Username: ")
    usernameLabel.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.1)
    usernameEntry = tk.Entry(screen1, textvariable=username)
    usernameEntry.place(relx=0.3, rely=0.3, relwidth=0.5, relheight=0.1)

    passwordLabel = tk.Label(screen1, text="Password: ")
    passwordLabel.place(relx=0.1, rely=0.425, relwidth=0.2, relheight=0.1)
    passwordEntry = tk.Entry(screen1, textvariable=password, show='*')
    passwordEntry.place(relx=0.3, rely=0.425, relwidth=0.5, relheight=0.1)

    loginButton = tk.Button(screen1, text="Login", width=10, height=1, command=verifyFaculty)
    loginButton.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.15)

def verifyInstructor():
    df = pd.read_csv('instructorCredentials.csv')
    dict = df.to_dict(orient='list')
    usernames = dict['Username']
    passwords = dict['Password']

    if usernameEntry.get() in usernames:
        if passwordEntry.get() == passwords[(usernames.index(usernameEntry.get()))]:
            success = tk.Label(screen1, text="Login successful", fg='#008000')
            success.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.1)
            screen1.destroy()
            m.destroy()
            instructorGUI.mainScreen()
        else:
            fail = tk.Label(screen1, text="Invalid login", fg='#cc0000')
            fail.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.1)
    else:
        fail = tk.Label(screen1, text="Invalid login", fg='#cc0000')
        fail.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.1)

def verifyChair():
    df = pd.read_csv('chairCredentials.csv')
    dict = df.to_dict(orient='list')
    usernames = dict['Username']
    passwords = dict['Password']

    if usernameEntry.get() in usernames:
        if passwordEntry.get() == passwords[(usernames.index(usernameEntry.get()))]:
            success = tk.Label(screen1, text="Login successful", fg='#008000')
            success.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.1)
            screen1.destroy()
            m.destroy()
            chairGUI.mainScreen()
        else:
            fail = tk.Label(screen1, text="Invalid login", fg='#cc0000')
            fail.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.1)
    else:
        fail = tk.Label(screen1, text="Invalid login", fg='#cc0000')
        fail.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.1)

def verifyDepartment():
    df = pd.read_csv('departmentCredentials.csv')
    dict = df.to_dict(orient='list')
    usernames = dict['Username']
    passwords = dict['Password']

    if usernameEntry.get() in usernames:
        if passwordEntry.get() == passwords[(usernames.index(usernameEntry.get()))]:
            success = tk.Label(screen1, text="Login successful", fg='#008000')
            success.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.1)
            screen1.destroy()
            m.destroy()
            departmentGUI.mainScreen()
        else:
            fail = tk.Label(screen1, text="Invalid login", fg='#cc0000')
            fail.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.1)
    else:
        fail = tk.Label(screen1, text="Invalid login", fg='#cc0000')
        fail.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.1)

def verifyFaculty():
    df = pd.read_csv('facultyCredentials.csv')
    dict = df.to_dict(orient='list')
    usernames = dict['Username']
    passwords = dict['Password']

    if usernameEntry.get() in usernames:
        if passwordEntry.get() == passwords[(usernames.index(usernameEntry.get()))]:
            success = tk.Label(screen1, text="Login successful", fg='#008000')
            success.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.1)
            screen1.destroy()
            m.destroy()
            facultyGUI.mainScreen()
        else:
            fail = tk.Label(screen1, text="Invalid login", fg='#cc0000')
            fail.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.1)
    else:
        fail = tk.Label(screen1, text="Invalid login", fg='#cc0000')
        fail.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.1)

def loginScreen():
    global m
    m = tk.Tk()
    m.title("TA-Course Matching System Login")

    canvas = tk.Canvas(m, height=900, width=1200, bg="#ffffff")
    canvas.pack()

    frame = tk.Frame(m, bg='#f3e6ff')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    label = tk.Label(frame, text="Select your affiliate group", bg='#f3e6ff')
    label.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.1)

    instructor = tk.Button(frame, text="Instructor", command=instructorLogin)
    instructor.place(relx=0.1, rely=0.5, relwidth=0.15, relheight=0.1)

    department = tk.Button(frame, text="Department", command=departmentLogin)
    department.place(relx=0.3, rely=0.5, relwidth=0.15, relheight=0.1)

    chair = tk.Button(frame, text="Undergrad Chair", command=chairLogin)
    chair.place(relx=0.5, rely=0.5, relwidth=0.15, relheight=0.1)

    faculty = tk.Button(frame, text="Faculty", command=facultyLogin)
    faculty.place(relx=0.7, rely=0.5, relwidth=0.15, relheight=0.1)

    m.mainloop()


loginScreen()
