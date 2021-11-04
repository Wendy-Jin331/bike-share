import tkinter as tk
from tkinter import ttk
from tkinter import * 
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import re

#GUI Designed with python gui-builder (http://www.python-gui-builder.com/)

root = tk.Tk()

#Function that checks the 
def check_format(input):
    return (re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}',input))

# this is the function called when the button is clicked
def query():
    start = getStart()
    end = getEnd()
   # print(start)
   # print(end)
    
        
    with sqlite3.connect('test_db.sqlite3') as db:cursor=db.cursor()
    query = "SELECT start_date_time,start_depot, COUNT(session_id) FROM bikecustomer_session WHERE start_date_time BETWEEN datetime ("+ start +") AND datetime("+ end +") GROUP BY start_date_time, start_depot"
    #this is the connection to the local DB sqlite file. Change it as needed
    #print(query)
    queryResult = cursor.execute(query)
    df = pd.DataFrame(queryResult)
        #print(df)
    tab = pd.crosstab(df[0],df[1], values=df[2],aggfunc='sum')
    tab = tab.fillna(0)
    #print(tab)
        #tab.plot(kind='bar', stacked=True)
        
    root2 = tk.Toplevel()
    f = plt.Figure(figsize=(8,8), dpi=100)
    ax1 = f.add_subplot(111)
    canvas = FigureCanvasTkAgg(f, root2)
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    tab.plot(kind='bar', legend=True, stacked=True, ax = ax1)
    ax1.set_xlabel("date")
    ax1.set_ylabel("bike uses")
    ax1.legend(title="depot ID",  loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
    


# this is a function to get the user input from the text input box
def getStart():
    
    userInput = startdate.get()
    if(check_format(userInput)):
        return '\''+userInput+'\''
    else:
        top = tk.Tk()
        top.geometry("300x150")
        messagebox.showwarning("Please input format as yyyy-mm-dd")
        top.mainloop()
        
# this is a function to get the user input from the text input box
def getEnd():
    
    userInput = enddate.get()
    if(check_format(userInput)):
        return '\''+userInput+'\''
    else:
        top = tk.Tk()
        top.geometry("300x150")
        messagebox.showwarning("Please input format as yyyy-mm-dd")
        top.mainloop()

# This is the section of code which creates the main window
root.geometry('540x200')
root.configure(background='#F0F8FF')
root.title('Glasgow Bike Sharing Service')


# This is the section of code which creates a button
Button(root, text='Make query', bg='#F0F8FF', font=('arial', 15, 'normal'), command=query).place(x=210, y=115)


# This is the section of code which creates a text input box
startdate=Entry(root)
startdate.place(x=69, y=65)


# This is the section of code which creates a text input box
enddate=Entry(root)
enddate.place(x=269, y=65)


# This is the section of code which creates the a label
Label(root, text='Enter date in YYYY-MM-DD format that you wish to access', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=69, y=35)


# This is the section of code which creates the a label
Label(root, text='From', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=19, y=65)


# This is the section of code which creates the a label
Label(root, text='To', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=239, y=65)


root.mainloop()
