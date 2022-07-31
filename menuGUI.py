import sqlite3
from datetime import datetime
from tkinter import *
from numpy import single
from tkinter import ttk

conn = sqlite3.connect('Database.db')
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = conn.cursor()

# Creating master Tkinter window
master = Tk()
master.geometry("200x175")

def search():
    new= Toplevel(master)
    new.geometry("750x400")
    new.title("New Window")
    # Create a Label in New window
    Label(new, text="Search in database", font=('Helvetica 17 bold')).pack(pady=30)
def searchSolar():
    # Create new window
    new= Toplevel(master)
    new.geometry("750x400")
    new.title("New Window")
    Label(new, text="Solar Eclipse Dates", font=('Helvetica 17 bold')).pack(pady=30)

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

    def selected_item():
        for i in lb.curselection():
            print(lb.get(i))

    btn = Button(new, text='Start Simulation', command=selected_item)
    btn.pack(side='bottom')
    lb.pack()

def searchLunar():
    new= Toplevel(master)
    new.geometry("750x400")
    new.title("New Window")
    Label(new, text="Lunar Eclipse Dates", font=('Helvetica 17 bold')).pack(pady=30)
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

    def selected_item():
        for i in lb.curselection():
            print(lb.get(i))
            
    btn = Button(new, text='Start Simulation', command=selected_item)
    btn.pack(side='bottom')
    lb.pack()
def searchConj():
    new= Toplevel(master)
    new.geometry("750x400")
    new.title("New Window")
    # Create a Label in New window
    Label(new, text="Conjunction Dates", font=('Helvetica 17 bold')).pack(pady=30)
    Label(new, text="1 = Mercury, 2 = Venus, 3 = Earth, 4 = Mars, 5 = Jupiter, 6 = Saturn, 7 = Uranus, 8 = Neptune, 9 = Pluto", font=('Helvetica 10 bold')).pack(pady=30)
    # define columns
    columns = ('date', 'p1', 'p2')
    tree = ttk.Treeview(new, columns=columns, show='headings')

    # define headings
    tree.heading('date', text='Date')
    tree.heading('p1', text='Planet 1 ID')
    tree.heading('p2', text='Planet 2 ID')

    cursor.execute("""SELECT CONJUNCTION.DATE, CONJUNCTION.FIRST_PLANET, CONJUNCTION.SECOND_PLANET FROM CONJUNCTION ORDER BY DATE DESC""")
    query_result = cursor.fetchall()
    
    for i in query_result:
        tree.insert('', 'end', values=(i[0], i[1], i[2]))
            
    def selected_item():
        item = tree.selection()[0]
        item_detail = tree.item(item)
        print (item_detail.get("values")[0])
            
    btn = Button(new, text='Start Simulation', command=selected_item)
    btn.pack(side='bottom')
    tree.pack()

# Initializee selection
v = StringVar(master, "1")
 
# Create radiobuttons
R1 = Radiobutton(master, text = "Search All", variable = v,
            value = 1, indicator = 0,
            command = search,
            background = "light blue").pack(fill = X, ipady = 5)
R2 = Radiobutton(master, text = "Solar Eclipses", variable = v,
            value = 2, indicator = 0,
            command = searchSolar,
            background = "light blue").pack(fill = X, ipady = 5)
R3 = Radiobutton(master, text = "Lunar Eclipses", variable = v,
            value = 3, indicator = 0,
            command = searchLunar,
            background = "light blue").pack(fill = X, ipady = 5)
R4 = Radiobutton(master, text = "Conjunctions", variable = v,
            value = 3, indicator = 0,
            command = searchConj,
            background = "light blue").pack(fill = X, ipady = 5)
mainloop()