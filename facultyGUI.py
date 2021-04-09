import tkinter as tk
from tkinter import filedialog, ttk
from readApplication import readApplicationFile
from readApplication import getFile


def uploadApplication():

    frame = tk.Frame(ms, bg='#f3e6ff')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    heading = tk.Label(frame, text= 'Application', bg='#f3e6ff', font=('Calibri',18))
    heading.place(relx=0.12, rely=0.2, relwidth=0.8, relheight=0.1)

    fn = filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=(('.csv', "*.csv"),('all files', '*.*')))
    app = readApplicationFile(fn)

    newFile = "2020-2021 Applications.csv"
    with open(newFile, 'w') as f:
        f.write('Course Code,Applicant Name,applicant email,"Applicant status ( 1- Fundable, 2-NotFundable,3-External)",5or10 hrs,Course Rank,Q1,A1,Q2,A2,Q3,A3,…,Qn,An,Instructor Preference\n')
        content = getFile(fn)
        for i in content:
            f.write(str(i))
            f.write('\n')
        f.close()

    tree = ttk.Treeview(frame)
    tree["columns"]=("Name","Email","Courses","Funding","Hours")
    tree.column("#0", width=0)
    tree.column("Name", width=150, minwidth=150, stretch=tk.NO)
    tree.column("Email", width=150, minwidth=150, stretch=tk.NO)
    tree.column("Courses", width=250, minwidth=270, stretch=tk.NO)
    tree.column("Funding", width=80, minwidth=50, stretch=tk.NO)
    tree.column("Hours", width=120, minwidth=100, stretch=tk.NO)

    tree.heading("Name",text="Name",anchor=tk.W)
    tree.heading("Email", text="Email",anchor=tk.W)
    tree.heading("Courses", text="Courses and Rankings",anchor=tk.W)
    tree.heading("Funding", text="Fundability",anchor=tk.W)
    tree.heading("Hours", text="Number of Hours", anchor=tk.W)

    tree.insert(parent="", index="end", iid=0, text="", values=(app[0][0],app[0][1],app[0][2],app[0][3],app[0][4]))
    tree.insert(parent="", index="end", iid=1, text="", values=(app[1][0],app[1][1],app[1][2],app[1][3],app[1][4]))
    tree.insert(parent="", index="end", iid=2, text="", values=(app[2][0],app[2][1],app[2][2],app[2][3],app[2][4]))
    tree.insert(parent="", index="end", iid=3, text="", values=(app[3][0],app[3][1],app[3][2],app[3][3],app[3][4]))

    tree.place(relx=0.1, rely=0.35)


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

    TAhours = tk.Button(frame, text="Upload Application (.csv)", command=uploadApplication)
    TAhours.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.15)

    ms.mainloop()
