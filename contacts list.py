import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageDraw, ImageTk
import sqlite3
import re

# Create a database connection
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    address TEXT
)
''')
conn.commit()

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
    root.after(1000, update_gradient)  # Update every second

# Function to validate phone number
def validate_phone(phone):
    if not re.match(r'^\d{10}$', phone):
        return False
    return True

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone Number are required.")
        return

    if not validate_phone(phone):
        messagebox.showwarning("Input Error", "Phone number must be exactly 10 digits.")
        return

    cursor.execute('INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)', (name, phone, email, address))
    conn.commit()
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_entries()
    refresh_contact_list()

# Function to view all contacts
def view_contacts():
    cursor.execute('SELECT name, phone FROM contacts')
    contacts = cursor.fetchall()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"👤 {contact[0]} - 📞 {contact[1]}")

# Function to search contacts
def search_contacts():
    search_query = simpledialog.askstring("Search", "Enter name or phone number to search:")
    if search_query:
        cursor.execute('SELECT name, phone FROM contacts WHERE name LIKE ? OR phone LIKE ?', (f'%{search_query}%', f'%{search_query}%'))
        contacts = cursor.fetchall()
        contact_list.delete(0, tk.END)
        for contact in contacts:
            contact_list.insert(tk.END, f"👤 {contact[0]} - 📞 {contact[1]}")
        if not contacts:
            messagebox.showinfo("No Results", "No contacts found.")

# Function to update contact
def update_contact():
    selected_contact = contact_list.curselection()
    if not selected_contact:
        messagebox.showwarning("Selection Error", "Please select a contact to update.")
        return
    
    contact_info = contact_list.get(selected_contact[0]).split(' - ')
    name = contact_info[0].replace("👤 ", "")
    phone = contact_info[1].replace("📞 ", "")

    new_name = simpledialog.askstring("Update", f"Enter new name for {name}:", initialvalue=name)
    new_phone = simpledialog.askstring("Update", f"Enter new phone number for {name}:", initialvalue=phone)
    new_email = simpledialog.askstring("Update", "Enter new email:", initialvalue="")
    new_address = simpledialog.askstring("Update", "Enter new address:", initialvalue="")

    if not new_name or not new_phone:
        messagebox.showwarning("Input Error", "Name and Phone Number are required.")
        return

    if not validate_phone(new_phone):
        messagebox.showwarning("Input Error", "Phone number must be exactly 10 digits.")
        return
    
    cursor.execute('UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE name=? AND phone=?', (new_name, new_phone, new_email, new_address, name, phone))
    conn.commit()
    messagebox.showinfo("Success", "Contact updated successfully!")
    refresh_contact_list()

# Function to delete contact
def delete_contact():
    selected_contact = contact_list.curselection()
    if not selected_contact:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")
        return
    
    contact_info = contact_list.get(selected_contact[0]).split(' - ')
    name = contact_info[0].replace("👤 ", "")
    phone = contact_info[1].replace("📞 ", "")
    
    cursor.execute('DELETE FROM contacts WHERE name=? AND phone=?', (name, phone))
    conn.commit()
    messagebox.showinfo("Success", "Contact deleted successfully!")
    refresh_contact_list()

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to refresh contact list
def refresh_contact_list():
    contact_list.delete(0, tk.END)
    view_contacts()

# Function to animate the contact list
def animate_contact_list():
    current = contact_list.curselection()
    if current:
        contact_list.itemconfig(current, {'bg':'#e0f7fa'})
    root.after(500, animate_contact_list)

# Setting up the main window
root = tk.Tk()
root.title("Contact Book 📒")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Create a canvas for the animated background
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack(fill="both", expand=True)

# Define gradient colors
gradient_colors = ["#ffcccc", "#ccffcc", "#ccccff", "#ffffcc", "#ccffff", "#ffccff"]
gradient_index = 0

# Initialize the gradient background
update_gradient()

# Create a frame for the contact book
frame = tk.Frame(root, bg='#f2f2f2', bd=5)
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)

# Title of the Contact Book
title_label = tk.Label(frame, text="CONTACT BOOK", bg='#f2f2f2', font=('Helvetica', 20, 'bold'))
title_label.pack(pady=10)

# Entry fields for contact information
entry_frame = tk.Frame(frame, bg='#f2f2f2')
entry_frame.pack(pady=10)

name_label = tk.Label(entry_frame, text="Name:", bg='#f2f2f2', font=('Helvetica', 12, 'bold'))
name_label.grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(entry_frame, width=30, font=('Helvetica', 12))
name_entry.grid(row=0, column=1, padx=5, pady=5)

phone_label = tk.Label(entry_frame, text="Phone:", bg='#f2f2f2', font=('Helvetica', 12, 'bold'))
phone_label.grid(row=1, column=0, padx=5, pady=5)

phone_entry = tk.Entry(entry_frame, width=30, font=('Helvetica', 12))
phone_entry.grid(row=1, column=1, padx=5, pady=5)

email_label = tk.Label(entry_frame, text="Email:", bg='#f2f2f2', font=('Helvetica', 12, 'bold'))
email_label.grid(row=2, column=0, padx=5, pady=5)

email_entry = tk.Entry(entry_frame, width=30, font=('Helvetica', 12))
email_entry.grid(row=2, column=1, padx=5, pady=5)

address_label = tk.Label(entry_frame, text="Address:", bg='#f2f2f2', font=('Helvetica', 12, 'bold'))
address_label.grid(row=3, column=0, padx=5, pady=5)

address_entry = tk.Entry(entry_frame, width=30, font=('Helvetica', 12))
address_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons to interact with contacts
button_frame = tk.Frame(frame, bg='#f2f2f2')
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Contact", command=add_contact, font=('Helvetica', 12, 'bold'), bg='#66ff66', fg='#000000')
add_button.grid(row=0, column=0, padx=5, pady=5)

update_button = tk.Button(button_frame, text="Update Contact", command=update_contact, font=('Helvetica', 12, 'bold'), bg='#66ccff', fg='#000000')
update_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact, font=('Helvetica', 12, 'bold'), bg='#ff6666', fg='#000000')
delete_button.grid(row=0, column=2, padx=5, pady=5)

search_button = tk.Button(button_frame, text="Search Contact", command=search_contacts, font=('Helvetica', 12, 'bold'), bg='#ffcc66', fg='#000000')
search_button.grid(row=0, column=3, padx=5, pady=5)

# Listbox to display contacts
contact_list = tk.Listbox(frame, width=50, height=15, font=('Helvetica', 12))
contact_list.pack(pady=10)

# Load initial contacts
refresh_contact_list()

# Start animation
animate_contact_list()

# Run the application
root.mainloop()

# Close database connection
conn.close()
