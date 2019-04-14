from tkinter import *
import backend

def view_command():
    """Calls the view function from backend.py"""
    list_box.delete(0,END)
    for row in backend.view_all():
        list_box.insert(END,row)

def search_command():
    """Calls the search function from backend.py"""
    list_box.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list_box.insert(END,row)

def insert_command():
    """Calls the insert function from backend.py"""
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list_box.delete(0,END)
    list_box.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def get_selected_row(event):
    """Function made to help select an entry from the GUI"""
    global selected_tuple
    try:
        index=list_box.curselection()[0]
        selected_tuple = list_box.get(index)
        #
        entry_title.delete(0,END)
        entry_title.insert(END,selected_tuple[1])
        #
        entry_author.delete(0,END)
        entry_author.insert(END,selected_tuple[2])
        #
        entry_year.delete(0,END)
        entry_year.insert(END,selected_tuple[3])
        #
        entry_isbn.delete(0,END)
        entry_isbn.insert(END,selected_tuple[4])
        #
    except IndexError:
        pass
    return selected_tuple

def delete_command():
    """Calls the delete_entry function from backend.py"""
    backend.delete_entry(selected_tuple[0])

def update_command():
    """Calls the update function from backend.py"""
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

def close_command():
    """Closes the app"""
    quit()

window = Tk(className="Book store")
"""Main window."""
##
label_title=Label(window,text="Title")
label_title.grid(row=0,column=0)

title_text=StringVar()
entry_title=Entry(window,textvariable=title_text)
entry_title.grid(row=0,column=1)
#
label_author=Label(window,text="Author")
label_author.grid(row=0,column=2)

author_text=StringVar()
entry_author=Entry(window,textvariable=author_text)
entry_author.grid(row=0,column=3)
#
label_year=Label(window,text="Year")
label_year.grid(row=1,column=0)

year_text=StringVar()
entry_year=Entry(window,textvariable=year_text)
entry_year.grid(row=1,column=1)
#
label_isbn=Label(window,text="ISBN")
label_isbn.grid(row=1,column=2)

isbn_text=StringVar()
entry_isbn=Entry(window,textvariable=isbn_text)
entry_isbn.grid(row=1,column=3)
##

##
button_view=Button(window,text="View All",width=12,command = view_command)
button_view.grid(row=2,column=3)
#
button_search=Button(window,text="Search Entry",width=12,command = search_command) #button size_char = 12
button_search.grid(row=3,column=3)
#
button_add=Button(window,text="Add Entry",width=12,command = insert_command)
button_add.grid(row=4,column=3)
#
button_update=Button(window,text="Update",width=12,command = update_command)
button_update.grid(row=5,column=3)
#
button_del=Button(window,text="Delete",width=12,command = delete_command)
button_del.grid(row=6,column=3)
#
button_close=Button(window,text="Close",width=12,command = close_command)
button_close.grid(row=7,column=3)

##
list_box=Listbox(window,width=35,height=6)
list_box.grid(row=2,column=0,rowspan=6,columnspan = 2)


sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list_box.configure(yscrollcommand=sb1.set)#connecting the list and the scrollbar
sb1.configure(command=list_box.yview)

list_box.bind('<<ListboxSelect>>',get_selected_row)

##
window.mainloop()
