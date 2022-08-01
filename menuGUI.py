import sqlite3
from datetime import datetime
from tkinter import *
from numpy import single
from tkinter import ttk
from tkinter import messagebox
from genericpath import exists
from operator import length_hint
import solarSystem
import query

conn = sqlite3.connect('Database.db')
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = conn.cursor()

# Creating master Tkinter window
master = Tk()
master.geometry("200x175")
master.title("Menu")

def searchAll():
    new= Toplevel(master)
    new.geometry("750x400")
    new.title("All Events")
    # Create a Label in New window
    Label(new, text="Event List", font=('Helvetica 17 bold')).pack(pady=30)

    def date_error():
        messagebox.showerror('Python Error', 'Error: Invalid Simulation Length!')
    def selected_item():
        item = tree.selection()
        item_detail = tree.item(item)
        solarSystem.simulation(item_detail.get("values")[1], lengthStr.get())

    # define columns
    columns = ('type', 'date')
    tree = ttk.Treeview(new, columns=columns, show='headings')

    # define headings
    tree.heading('type', text='Event Type')
    tree.heading('date', text='Event Date')

    # add all event dates and type into list
    cursor.execute("""SELECT SOLAR_ECLIPSES.DATE FROM SOLAR_ECLIPSES""")
    solar_result = cursor.fetchall()
    for i in solar_result:
        tree.insert('', 'end', values=('Solar Eclipse', i[0]))

    cursor.execute("""SELECT LUNAR_ECLIPSES.DATE FROM LUNAR_ECLIPSES""")
    lunar_result = cursor.fetchall()
    for i in lunar_result:
        tree.insert('', 'end', values=('Lunar Eclipse', i[0]))

    cursor.execute("""SELECT CONJUNCTION.DATE FROM CONJUNCTION""")
    conjunction_result = cursor.fetchall()
    for i in conjunction_result:
        tree.insert('', 'end', values=('Conjunction', i[0]))
    
    #store length
    lengthStr = StringVar()
    lengthStr_label = ttk.Label(new, text="Simulation Length (in days):")
    lengthStr_entry = ttk.Entry(new, textvariable=lengthStr, width=20)
    lengthStr_entry.focus()

    btn = Button(new, text='Start Simulation', command=selected_item)
    btn.pack(side='bottom')
    tree.pack()
    lengthStr_entry.pack(side='bottom')
    lengthStr_label.pack(side='bottom')

def searchBody():
    new= Toplevel(master)
    new.geometry("1500x400")
    new.title("Bodies")
    # Create a Label in New window
    Label(new, text="Bodies in the Solar System", font=('Helvetica 17 bold')).pack(pady=30)

    # define columns
    columns = ('name', 'mass', 'radius', 'volume', 'orbital', 'rotational', 'distance')
    tree = ttk.Treeview(new, columns=columns, show='headings')

    # define headings
    tree.heading('name', text='Name')
    tree.heading('mass', text='Mass(Kg)')
    tree.heading('radius', text='Radius(Km)')
    tree.heading('volume', text='Volume(Km^3)')
    tree.heading('orbital', text='Orbital Velocity(Km/s)')
    tree.heading('rotational', text='Rotational Velocity(Km/s)')
    tree.heading('distance', text='Distance to Sun(Km)')

    cursor.execute("""SELECT BODIES.NAME, BODIES.MASS, BODIES.RADIUS, BODIES.VOLUME, BODIES.ORBITAL, BODIES.ROTATIONAL, BODIES.DISTANCE FROM BODIES""")
    query_result = cursor.fetchall()
    
    for i in query_result:
        tree.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

    tree.pack()
    
def searchSolar():
    # Create new window
    new= Toplevel(master)
    new.geometry("750x400")
    new.title("Solar Eclipses")
    Label(new, text="Solar Eclipse Dates", font=('Helvetica 17 bold')).pack(pady=30)
    def date_error():
        messagebox.showerror('Python Error', 'Error: Invalid Simulation Length!')
    def selected_item():
        for i in lb.curselection():
            solarSystem.simulation(lb.get(i), lengthStr.get())

    # QUERY FOR ALL SOLAR ECLIPSES
    cursor.execute("""SELECT SOLAR_ECLIPSES.DATE FROM SOLAR_ECLIPSES""")
    query_result = cursor.fetchall()
    sort_list = []
    for i in query_result:
        sort_list.append(i[0])
    sort_list.sort(key = lambda date: datetime.strptime(date, "%Y-%m-%d"))
    
    lb = Listbox(new, width=40, height=15, selectmode=single)
    for j in sort_list:
        x = 0
        lb.insert(x, j)
        x = x + 1
    
    #store length
    lengthStr = StringVar()
    lengthStr_label = ttk.Label(new, text="Simulation Length (in days):")
    lengthStr_entry = ttk.Entry(new, textvariable=lengthStr, width=20)
    lengthStr_entry.focus()

    btn = Button(new, text='Start Simulation', command=selected_item)
    btn.pack(side='bottom')
    lb.pack()
    lengthStr_entry.pack(side='bottom')
    lengthStr_label.pack(side='bottom')

def searchLunar():
    new= Toplevel(master)
    new.geometry("750x400")
    new.title("Lunar Eclipses")
    Label(new, text="Lunar Eclipse Dates", font=('Helvetica 17 bold')).pack(pady=30)

    def date_error():
        messagebox.showerror('Python Error', 'Error: Invalid Simulation Length!')
    def selected_item():
        for i in lb.curselection():
            solarSystem.simulation(lb.get(i), lengthStr.get())

    cursor.execute("""SELECT LUNAR_ECLIPSES.DATE FROM LUNAR_ECLIPSES""")
    query_result = cursor.fetchall()
    sort_list = []
    for i in query_result:
        sort_list.append(i[0])
    sort_list.sort(key = lambda date: datetime.strptime(date, "%Y-%m-%d"))
    
    lb = Listbox(new, width=40, height=15, selectmode=single)
    for j in sort_list:
        x = 0
        lb.insert(x, j)
        x = x + 1
            
    #store length
    lengthStr = StringVar()
    lengthStr_label = ttk.Label(new, text="Simulation Length (in days):")
    lengthStr_entry = ttk.Entry(new, textvariable=lengthStr, width=20)
    lengthStr_entry.focus()

    btn = Button(new, text='Start Simulation', command=selected_item)
    btn.pack(side='bottom')
    lb.pack()
    lengthStr_entry.pack(side='bottom')
    lengthStr_label.pack(side='bottom')

def searchConj():
    new= Toplevel(master)
    new.geometry("750x500")
    new.title("Planetary Conjunctions")
    Label(new, text="Conjunction Dates", font=('Helvetica 17 bold')).pack(pady=30)
    Label(new, text="1 = Mercury, 2 = Venus, 3 = Earth, 4 = Mars, 5 = Jupiter, 6 = Saturn, 7 = Uranus, 8 = Neptune, 9 = Pluto", font=('Helvetica 10 bold')).pack(pady=30)
    # define columns
    columns = ('date', 'p1', 'p2')
    tree = ttk.Treeview(new, columns=columns, show='headings')

    # define headings
    tree.heading('date', text='Date')
    tree.heading('p1', text='Planet 1 ID')
    tree.heading('p2', text='Planet 2 ID')

    def date_error():
        messagebox.showerror('Python Error', 'Error: Invalid Simulation Length!')
    def selected_item():
        item = tree.selection()
        item_detail = tree.item(item)
        solarSystem.simulation(item_detail.get("values")[0], lengthStr.get())

    cursor.execute("""SELECT CONJUNCTION.DATE, CONJUNCTION.FIRST_PLANET, CONJUNCTION.SECOND_PLANET FROM CONJUNCTION ORDER BY DATE DESC""")
    query_result = cursor.fetchall()
    
    for i in query_result:
        tree.insert('', 'end', values=(i[0], i[1], i[2]))
            
            
    #store length
    lengthStr = StringVar()
    lengthStr_label = ttk.Label(new, text="Simulation Length (in days):")
    lengthStr_entry = ttk.Entry(new, textvariable=lengthStr, width=20)
    lengthStr_entry.focus()

    
    btn = Button(new, text='Start Simulation', command=selected_item)
    btn.pack(side='bottom')
    tree.pack()
    lengthStr_entry.pack(side='bottom')
    lengthStr_label.pack(side='bottom')

# Initialize selection
v = StringVar(master, "1")
 
# Create radiobuttons
R0 = Radiobutton(master, text = "All Events", variable = v,
            value = 1, indicator = 0,
            command = searchAll,
            background = "light blue").pack(fill = X, ipady = 5)
R1 = Radiobutton(master, text = "Bodies", variable = v,
            value = 1, indicator = 0,
            command = searchBody,
            background = "light blue").pack(fill = X, ipady = 5)
R2 = Radiobutton(master, text = "Solar Eclipse Dates", variable = v,
            value = 2, indicator = 0,
            command = searchSolar,
            background = "light blue").pack(fill = X, ipady = 5)
R3 = Radiobutton(master, text = "Lunar Eclipse Dates", variable = v,
            value = 3, indicator = 0,
            command = searchLunar,
            background = "light blue").pack(fill = X, ipady = 5)
R4 = Radiobutton(master, text = "Conjunction Dates", variable = v,
            value = 3, indicator = 0,
            command = searchConj,
            background = "light blue").pack(fill = X, ipady = 5)
mainloop()