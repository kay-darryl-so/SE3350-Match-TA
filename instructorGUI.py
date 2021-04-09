import tkinter as tk
from tkinter import filedialog, Text
from tkinter import*
from rank_applicants import *

#def rankApplicants():

def viewTAAllocations():
    global frame
    frame = tk.Frame(ms, bg='#f3e6ff')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    label1 = tk.Label(frame, text= 'Match Results', bg='#f3e6ff', font=('Calibri',18))
    label1.place(relx=0.12, rely=0.2, relwidth=0.8, relheight=0.1)

    fn = "sample.csv"
    match = matchTA(fn)

    tree = ttk.Treeview(frame)
    tree["columns"]=("Name","Course")
    tree.column("#0", width=0)
    tree.column("Name", width=150, minwidth=150, stretch=tk.NO)
    tree.column("Course", width=250, minwidth=270, stretch=tk.NO)

    tree.heading("Name",text="Name",anchor=tk.W)
    tree.heading("Course", text="Course",anchor=tk.W)

    tree.insert(parent="", index="end", iid=0, text="", values=(match[0][0],match[0][1]))
    tree.insert(parent="", index="end", iid=1, text="", values=(match[1][0],match[1][1]))
    tree.insert(parent="", index="end", iid=2, text="", values=(match[2][0],match[2][1]))
    tree.insert(parent="", index="end", iid=3, text="", values=(match[3][0],match[3][1]))

    tree.place(relx=0.3, rely=0.35)

    accept = tk.Button(frame, text='Accept', width=10, height=1, command=acceptResponse)
    accept.place(relx=0.32, rely=0.7, relwidth=0.15, relheight=0.1)

    reject = tk.Button(frame, text='Reject', width=10, height=1, command=rejectResponse)
    reject.place(relx=0.52, rely=0.7, relwidth=0.15, relheight=0.1)


def acceptResponse():
    success = tk.Label(frame, text="Your response has been saved", fg='#008000')
    success.place(relx=0.3, rely=0.8, relwidth=0.5, relheight=0.1)
    newFile = "instructorResponse.txt"
    with open(newFile, 'w') as f:
        f.write("Instructor Accepts Matches")
        f.close()

def rejectResponse():
    global screen1
    screen1 = Toplevel(ms)
    screen1.title("Instructor Response")
    screen1.geometry("600x400")

    response = StringVar()
    global textEntry

    label = tk.Label(screen1, text = "Please enter your reason for rejecting the match:")
    label.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.2)
    textEntry = tk.Entry(screen1, textvariable=response)
    textEntry.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.3)
    saveButton = tk.Button(screen1, text='Save Response', width=10, height=1, command=responseSavedMessage)
    saveButton.place(relx=0.4, rely=0.65, relwidth=0.2, relheight=0.1)

    newFile = "instructorResponse.txt"
    with open(newFile, 'w') as f:
        f.write("Instructor Rejects Matches\n")
        f.write("Reason: \n")
        f.write(repr(textEntry))
        f.close()

def responseSavedMessage():
    success = tk.Label(screen1, text="Your response has been saved", fg='#008000')
    success.place(relx=0.25, rely=0.75, relwidth=0.5, relheight=0.1)

    newFile = "instructorResponse.txt"
    with open(newFile, 'w') as f:
        f.write("Instructor Rejects Matches\n")
        f.write("Reason: \n")
        f.write(textEntry.get())
        f.close()

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

    RankApplicants = tk.Button(frame, text="Rank Applicants", command=view_applicant_interface)
    RankApplicants.place(relx=0.225, rely=0.5, relwidth=0.25, relheight=0.15)

    TAallocations = tk.Button(frame, text="View TA Allocations", command=viewTAAllocations)
    TAallocations.place(relx=0.525, rely=0.5, relwidth=0.25, relheight=0.15)

    ms.mainloop()
