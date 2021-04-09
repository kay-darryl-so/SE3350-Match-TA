import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import numpy as np
import re

def file_open():
    filename=filedialog.askopenfilename(
        initialdir="./",
        title="Open A File",
        filetype=(("xlsx files", "*.xlsx"),("All Files", "*,*"))
    )
    if filename:
        try:
            filename = r"{}".format(filename)
            df = pd.read_excel(filename)
        except ValueError:
            print('Wrong file')
        except FileNotFoundError:
            print('Wrong file')
    
    #Clear old tree view
    clear_tree()
    return df

#clear data in tree view
def clear_tree():
    data_tree.delete(*data_tree.get_children())

def clear_ranking_frame():
    for widget in rank_frame.winfo_children():
        widget.destroy()

def display_tree(dataframe):
    #Set up new tree view or applicant information
    data_tree['column']=list(dataframe.columns)
    data_tree['show']='headings'
    #headers
    for column in data_tree['column']:
        data_tree.heading(column, text=column)

    #put data in tree view
    dataframe_rows = dataframe.to_numpy().tolist()
    for row in dataframe_rows:
        data_tree.insert("", "end", values=row)
    data_tree.pack()

def update_results():
    results_list=[None]*len(name_list)
    complete=True
    for x in range(len(name_list)):
        for y in range(x+1, len(name_list)):
            if combobox_list[x].get()==combobox_list[y].get():
                complete=False
    
    if not complete:
        messagebox.showerror('Error', 'Ranking of applicants is incomplete or duplicate of same rank selected')

    else:
        row_index_list = [None]*len(name_list)
        course_filter = course_choice.get().split()[0]
        if "Instructor Rank" not in df_applicant:
            df_applicant.insert(6, "Instructor Rank", None)
        for x in range(len(name_list)):
            df_applicant["Instructor Rank"] = np.where((df_applicant['Applicant Name']==name_list[x])&(df_applicant['Course Code']==course_filter), combobox_list[x].get(), df_applicant["Instructor Rank"])
        df_applicant.to_csv('./InstructorRanking.csv', index=False)
        messagebox.showinfo('Update Success', f'Ranking of Applicants for course {course_choice.get()} is successfully saved')
        



def rank_applicant(dataframe):
    student_data = dataframe.to_numpy().tolist()
    clear_ranking_frame()

    global name_list
    global combobox_list
    name_list= [None] * len(student_data)
    combobox_list= [None] * len(student_data)
    count=0
    for student in student_data:
        name_list[count] = student[1]
        tk.Label(rank_frame, text=student[1], bg='#f3e6ff', font='bold').grid(column=0, row=count)
        temp_list=np.arange(start=1, stop=len(student_data)+1).tolist()
        combobox_list[count] = ttk.Combobox(rank_frame, value=temp_list, state='readonly')
        combobox_list[count].grid(column=1, row=count)
        count+=1
    
    results_btn.pack(padx=10,pady=10, ipadx=30, ipady=15, side='bottom')


def update_applicant(event):
    clear_tree()
    course_filter = course_choice.get().split()[0]
    try:
        df_temp=df_applicant[df_applicant['Course Code']==course_filter]
    except NameError:
        return
    else:
        display_tree(df_temp)
        rank_applicant(df_temp)

def select_applicant_file():
    global df_applicant
    df_applicant = file_open()
    clear_tree()
    course_filter = course_choice.get().split()[0]
    df_temp=df_applicant[df_applicant['Course Code']==course_filter]
    display_tree(df_temp)
    rank_applicant(df_temp)

def select_course():
    df_course = file_open()
    course_list =[]
    df_rows = df_course.to_numpy().tolist()
    for row in df_rows:
        course_name=''
        for x in range(len(row)):
            if x==0:
                course_name += row[x]
            elif x==1:
                course_name += ' '+row[x]
        course_list.append(course_name)
    
    course_choice.configure(value=course_list)
    course_choice.current(0)
    course_choice.bind("<<ComboboxSelected>>", update_applicant)
    course_choice.pack(padx=10,pady=10, ipadx=10, ipady=5)
    choose_applicant_btn.pack(padx=10,pady=10, ipadx=30, ipady=15)    

def view_applicant_interface():
    view_app = tk.Tk()
    view_app.title('TA-Course Matching System')
    view_app.geometry('1000x900')

    view_canvas = tk.Canvas(view_app, bg="#ffffff")
    view_canvas.pack(fill='both', expand='yes')

    view_frame = tk.Frame(view_canvas, bg='#f3e6ff')
    view_frame.pack(fill='both', expand='yes', padx = 80, pady=80)

    global choose_course_frame
    choose_course_frame = tk.Frame(view_frame, bg='#f3e6ff')
    choose_course_frame.pack(side='top', padx=10,pady=10)

    choose_course_btn= tk.Button(choose_course_frame,text="Choose Course File", command=select_course)
    choose_course_btn.pack(padx=10,pady=10, ipadx=30, ipady=15)
    
    global course_choice
    course_choice = ttk.Combobox(choose_course_frame, state='readonly')

    applicant_display = tk.Frame(view_frame, bg='#f3e6ff')
    applicant_display.pack(side='top', padx=10,pady=10)

    global choose_applicant_btn
    choose_applicant_btn = tk.Button(applicant_display, text="Choose Applicant File", command=select_applicant_file)

    global data_tree
    data_tree = ttk.Treeview(applicant_display)

    x_scrollbar = tk.Scrollbar(view_frame, orient='horizontal', command=data_tree.xview)
    x_scrollbar.pack(side='bottom', fill='x')
    data_tree.configure(xscrollcommand=x_scrollbar.set)

    global rank_frame
    rank_frame=tk.Frame(view_frame, bg='#f3e6ff')
    rank_frame.pack(side='top', padx=10, pady=10)

    global results_btn
    results_btn=tk.Button(view_frame, text="Update Ranking", command=update_results)

    view_app.mainloop()

view_applicant_interface()
# output_df = pd.DataFrame(columns=['Name', 'Course', 'Instructor Ranking'])
# output_df.loc[0] = ['one','two','three']
# output_df.loc[1] = ['two','two','two']
# if ((output_df['Name'] == 'three') & (output_df['Course']=='two')).any():
#     print('True')
# else:
#     print('False')
# print(output_df)