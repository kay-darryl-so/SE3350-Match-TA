import tkinter as tk
from tkinter import filedialog, Text
from tkinter import*

#def rankApplicants():

#def viewTAAllocations():


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

    RankApplicants = tk.Button(frame, text="Rank Applicants")
    RankApplicants.place(relx=0.225, rely=0.5, relwidth=0.25, relheight=0.15)

    TAallocations = tk.Button(frame, text="View TA Allocations")
    TAallocations.place(relx=0.525, rely=0.5, relwidth=0.25, relheight=0.15)

    ms.mainloop()
