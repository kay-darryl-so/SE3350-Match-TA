# GUI for Undergraduate Chair

import tkinter as tk
from tkinter import filedialog, Text
from tkinter import*
from calculateTAHours import calculateHours
from adjustTAHours import viewHours, viewList, adjustHours
import pandas as pd
import os

def TAHours():

    frame = tk.Frame(ms, bg='#f3e6ff')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    label1 = tk.Label(frame, text="Select the year for which you would like to view or adjust calculated TA hours:", bg='#f3e6ff', font=('Calibri',18))
    label1.place(relx=0.12, rely=0.2, relwidth=0.8, relheight=0.1)

    global years
    years = ['Select an option', '2020-2019', '2019-2018']
    global menu
    menu = StringVar(frame)
    menu.set(years[0])
    menuLabel = OptionMenu(frame, menu, *years)
    menuLabel.place(relx=0.25, rely=0.3, relwidth=0.3, relheight=0.1)

    button1 = tk.Button(frame, text='Go', command=TAAllocations)
    button1.place(relx=0.6, rely=0.32, relwidth=0.1, relheight=0.07)

    label2 = tk.Label(frame, text='Calculate TA Hours for a new school year:', bg='#f3e6ff', font=('Calibri',18))
    label2.place(relx=0.12, rely=0.5, relwidth = 0.8, relheight=0.1)

    upload = tk.Button(frame, text='Upload CSV File', command=uploadFile)
    upload.place(relx=0.45, rely=0.6, relwidth = 0.15, relheight=0.07)

    back = tk.Button(frame, text='< Previous Page', bg='#f3e6ff', command=mainScreen)
    back.place(relx=0.01, rely=0.01, relwidth=0.12, relheight=0.05)


def uploadFile():
    fn = filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=(('.csv', "*.csv"),('all files', '*.*')))

    calculate = calculateHours(fn)
    years.insert(1, '2020-2021')

    frame = tk.Frame(ms, bg='#f3e6ff')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    viewResults = ''

    for i in calculate:
        viewResults = viewResults + str(i) + '\n\n'

    heading = tk.Label(frame, text=menu.get() + ' Courses and Allocated TA Hours', bg='#f3e6ff', font=('Calibri',18))
    heading.place(relx=0.12, rely=0.2, relwidth=0.8, relheight=0.1)

    results = tk.Label(frame, text=viewResults)
    results.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.45)

    editButton = tk.Button(frame, text='Edit Hours', command=editHoursInput)
    editButton.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.1)

    back = tk.Button(frame, text='< Home', bg='#f3e6ff', command=mainScreen)
    back.place(relx=0.01, rely=0.01, relwidth=0.12, relheight=0.05)


def TAAllocations():
    global selected
    selected = menu.get() + '.csv'
    frame = tk.Frame(ms, bg='#f3e6ff')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    view = viewHours(selected)

    heading = tk.Label(frame, text=menu.get() + ' Courses and Allocated TA Hours', bg='#f3e6ff', font=('Calibri',18))
    heading.place(relx=0.12, rely=0.2, relwidth=0.8, relheight=0.1)

    results = tk.Label(frame, text=view)
    results.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.45)

    editButton = tk.Button(frame, text='Edit Hours', command=editHoursInput)
    editButton.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.1)

    back = tk.Button(frame, text='< Home', bg='#f3e6ff', command=mainScreen)
    back.place(relx=0.01, rely=0.01, relwidth=0.12, relheight=0.05)


def editHoursInput():
    global screen1
    screen1 = Toplevel(ms)
    screen1.title("Edit TA Hours")
    screen1.geometry("500x300")

    hours = StringVar()

    global hoursEntry

    label1 = tk.Label(screen1, text = "Which course would you like to edit?")
    label1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.2)

    global courses
    courses = []
    hoursList = viewList(selected)
    courses.insert(0, 'Select a course')

    a = 0
    b = 0
    for i in hoursList:
        courses.append(hoursList[a][b])
        a += 1

    global options
    options = StringVar(screen1)
    options.set(courses[0])
    coursesLabel = OptionMenu(screen1, options, *courses)
    coursesLabel.place(relx=0.25, rely=0.3, relwidth=0.4, relheight=0.1)

    label2 = tk.Label(screen1, text='Enter the new number of hours: ')
    label2.place(relx=0.15, rely=0.4, relwidth=0.6, relheight=0.1)

    hoursEntry = tk.Entry(screen1, textvariable=hours)
    hoursEntry.place(relx=0.25, rely=0.5, relwidth=0.3, relheight=0.1)

    adjustButton = tk.Button(screen1, text='Adjust', command=editHours)
    adjustButton.place(relx=0.45, rely=0.6, relwidt=0.1, relheight=0.1)


def editHours():
    result = adjustHours(selected, options.get(), hoursEntry.get())
    if (not result):
        resultLabel1 = tk.Label(screen1, text='Failed to save.', fg='#cc0000')
        resultLabel1.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.1)
    else:
        resultLabel = tk.Label(screen1, text='Changes successfully saved.', fg='#008000')
        resultLabel.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.1)


def mainScreen():
    global ms
    ms = tk.Tk()
    ms.title("TA-Course Matching System")

    canvas = tk.Canvas(ms, height=900, width=1200, bg="#ffffff")
    canvas.pack()

    frame = tk.Frame(ms, bg='#f3e6ff')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    label = tk.Label(frame, text="Select a function", bg='#f3e6ff', font=('Calibri',18))
    label.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.1)

    TAhours = tk.Button(frame, text="Calculate/Adjust TA Hours", command=TAHours)
    TAhours.place(relx=0.225, rely=0.5, relwidth=0.25, relheight=0.15)

    TAallocations = tk.Button(frame, text="View/Edit TA Allocations")
    TAallocations.place(relx=0.525, rely=0.5, relwidth=0.25, relheight=0.15)

    ms.mainloop()
