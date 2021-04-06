# GUI for Department

import tkinter as tk
from tkinter import filedialog, ttk
from matchTA import matchTA


def matchTAtoCourse():

    frame = tk.Frame(ms, bg='#f3e6ff')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    label1 = tk.Label(frame, text= 'Match Results', bg='#f3e6ff', font=('Calibri',18))
    label1.place(relx=0.12, rely=0.2, relwidth=0.8, relheight=0.1)

    fn = filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=(('.csv', "*.csv"),('all files', '*.*')))
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

    TAhours = tk.Button(frame, text="Match TAs to Courses", command=matchTAtoCourse)
    TAhours.place(relx=0.225, rely=0.5, relwidth=0.25, relheight=0.15)

    TAallocations = tk.Button(frame, text="View/Edit TA Allocations")
    TAallocations.place(relx=0.525, rely=0.5, relwidth=0.25, relheight=0.15)

    ms.mainloop()