from tkinter import *
import tkinter.messagebox

# Function to enter the task in the Listbox
def entertask():
    # A new window to pop up to take input
    input_text = ""
    
    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please enter some text")
        else:
            listbox_task.insert(END, input_text)
            # Close the root1 window
            root1.destroy()

    root1 = Tk()
    root1.title("Add task")
    
    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()

    button_temp = Button(root1, text="Add task", command=add)
    button_temp.pack()

    root1.mainloop()

# Function to facilitate the deletion of a task from the Listbox
def deletetask():
    # Selects the selected item and then deletes it
    try:
        selected = listbox_task.curselection()
        listbox_task.delete(selected[0])
    except IndexError:
        tkinter.messagebox.showwarning(title="Warning!", message="Please select a task to delete")

# Function to mark a task as completed
def markcompleted():
    try:
        marked = listbox_task.curselection()
        temp = marked[0]
        # Store the text of the selected item in a string
        temp_marked = listbox_task.get(marked)
        # Update it by appending a checkmark
        temp_marked = temp_marked + " ✔"
        # Delete it then insert the updated version
        listbox_task.delete(temp)
        listbox_task.insert(temp, temp_marked)
    except IndexError:
        tkinter.messagebox.showwarning(title="Warning!", message="Please select a task to mark as completed")

# Creating the initial window
window = Tk()
# Giving a title
window.title("To-Do List App")

# Frame widget to hold the listbox and the scrollbar
frame_task = Frame(window)
frame_task.pack()

# To hold items in a listbox
listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="Helvetica")
listbox_task.pack(side=LEFT)

# Scrollbar in case the list exceeds the size of the window
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)

listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Button widgets
entry_button = Button(window, text="Add task", width=50, command=entertask)
entry_button.pack(pady=3)

delete_button = Button(window, text="Delete selected task", width=50, command=deletetask)
delete_button.pack(pady=3)

mark_button = Button(window, text="Mark as completed", width=50, command=markcompleted)
mark_button.pack(pady=3)

window.mainloop()
