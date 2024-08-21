import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageTk
import random
import string

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

# Function to check if the password meets constraints
def check_constraints(password):
    min_uppercase = int(min_uppercase_entry.get())
    min_lowercase = int(min_lowercase_entry.get())
    min_digits = int(min_digits_entry.get())
    min_special = int(min_special_entry.get())

    upper_count = sum(1 for c in password if c.isupper())
    lower_count = sum(1 for c in password if c.islower())
    digit_count = sum(1 for c in password if c.isdigit())
    special_count = sum(1 for c in password if c in string.punctuation)

    if (upper_count >= min_uppercase and
        lower_count >= min_lowercase and
        digit_count >= min_digits and
        special_count >= min_special):
        return True
    return False

# Function to generate a random password with constraints
def generate_password():
    try:
        length = int(length_entry.get())
        min_uppercase = int(min_uppercase_entry.get())
        min_lowercase = int(min_lowercase_entry.get())
        min_digits = int(min_digits_entry.get())
        min_special = int(min_special_entry.get())

        if length < min_uppercase + min_lowercase + min_digits + min_special:
            messagebox.showerror("Error", "Total length must be greater than or equal to the sum of constraints.")
            return

        characters = {
            'upper': string.ascii_uppercase,
            'lower': string.ascii_lowercase,
            'digits': string.digits,
            'special': string.punctuation
        }

        password = []
        password.extend(random.choices(characters['upper'], k=min_uppercase))
        password.extend(random.choices(characters['lower'], k=min_lowercase))
        password.extend(random.choices(characters['digits'], k=min_digits))
        password.extend(random.choices(characters['special'], k=min_special))
        
        remaining_length = length - len(password)
        all_characters = characters['upper'] + characters['lower'] + characters['digits'] + characters['special']
        password.extend(random.choices(all_characters, k=remaining_length))
        
        random.shuffle(password)
        password = ''.join(password)
        password_var.set(password)
    
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for constraints.")

# Function to validate user-set password
def validate_password():
    user_password = user_password_entry.get()
    if check_constraints(user_password):
        messagebox.showinfo("Success", "Your password meets the constraints!")
        generate_password()  # Optionally generate a new password
    else:
        messagebox.showerror("Error", "Your password does not meet the constraints. Please try again.")

# Setting up the main window
root = tk.Tk()
root.title("Password Generator with Constraints")

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

# Initialize the gradient background
update_gradient()

# Create a frame for the password generator
frame = tk.Frame(root, bg='#f2f2f2', bd=5)
frame.place(relwidth=0.5, relheight=0.7, relx=0.25, rely=0.2)

# Title of the Password Generator
title_label = tk.Label(frame, text="PASSWORD GENERATOR", bg='#f2f2f2', font=('Helvetica', 20, 'bold'))
title_label.pack(pady=10)

# Entry box to input password length
length_frame = tk.Frame(frame, bg='#f2f2f2')
length_frame.pack(pady=10)

length_label = tk.Label(length_frame, text="PASSWORD LENGTH:", bg='#f2f2f2', font=('Helvetica', 14, 'bold'))
length_label.pack(side=tk.LEFT, padx=5)

length_entry = tk.Entry(length_frame, width=5, font=('Helvetica', 14, 'bold'))
length_entry.pack(side=tk.LEFT, padx=5)

# Constraints Entry
constraints_frame = tk.Frame(frame, bg='#f2f2f2')
constraints_frame.pack(pady=10)

min_uppercase_label = tk.Label(constraints_frame, text="Min Uppercase:", bg='#f2f2f2', font=('Helvetica', 12, 'bold'))
min_uppercase_label.grid(row=0, column=0, padx=5, pady=5)

min_uppercase_entry = tk.Entry(constraints_frame, width=5, font=('Helvetica', 12, 'bold'))
min_uppercase_entry.grid(row=0, column=1, padx=5, pady=5)

min_lowercase_label = tk.Label(constraints_frame, text="Min Lowercase:", bg='#f2f2f2', font=('Helvetica', 12, 'bold'))
min_lowercase_label.grid(row=1, column=0, padx=5, pady=5)

min_lowercase_entry = tk.Entry(constraints_frame, width=5, font=('Helvetica', 12, 'bold'))
min_lowercase_entry.grid(row=1, column=1, padx=5, pady=5)

min_digits_label = tk.Label(constraints_frame, text="Min Digits:", bg='#f2f2f2', font=('Helvetica', 12, 'bold'))
min_digits_label.grid(row=2, column=0, padx=5, pady=5)

min_digits_entry = tk.Entry(constraints_frame, width=5, font=('Helvetica', 12, 'bold'))
min_digits_entry.grid(row=2, column=1, padx=5, pady=5)

min_special_label = tk.Label(constraints_frame, text="Min Special:", bg='#f2f2f2', font=('Helvetica', 12, 'bold'))
min_special_label.grid(row=3, column=0, padx=5, pady=5)

min_special_entry = tk.Entry(constraints_frame, width=5, font=('Helvetica', 12, 'bold'))
min_special_entry.grid(row=3, column=1, padx=5, pady=5)

# Button to generate password
generate_button = tk.Button(frame, text="Generate Random Password", command=generate_password, font=('Helvetica', 14, 'bold'), bg='#66ff66')
generate_button.pack(pady=10)

# Label to display the generated password
password_var = tk.StringVar()
password_label = tk.Label(frame, textvariable=password_var, bg='#f2f2f2', font=('Helvetica', 14, 'bold'))
password_label.pack(pady=10)

# Entry box for user-defined password
user_password_frame = tk.Frame(frame, bg='#f2f2f2')
user_password_frame.pack(pady=10)

user_password_label = tk.Label(user_password_frame, text="SET YOUR PASSWORD:", bg='#f2f2f2', font=('Helvetica', 12, 'bold'))
user_password_label.pack(side=tk.LEFT, padx=5)

user_password_entry = tk.Entry(user_password_frame, width=30, font=('Helvetica', 12, 'bold'))
user_password_entry.pack(side=tk.LEFT, padx=5)

validate_button = tk.Button(user_password_frame, text="Validate Password", command=validate_password, font=('Helvetica', 12, 'bold'), bg='#66ff66')
validate_button.pack(side=tk.LEFT, padx=5)

# Run the application
root.mainloop()
