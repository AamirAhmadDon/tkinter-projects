import tkinter as tk
from tkinter import messagebox, simpledialog
import os

TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASK_FILE, "w") as file:
        file.write("\n".join(tasks))

def add_task():
    """Add a new task to the list."""
    task = task_entry.get()
    if task.strip():
        tasks.append(task)
        save_tasks(tasks)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    """Delete the selected task."""
    try:
        task_index = task_listbox.curselection()[0]
        task = task_listbox.get(task_index)
        task_listbox.delete(task_index)
        tasks.remove(task)
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def edit_task():
    """Edit the selected task."""
    try:
        task_index = task_listbox.curselection()[0]
        task = task_listbox.get(task_index)
        new_task = simpledialog.askstring("Edit Task", "Edit Task", initialvalue=task)
        if new_task:
            tasks[task_index] = new_task
            task_listbox.delete(task_index)
            task_listbox.insert(task_index, new_task)
            save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")

def mark_task_complete():
    """Mark the selected task as complete."""
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks[selected_task_index] = f"[✔] {tasks[selected_task_index].replace('[✔] ', '')}"
        update_task_list()
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as complete!")

def update_task_list():
    """Refresh the task list in the Listbox."""
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Initialize the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.config(bg="gray14")
root.maxsize(800, 600)
root.minsize(400, 300)
root.resizable(True, True)

# Load tasks
tasks = load_tasks()

# Creating main window label
interface_label = tk.Label(root, text="To-Do List App", font=("Arial", 24), bg="gray14", fg="white")
interface_label.pack(pady=10)

# Making the widgets
task_entry = tk.Entry(root, font=("Arial", 16), bg="gray14", fg="white")
task_entry.pack(pady=20)

# Making the buttons
add_button = tk.Button(root, text="Add Task", font=("Arial", 16), bg="DodgerBlue2", fg="white", command=add_task)
add_button.pack(pady=10)

task_listbox = tk.Listbox(root, font=("Arial", 16), bg="gray14", fg="white", selectbackground="firebrick1", selectforeground="white")
task_listbox.pack(pady=20, fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

edit_button = tk.Button(button_frame, text="Edit Task", font=("Arial", 16), bg="DodgerBlue2", fg="white", command=edit_task)
edit_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", font=("Arial", 16), bg="deeppink2", fg="white", command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

complete_button = tk.Button(button_frame, text="Mark Complete", command=mark_task_complete, width=12)
complete_button.grid(row=0, column=2, padx=5)

# Populate the task list on startup
update_task_list()

# Start the application
root.mainloop()