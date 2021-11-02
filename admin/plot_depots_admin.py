# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 15:00:01 2021

@author: SRI$
"""

#!/usr/bin/env python
# coding: utf-8

import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import * 
import pandas as pd
import numpy as np
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

start_date = ''
end_date = ''

# this is a function to get the user input from the text input box
def getStart():
	userInput = start_date.get()
	return userInput


# this is a function to get the user input from the text input box
def getEnd():
	userInput = end_date.get()
	return userInput


# this is the function called when the button is clicked
def btnQuery():
    con = sqlite3.connect('C:/Users/SRI$/Desktop/Glassgow/4084_lb1_team5_project/db.sqlite3')
    #this is the connection to the local DB sqlite file. Change it as needed
    

# this is the function called when the button is clicked

    
class Adminpage(tk.Tk):
#main app page
    def __init__(self, *args, **kwargs):       
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        for F in (StartPage, GraphPage_1wk):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")
        
        self.geometry('1200x950')
        self.configure(background='#F0F8FF')
        self.title('Glasgow Bike Sharing Service')

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    #added for the controller function
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
    
        #root = Tk()
        from_date = StringVar()
        to_date_var = StringVar()

        # This is the section of code which creates the main window
        

        # This is the section of code which creates a text input box
        start_date=Entry(self)
        start_date.place(x=33, y=45)


        # This is the section of code which creates the a label
        Label(self, text='From date (yyyy-mm-dd)', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=26, y=17)


        # This is the section of code which creates a text input box
        end_date=Entry(self)
        end_date.place(x=240, y=45)


        # This is the section of code which creates the a label
        Label(self, text='To date (yyyy-mm-dd)', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=240, y=17)


        # This is the section of code which creates a button
        Button(self, text='Query', bg='#EEE8CD', font=('arial', 12, 'normal'), command=btnQuery).place(x=440, y=35)


        # This is the section of code which creates a button
        Button(self, text='1week auto', bg='#EEE8CD', font=('arial', 12, 'normal'), command=lambda: controller.show_frame(GraphPage_1wk)).place(x=150, y=95)

class GraphPage_1wk(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Summary of Last week", font='Verdana')
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Main Page",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        self.place(x=0, y=116, anchor="nw", width=800, height=550)
        
        with sqlite3.connect('C:/Users/SRI$/Desktop/Glassgow/4084_lb1_team5_project/db.sqlite3') as db:cursor=db.cursor()
        query = "SELECT start_date_time,start_depot, COUNT(session_id)  FROM bikecustomer_hiresession WHERE DATE(start_date_time) >= DATE('now', 'weekday 0', '-7 days')  GROUP BY start_date_time, start_depot  ORDER BY start_date_time"
        #this is the connection to the local DB sqlite file. Change it as needed
        queryResult = cursor.execute(query)
        df = pd.DataFrame(queryResult)
        #print(df)
        tab = pd.crosstab(df[0],df[1], values=df[2],aggfunc='sum')
        tab = tab.fillna(0)
        print(tab)
        #tab.plot(kind='bar', stacked=True)
        
        f = Figure(figsize=(8,8), dpi=100)
        ax1 = f.add_subplot(111)
        canvas = FigureCanvasTkAgg(f, self)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        tab.plot(kind='bar', legend=True, stacked=True, ax = ax1)
        ax1.set_xlabel("date")
        ax1.set_ylabel("bike uses")
        ax1.legend(title="depot ID",  loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
        #a.plot()
        #canvas.draw()
        #toolbar = NavigationToolbar2Tk(f, self)
        #toolbar.update()
        #canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
class GraphPage_custom(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Summary of Last week", font='Verdana')
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Main Page",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        self.place(x=0, y=116, anchor="nw", width=800, height=550)
        
        with sqlite3.connect('C:/Users/SRI$/Desktop/Glassgow/4084_lb1_team5_project/db.sqlite3') as db:cursor=db.cursor()
        query = "SELECT start_date_time,start_depot, COUNT(session_id)  FROM bikecustomer_hiresession WHERE DATE(start_date_time) >= DATE('now', 'weekday 0', '-7 days')  GROUP BY start_date_time, start_depot  ORDER BY start_date_time"
        #this is the connection to the local DB sqlite file. Change it as needed
        queryResult = cursor.execute(query)
        df = pd.DataFrame(queryResult)
        #print(df)
        tab = pd.crosstab(df[0],df[1], values=df[2],aggfunc='sum')
        tab = tab.fillna(0)
        print(tab)
        #tab.plot(kind='bar', stacked=True)
        
        f = Figure(figsize=(8,8), dpi=100)
        ax1 = f.add_subplot(111)
        canvas = FigureCanvasTkAgg(f, self)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        tab.plot(kind='bar', legend=True, stacked=True, ax = ax1)
        ax1.set_xlabel("date")
        ax1.set_ylabel("bike uses")
        ax1.legend(title="depot ID",  loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)

app = Adminpage()
app.mainloop()




#code to display depots. Did it in CSV, but call from DB usign pymysql or other 
import pymysql.cursors
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='dkzkrl123!',
                             database='bikeproj',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)




with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "SELECT * FROM bikecustomer_hiresession"
        cursor.execute(sql)
result = cursor.fetchall()
df = (pd.DataFrame(result))




df.head(5)




df2 = df
df2['start_datetime'] = pd.to_datetime(df['start_datetime']).dt.date
df2.head(5)




tab = pd.crosstab(df2.start_datetime, df2.start_depot,margins=True, margins_name="Total")
tab.head(10)




df3=tab[:-1]
df3.head(10)




df3.plot(kind='bar', stacked=True)




#filtering date 
#df2.loc()

