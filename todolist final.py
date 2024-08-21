import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageDraw, ImageTk
import random
from datetime import datetime

# Function to create a gradient image
def create_gradient(width, height, start_color, end_color):
    base = Image.new('RGB', (width, height), start_color)
    top = Image.new('RGB', (width, height), end_color)
    mask = Image.new('L', (width, height))
    mask_data = []

    for y in range(height):
        for x in range(width):
            mask_data.append(int(255 * (y / height)))

    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

# Function to update the gradient background
def update_gradient():
    global gradient_index
    gradient_image = create_gradient(screen_width, screen_height, gradient_colors[gradient_index], gradient_colors[(gradient_index + 1) % len(gradient_colors)])
    gradient_image_tk = ImageTk.PhotoImage(gradient_image)
    canvas.create_image(0, 0, anchor='nw', image=gradient_image_tk)
    canvas.image = gradient_image_tk
    gradient_index = (gradient_index + 1) % len(gradient_colors)
    root.after(100, update_gradient)  # Update every 100 ms

# Function to animate gradient colors on a button
def update_button_gradient(button, colors):
    global button_gradient_index
    button.config(bg=colors[button_gradient_index])
    button_gradient_index = (button_gradient_index + 1) % len(colors)
    root.after(200, update_button_gradient, button, colors)

# Function to add a new task to the list
def add_task():
    task = entry.get()
    date = calendar.get_date()
    if task:
        frame = tk.Frame(task_frame, bg='#f2f2f2')
        var = tk.StringVar(value=f"{task} (Due: {date})")
        checkbox = tk.Checkbutton(frame, text=var.get(), variable=var, font=('Helvetica', 12, 'bold'), bg='#f2f2f2')
        checkbox.pack(side=tk.LEFT)
        complete_button = tk.Button(frame, text="Complete", command=lambda: mark_complete(frame, checkbox, complete_button, date), bg='#66ff66', font=('Helvetica', 12, 'bold'))
        complete_button.pack(side=tk.RIGHT, padx=5)
        delete_button = tk.Button(frame, text="Delete", command=lambda: delete_task(frame), bg='#ff6666', font=('Helvetica', 12, 'bold'))
        delete_button.pack(side=tk.RIGHT, padx=5)
        frame.pack(anchor='w', pady=2)
        tasks.append((frame, var, checkbox, complete_button, date))
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")
    update_buttons()

# Function to delete a task from the list
def delete_task(frame):
    frame.pack_forget()
    tasks.remove(next(task for task in tasks if task[0] == frame))
    update_buttons()

# Function to mark a task as complete
def mark_complete(frame, checkbox, button, due_date):
    checkbox.config(state=tk.DISABLED)
    checkbox.config(fg='gray')
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Button) and widget.cget('text') == 'Complete':
            widget.config(state=tk.DISABLED)
    button.config(bg='#d9d9d9')
    congrats_message = tk.Label(root, text="Task Completed! ❤️ Congratulations! 🎉", font=('Helvetica', 18, 'bold'), fg='#ff6600', bg='#99ff99', bd=5, relief="solid")
    congrats_message.place(relx=0.5, rely=0.5, anchor='center')
    root.after(3000, congrats_message.destroy)
    update_buttons()

# Function to show the status of selected tasks
def show_status():
    selected_tasks = [var.get() for frame, var, checkbox, complete_button, due_date in tasks if var.get() == checkbox.cget("text")]
    if selected_tasks:
        messagebox.showinfo("Task Status", f"Selected Tasks: {', '.join(selected_tasks)}\nStatus: Incomplete")
    else:
        motivational_quotes = [
            "Keep going, you're doing great! ❤️",
            "Don't give up! You've got this! 💪",
            "Stay positive, work hard, make it happen! 🌟",
            "Believe in yourself! You can do it! 🌈",
            "Small steps every day! 🚶‍♂️"
        ]
        messagebox.showinfo("Motivation", random.choice(motivational_quotes))

# Function to update button styles based on selection
def update_buttons():
    for frame, var, checkbox, complete_button, due_date in tasks:
        current_date = datetime.now().date()
        if datetime.strptime(due_date, '%Y-%m-%d').date() < current_date:
            complete_button.config(text="Overdue", bg='#ff6666')
            checkbox.config(fg='red', font=('Helvetica', 12, 'bold'))
            checkbox.config(text=f"{var.get()} (Overdue)")
        else:
            complete_button.config(text="Complete", bg='#66ff66')

# Setting up the main window
root = tk.Tk()
root.title("Panda Theme To-Do List with Gradient Background")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")

# Create a canvas for the gradient background
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack(fill="both", expand=True)

# Define gradient colors
gradient_colors = ["#ffcccc", "#ccffcc", "#ccccff", "#ffffcc", "#ccffff", "#ffccff"]
gradient_index = 0

# Define button gradient colors
button_gradient_colors = ["#ffcc00", "#ff9966", "#ff66cc", "#cc66ff", "#66ccff", "#66ff66"]
button_gradient_index = 0

# Initialize the gradient background
update_gradient()

# Create a frame for the to-do list
frame = tk.Frame(root, bg='#f2f2f2', bd=5)
frame.place(relwidth=0.6, relheight=0.6, relx=0.2, rely=0.2)

# Title of the To-Do List
title_label = tk.Label(frame, text="TO-DO LIST", bg='#f2f2f2', font=('Helvetica', 20, 'bold'))
title_label.pack(pady=10)

# Entry box to input tasks
entry_frame = tk.Frame(frame, bg='#f2f2f2')
entry_frame.pack(pady=10)

entry_label = tk.Label(entry_frame, text="ADD TASK:", bg='#f2f2f2', font=('Helvetica', 14, 'bold'))
entry_label.pack(side=tk.LEFT, padx=5)

entry = tk.Entry(entry_frame, width=30, font=('Helvetica', 14, 'bold'))
entry.pack(side=tk.LEFT, padx=5)

calendar_frame = tk.Frame(entry_frame, bg='#f2f2f2')
calendar_frame.pack(side=tk.LEFT, padx=5)

# Drop-down calendar for selecting due date
calendar = DateEntry(calendar_frame, selectmode='day', date_pattern='y-mm-dd', background='#ffcccc', foreground='#000000', headersbackground='#ff6666', normalbackground='#ff9999', weekendbackground='#ffcccc')
calendar.pack()

add_button = tk.Button(entry_frame, text="Add", command=add_task, font=('Helvetica', 14, 'bold'))
add_button.pack(side=tk.LEFT, padx=5)

# Start the button gradient animation
update_button_gradient(add_button, button_gradient_colors)

# Frame to hold task checkboxes
task_frame = tk.Frame(frame, bg='#f2f2f2')
task_frame.pack(pady=10)

# List to hold tasks and their variables
tasks = []

# Taskbar for additional actions
taskbar_frame = tk.Frame(frame, bg='#f2f2f2')
taskbar_frame.pack(pady=10)

delete_all_button = tk.Button(taskbar_frame, text="Delete All Selected", command=lambda: [delete_task(task[0]) for task in tasks], bg='#d9d9d9', font=('Helvetica', 14, 'bold'))
delete_all_button.pack(side=tk.LEFT, padx=5)

status_button = tk.Button(taskbar_frame, text="Show Status", command=show_status, bg='#d9d9d9', font=('Helvetica', 14, 'bold'))
status_button.pack(side=tk.LEFT, padx=5)

# Update buttons style based on selection
root.after(100, update_buttons)

# Run the application
root.mainloop()
