# GUI for Undergraduate Chair

import tkinter as tk
from tkinter import filedialog, ttk
from tkinter import*
from calculateTAHours import calculateHours
from adjustTAHours import viewHours, viewList
from editTAHours import editTAHours
from matchTA import matchTA


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
    heading.place(relx=0.12, rely=0.1, relwidth=0.8, relheight=0.1)

    global tree
    tree = ttk.Treeview(frame)
    tree["columns"]=("Course","Hours")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Course", width=150, minwidth=150, stretch=tk.NO)
    tree.column("Hours", width=250, minwidth=270, stretch=tk.NO)

    tree.heading("Course",text="Course",anchor=tk.W)
    tree.heading("Hours", text="Hours",anchor=tk.W)

    count = 0
    for i in calculate:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1]))
        count = count + 1

    tree.place(relx=0.35, rely=0.2)

    #Labels
    courseLabel = tk.Label(frame, text='Course', bg='#f3e6ff')
    courseLabel.place(relx=0.12, rely=0.6, relwidth=0.1, relheight=0.05)

    hoursLabel = tk.Label(frame, text='Hours', bg='#f3e6ff')
    hoursLabel.place(relx=0.5, rely=0.6, relwidth=0.1, relheight=0.05)

    #Entries
    global courseEntry
    global hoursEntry
    courseEntry = tk.Entry(frame)
    courseEntry.place(relx=0.12, rely=0.65, relwidth=0.4, relheight=0.05)

    hoursEntry = tk.Entry(frame)
    hoursEntry.place(relx=0.5, rely=0.65, relwidth=0.4, relheight=0.05)

    #Buttons
    selectButton = tk.Button(frame, text='Select Record to Update', command=selectHour)
    selectButton.place(relx=0.15, rely=0.8, relwidth=0.35, relheight=0.05)

    updateButton = tk.Button(frame, text='Save Update', command=updateHour)
    updateButton.place(relx=0.55, rely=0.8, relwidth=0.2, relheight=0.05)

    back = tk.Button(frame, text='< Home', bg='#f3e6ff', command=mainScreen)
    back.place(relx=0.01, rely=0.01, relwidth=0.12, relheight=0.05)

def selectHour():
    #Clear Entry Boxes
    courseEntry.delete(0, tk.END)
    hoursEntry.delete(0, tk.END)

    selected = tree.focus()
    values = tree.item(selected, 'values')

    #Output to Entry Boxes
    courseEntry.insert(0, values[0])
    hoursEntry.insert(0, values[1])

def updateHour():
    selected = tree.focus()
    tree.item(selected, text='', values=(courseEntry.get(), hoursEntry.get()))


def TAAllocations():
    global selected
    selected = menu.get() + '.csv'
    frame = tk.Frame(ms, bg='#f3e6ff')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    view = viewHours(selected)

    heading = tk.Label(frame, text=menu.get() + ' Courses and Allocated TA Hours', bg='#f3e6ff', font=('Calibri',18))
    heading.place(relx=0.12, rely=0.1, relwidth=0.8, relheight=0.1)

    global tree
    tree = ttk.Treeview(frame)
    tree["columns"]=("Course","Hours")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Course", width=150, minwidth=150, stretch=tk.NO)
    tree.column("Hours", width=250, minwidth=270, stretch=tk.NO)

    tree.heading("Course",text="Course",anchor=tk.W)
    tree.heading("Hours", text="Hours",anchor=tk.W)

    count = 0
    for i in view:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1]))
        count = count + 1

    tree.place(relx=0.35, rely=0.2)

    #Labels
    courseLabel = tk.Label(frame, text='Course', bg='#f3e6ff')
    courseLabel.place(relx=0.12, rely=0.6, relwidth=0.1, relheight=0.05)

    hoursLabel = tk.Label(frame, text='Hours', bg='#f3e6ff')
    hoursLabel.place(relx=0.5, rely=0.6, relwidth=0.1, relheight=0.05)

    #Entries
    global courseEntry
    global hoursEntry
    courseEntry = tk.Entry(frame)
    courseEntry.place(relx=0.12, rely=0.65, relwidth=0.4, relheight=0.05)

    hoursEntry = tk.Entry(frame)
    hoursEntry.place(relx=0.5, rely=0.65, relwidth=0.4, relheight=0.05)

    #Buttons
    selectButton = tk.Button(frame, text='Select Record to Update', command=selectHour)
    selectButton.place(relx=0.15, rely=0.8, relwidth=0.35, relheight=0.05)

    updateButton = tk.Button(frame, text='Save Update', command=updateHour)
    updateButton.place(relx=0.55, rely=0.8, relwidth=0.2, relheight=0.05)

    back = tk.Button(frame, text='< Home', bg='#f3e6ff', command=mainScreen)
    back.place(relx=0.01, rely=0.01, relwidth=0.12, relheight=0.05)


def editHoursInput():

    global screen1
    screen1 = Toplevel(ms)
    screen1.title("Edit TA Hours")
    screen1.geometry("500x300")

    global hours
    hours = StringVar()

    label1 = tk.Label(screen1, text = "Which course would you like to edit?")
    label1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.2)

    global courses
    courses = []
    selected = menu.get() + '.csv'
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
    result = editTAHours(selected, options.get(), hours)
    if (not result):
        resultLabel1 = tk.Label(screen1, text='Failed to save.', fg='#cc0000')
        resultLabel1.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.1)
    else:
        resultLabel = tk.Label(screen1, text='Changes successfully saved.', fg='#008000')
        resultLabel.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.1)

def editAllocations():
    global frame2
    frame2 = tk.Frame(ms, bg='#f3e6ff')
    frame2.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    label1 = tk.Label(frame2, text= 'Match Results', bg='#f3e6ff', font=('Calibri',18))
    label1.place(relx=0.12, rely=0.2, relwidth=0.8, relheight=0.1)

    global tree
    tree = ttk.Treeview(frame2)
    tree["columns"]=("Name","Course")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Name", width=150, minwidth=150, stretch=tk.NO)
    tree.column("Course", width=250, minwidth=270, stretch=tk.NO)

    tree.heading("Name",text="Name",anchor=tk.W)
    tree.heading("Course", text="Course",anchor=tk.W)

    match = matchTA("sample.csv")

    tree.insert(parent="", index="end", iid=0, text="", values=(match[0][0],match[0][1]))
    tree.insert(parent="", index="end", iid=1, text="", values=(match[1][0],match[1][1]))
    tree.insert(parent="", index="end", iid=2, text="", values=(match[2][0],match[2][1]))
    tree.insert(parent="", index="end", iid=3, text="", values=(match[3][0],match[3][1]))

    global count
    count = 4

    tree.place(relx=0.3, rely=0.2)

    #Labels
    nameLabel = tk.Label(frame2, text='Name', bg='#f3e6ff')
    nameLabel.place(relx=0.12, rely=0.6, relwidth=0.1, relheight=0.05)

    courseLabel = tk.Label(frame2, text='Course', bg='#f3e6ff')
    courseLabel.place(relx=0.5, rely=0.6, relwidth=0.1, relheight=0.05)

    #Entries
    global nameEntry
    global courseEntry
    nameEntry = tk.Entry(frame2)
    nameEntry.place(relx=0.12, rely=0.65, relwidth=0.4, relheight=0.05)

    courseEntry = tk.Entry(frame2)
    courseEntry.place(relx=0.5, rely=0.65, relwidth=0.4, relheight=0.05)

    #Buttons
    addRecordButton = tk.Button(frame2, text='Add Record', command=addRecords)
    addRecordButton.place(relx=0.15, rely=0.725, relwidth=0.2, relheight=0.05)

    removeSelected = tk.Button(frame2, text='Remove Selected Record', command=removeRecords)
    removeSelected.place(relx=0.4, rely=0.725, relwidth=0.35, relheight=0.05)

    selectButton = tk.Button(frame2, text='Select Record to Update', command=selectRecord)
    selectButton.place(relx=0.15, rely=0.8, relwidth=0.35, relheight=0.05)

    updateButton = tk.Button(frame2, text='Save Update', command=updateRecord)
    updateButton.place(relx=0.55, rely=0.8, relwidth=0.2, relheight=0.05)

def addRecords():
    count = 4
    tree.insert(parent="", index="end", iid=count, text="", values=(nameEntry.get(), courseEntry.get()))
    count += 1

    #Clear boxes
    nameEntry.delete(0, tk.END)
    courseEntry.delete(0, tk.END)

def removeRecords():
    selectedRecord = tree.selection()
    for record in selectedRecord:
        tree.delete(record)

def selectRecord():
    #Clear Entry Boxes
    nameEntry.delete(0, tk.END)
    courseEntry.delete(0, tk.END)

    selected = tree.focus()
    values = tree.item(selected, 'values')

    #Output to Entry Boxes
    nameEntry.insert(0, values[0])
    courseEntry.insert(0, values[1])

def updateRecord():
    selected = tree.focus()
    tree.item(selected, text='', values=(nameEntry.get(), courseEntry.get()))


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

    TAallocations = tk.Button(frame, text="View/Edit TA Allocations", command=editAllocations)
    TAallocations.place(relx=0.525, rely=0.5, relwidth=0.25, relheight=0.15)

    ms.mainloop()
