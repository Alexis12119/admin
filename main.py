import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
from mysql.connector import Error
from db import create_connection

image_url = "https://www.example.com/placeholder.png"

window = tk.Tk()
window.title("Dashboard")
window.geometry("800x400")

bg_color = "#0a9ea8"
button_bg_color = "#fdd97e"
text_color = "black"
form_bg_color = "white"
sidebar_expanded = True

window.configure(bg=bg_color)

sidebar_frame = None
content_frame = None
toggle_button = None

window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=1)

def show_main_interface(real_name):
    global sidebar_frame, content_frame
    
    for widget in window.winfo_children():
        widget.destroy()
    
    sidebar_frame = tk.Frame(window, width=200, bg=bg_color)
    separator_frame = tk.Frame(window, width=1, bg="white")
    content_frame = tk.Frame(window, bg=bg_color)
    
    sidebar_frame.grid(row=0, column=0, sticky="ns")
    separator_frame.grid(row=0, column=1, sticky="ns")
    content_frame.grid(row=0, column=2, sticky="nsew")

    icon_placeholder = tk.Frame(sidebar_frame, width=50, height=50, bg="white")
    icon_placeholder.pack(pady=(5, 10), padx=10)

    sidebar_button_style = "Sidebar.TButton"
    style.configure(sidebar_button_style,
                    background=bg_color,
                    foreground=text_color,
                    borderwidth=0,
                    padding=5)
    style.map(sidebar_button_style,
              background=[("active", bg_color)],
              foreground=[("active", text_color)])

     # Add a horizontal line
    line = tk.Frame(sidebar_frame, height=1, bg="white")
    line.pack(fill=tk.X, padx=10)


    home_button = ttk.Button(sidebar_frame, text="    Home", command=lambda: show_home_page(real_name), style=sidebar_button_style)
    home_button.pack(pady=(5, 10))

    teacher_button = ttk.Button(sidebar_frame, text="󱪌  Teacher", command=lambda: show_teacher_form(real_name), style=sidebar_button_style)
    teacher_button.pack(pady=10)

    student_button = ttk.Button(sidebar_frame, text="  Student", command=lambda: show_student_form(real_name), style=sidebar_button_style)
    student_button.pack(pady=10)

    line = tk.Frame(sidebar_frame, height=1, bg="white")
    line.pack(fill=tk.X, padx=10)

    admin_button = ttk.Button(sidebar_frame, text="󰘰   Admin", command=lambda: show_admin_form(real_name), style=sidebar_button_style)
    admin_button.pack(pady=10)

    setting_button = ttk.Button(sidebar_frame, text="   Settings", command=lambda: show_settings_page(real_name), style=sidebar_button_style)
    setting_button.pack(pady=10)

    show_home_page(real_name)

def show_blank_page(role):
    for widget in window.winfo_children():
        widget.destroy()

    blank_frame = tk.Frame(window, bg=bg_color)
    blank_frame.pack(expand=True)

    welcome_label = tk.Label(blank_frame, text=f"Welcome, {role}!", font=("Arial", 20), bg=bg_color, fg=text_color)
    welcome_label.pack(pady=20)

    message_label = tk.Label(blank_frame, text="This is a blank page for your role.", font=("Arial", 14), bg=bg_color, fg=text_color)
    message_label.pack(pady=10)

    back_button = ttk.Button(blank_frame, text="Back to Login", command=show_login_page, style="TButton")
    back_button.pack(pady=10)

def get_image():
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            response.raw.decode_content = True
            return tk.PhotoImage(data=response.content)
        else:
            return None
    except requests.exceptions.RequestException as e:
        return e.response.status_code

placeholder_image = get_image()

def show_home_page(real_name):
    for widget in content_frame.winfo_children():
        widget.destroy()

    header_frame = tk.Frame(content_frame, bg=bg_color)
    header_frame.pack(pady=(10, 0), fill="x")

    title_label = tk.Label(header_frame, text="Home", font=("Arial", 16), fg=text_color, bg=bg_color)
    title_label.pack(side="left", padx=(10, 0))

    username_label = tk.Label(header_frame, text=f"User: {real_name}", font=("Arial", 12), fg=text_color, bg=bg_color)
    username_label.pack(side="right", padx=(0, 10))

    separator = tk.Frame(content_frame, height=2, bg="white")
    separator.pack(fill="x", padx=20, pady=(0, 10))

    image_label = tk.Label(content_frame, image=placeholder_image, bg=bg_color)
    image_label.pack(pady=10)

    welcome_label = tk.Label(content_frame, text="WELCOME ADMIN!", font=("Arial", 16), fg=button_bg_color, bg=bg_color)
    welcome_label.pack()

    prompt_label = tk.Label(content_frame, text="Who do you want to create an account?", font=("Arial", 12), bg=bg_color, fg=text_color)
    prompt_label.pack(pady=10)

    button_frame = tk.Frame(content_frame, bg=bg_color)
    button_frame.pack()

    admin_button = ttk.Button(button_frame, text="ADMIN", command=lambda: show_admin_form(real_name))
    admin_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    teacher_button = ttk.Button(button_frame, text="TEACHER", command=lambda: show_teacher_form(real_name), style="TButton")
    teacher_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    student_button = ttk.Button(button_frame, text="STUDENT", command=lambda: show_student_form(real_name), style="TButton")
    student_button.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")


def show_admin_form(real_name):
    for widget in content_frame.winfo_children():
        widget.destroy()


    header_frame = tk.Frame(content_frame, bg=bg_color)
    header_frame.pack(pady=(10, 0), fill="x")

    title_label = tk.Label(header_frame, text="Admin Dashboard", font=("Arial", 16), fg=text_color, bg=bg_color)
    title_label.pack(side="left", padx=(10, 0))

    username_label = tk.Label(header_frame, text=f"User: {real_name}", font=("Arial", 12), fg=text_color, bg=bg_color)
    username_label.pack(side="right", padx=(0, 10))


    separator = tk.Frame(content_frame, height=2, bg="white")
    separator.pack(fill="x", padx=20, pady=(0, 10))

    form_container = tk.Frame(content_frame, bg=form_bg_color, padx=20, pady=20)  # Adjusted padding
    form_container.pack(padx=20, pady=(0, 20))


    labels = ["Admin Username", "Admin First Name", "Admin Last Name", "Admin Email", "Admin ID", "Password"]
    entries = {}

    for i, label in enumerate(labels):
        tk.Label(form_container, text=label, bg=form_bg_color, fg=text_color).grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entry = ttk.Entry(form_container)
        entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
        entries[label] = entry

    def create_account():
        admin_username = entries["Admin Username"].get()
        admin_first_name = entries["Admin First Name"].get()
        admin_last_name = entries["Admin Last Name"].get()
        admin_email = entries["Admin Email"].get()
        admin_id = entries["Admin ID"].get()
        password = entries["Password"].get()

        if all([admin_username, admin_first_name, admin_last_name, admin_email, admin_id]):
            # Validate ID
            if not admin_id.isdigit():
                messagebox.showerror("Invalid Input", "Admin ID must be an integer.")
                return
            # Validate non-numeric fields
            if not (admin_username.isalpha() and admin_first_name.isalpha() and admin_last_name.isalpha()):
                messagebox.showerror("Invalid Input", "Username, First Name, and Last Name must contain only alphabetic characters.")
                return
           # Validate email format (simple check)
            if "@" not in admin_email or "." not in admin_email:
                messagebox.showerror("Invalid Input", "Please enter a valid email address.")
                return
            confirmation = messagebox.askokcancel("Confirm Account Creation", "Are you sure you want to create this account?")
            if confirmation:
                connection = create_connection()
                if connection:
                    cursor = connection.cursor()
                    # Check if ID already exists
                    cursor.execute("SELECT COUNT(*) FROM Admin WHERE admin_id = %s", (admin_id,))
                    if cursor.fetchone()[0] > 0:
                        messagebox.showerror("ID Exists", "An account with this Admin ID already exists.")
                    else:
                        sql = "INSERT INTO Admin (admin_id, username, first_name, last_name, email, password) VALUES (%s, %s, %s, %s, %s, %s)"
                        try:
                            cursor.execute(sql, (admin_id, admin_username, admin_first_name, admin_last_name, admin_email, password))
                            connection.commit()
                            messagebox.showinfo("Account Created", "Admin account successfully created!")
                        except Error as e:
                            messagebox.showerror("Error", f"Failed to create account: {e}")
                    cursor.close()
                    connection.close()
            else:
                messagebox.showinfo("Action Cancelled", "Account creation cancelled.")
        else:
            messagebox.showwarning("Incomplete Form", "Please fill out all fields!")

    create_button = ttk.Button(form_container, text="Create Account", command=create_account, style="TButton")
    create_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

def show_teacher_form(real_name):
    for widget in content_frame.winfo_children():
        widget.destroy()

    header_frame = tk.Frame(content_frame, bg=bg_color)
    header_frame.pack(pady=(10, 0), fill="x")

    title_label = tk.Label(header_frame, text="Teacher Dashboard", font=("Arial", 16), fg=text_color, bg=bg_color)
    title_label.pack(side="left", padx=(10, 0))

    username_label = tk.Label(header_frame, text=f"User: {real_name}", font=("Arial", 12), fg=text_color, bg=bg_color)
    username_label.pack(side="right", padx=(0, 10))

    separator = tk.Frame(content_frame, height=2, bg="white")
    separator.pack(fill="x", padx=20, pady=(0, 10))

    form_container = tk.Frame(content_frame, bg=form_bg_color, padx=20, pady=20)
    form_container.pack(padx=20, pady=(0, 20))

    labels = ["Teacher Username", "Teacher First Name", "Teacher Last Name", "Teacher Email", "Teacher ID", "Password"]
    entries = {}

    for i, label in enumerate(labels):
        tk.Label(form_container, text=label, bg=form_bg_color, fg=text_color).grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entry = ttk.Entry(form_container)
        entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
        entries[label] = entry

    def create_account():
        teacher_username = entries["Teacher Username"].get()
        teacher_first_name = entries["Teacher First Name"].get()
        teacher_last_name = entries["Teacher Last Name"].get()
        teacher_email = entries["Teacher Email"].get()
        teacher_id = entries["Teacher ID"].get()
        password = entries["Password"].get()

        if all([teacher_username, teacher_first_name, teacher_last_name, teacher_email, teacher_id]):
            # Validate ID
            if not teacher_id.isdigit():
                messagebox.showerror("Invalid Input", "Teacher ID must be an integer.")
                return
            
            # Validate non-numeric fields
            if not (teacher_username.isalpha() and teacher_first_name.isalpha() and teacher_last_name.isalpha()):
                messagebox.showerror("Invalid Input", "Username, First Name, and Last Name must contain only alphabetic characters.")
                return
            
            # Validate email format (simple check)
            if "@" not in teacher_email or "." not in teacher_email:
                messagebox.showerror("Invalid Input", "Please enter a valid email address.")
                return

            confirmation = messagebox.askokcancel("Confirm Account Creation", "Are you sure you want to create this account?")
            if confirmation:
                connection = create_connection()
                if connection:
                    cursor = connection.cursor()
                    # Check if ID already exists
                    cursor.execute("SELECT COUNT(*) FROM Teacher WHERE teacher_id = %s", (teacher_id,))
                    if cursor.fetchone()[0] > 0:
                        messagebox.showerror("ID Exists", "An account with this Teacher ID already exists.")
                    else:
                        sql = "INSERT INTO Teacher (teacher_id, username, first_name, last_name, email, password) VALUES (%s, %s, %s, %s, %s, %s)"
                        try:
                            cursor.execute(sql, (teacher_id, teacher_username, teacher_first_name, teacher_last_name, teacher_email, password))
                            connection.commit()
                            messagebox.showinfo("Account Created", "Teacher account successfully created!")
                        except Error as e:
                            messagebox.showerror("Error", f"Failed to create account: {e}")
                    cursor.close()
                    connection.close()
            else:
                messagebox.showinfo("Action Cancelled", "Account creation cancelled.")
        else:
            messagebox.showwarning("Incomplete Form", "Please fill out all fields!")

    create_button = ttk.Button(form_container, text="Create Account", command=create_account, style="TButton")
    create_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

def show_student_form(real_name):
    for widget in content_frame.winfo_children():
        widget.destroy()

    header_frame = tk.Frame(content_frame, bg=bg_color)
    header_frame.pack(pady=(10, 0), fill="x")

    title_label = tk.Label(header_frame, text="Student Dashboard", font=("Arial", 16), fg=text_color, bg=bg_color)
    title_label.pack(side="left", padx=(10, 0))

    username_label = tk.Label(header_frame, text=f"User: {real_name}", font=("Arial", 12), fg=text_color, bg=bg_color)
    username_label.pack(side="right", padx=(0, 10))

    separator = tk.Frame(content_frame, height=2, bg="white")
    separator.pack(fill="x", padx=20, pady=(0, 10))

    form_container = tk.Frame(content_frame, bg=form_bg_color, padx=20, pady=20)
    form_container.pack(padx=20, pady=(0, 20))

    labels = ["Student Username", "Student First Name", "Student Last Name", "Guardian's Name", "Contact Number", "Student ID", "Password"]
    entries = {}

    for i, label in enumerate(labels):
        tk.Label(form_container, text=label, bg=form_bg_color, fg=text_color).grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entry = ttk.Entry(form_container)
        entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
        entries[label] = entry

    def create_account():
        student_username = entries["Student Username"].get()
        student_first_name = entries["Student First Name"].get()
        student_last_name = entries["Student Last Name"].get()
        guardian_name = entries["Guardian's Name"].get()
        contact_number = entries["Contact Number"].get()
        student_id = entries["Student ID"].get()
        password = entries["Password"].get()

        if all([student_username, student_first_name, student_last_name, guardian_name, contact_number, student_id]):
            # Validate ID
            if not student_id.isdigit():
                messagebox.showerror("Invalid Input", "Student ID must be an integer.")
                return
            
            # Validate Contact Number
            if not contact_number.isdigit():
                messagebox.showerror("Invalid Input", "Contact Number must be an integer.")
                return
            
            # Validate non-numeric fields
            if not (student_username.isalpha() and student_first_name.isalpha() and student_last_name.isalpha() and guardian_name.isalpha()):
                messagebox.showerror("Invalid Input", "Username, First Name, Last Name, and Guardian's Name must contain only alphabetic characters.")
                return
            
            confirmation = messagebox.askokcancel("Confirm Account Creation", "Are you sure you want to create this account?")
            if confirmation:
                connection = create_connection()
                if connection:
                    cursor = connection.cursor()
                    # Check if ID already exists
                    cursor.execute("SELECT COUNT(*) FROM Student WHERE student_id = %s", (student_id,))
                    if cursor.fetchone()[0] > 0:
                        messagebox.showerror("ID Exists", "An account with this Student ID already exists.")
                    else:
                        sql = "INSERT INTO Student (student_id, username, first_name, last_name, guardian_name, contact_number, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        try:
                            cursor.execute(sql, (student_id, student_username, student_first_name, student_last_name, guardian_name, contact_number, password))
                            connection.commit()
                            messagebox.showinfo("Account Created", "Student account successfully created!")
                        except Error as e:
                            messagebox.showerror("Error", f"Failed to create account: {e}")
                    cursor.close()
                    connection.close()
            else:
                messagebox.showinfo("Action Cancelled", "Account creation cancelled.")
        else:
            messagebox.showwarning("Incomplete Form", "Please fill out all fields!")

    create_button = ttk.Button(form_container, text="Create Account", command=create_account, style="TButton")
    create_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

def show_settings_page(real_name):
    for widget in content_frame.winfo_children():
        widget.destroy()

    header_frame = tk.Frame(content_frame, bg=bg_color)
    header_frame.pack(pady=(10, 0), fill="x")

    title_label = tk.Label(header_frame, text="Settings", font=("Arial", 16), fg=text_color, bg=bg_color)
    title_label.pack(side="left", padx=(10, 0))

    username_label = tk.Label(header_frame, text=f"User: {real_name}", font=("Arial", 12), fg=text_color, bg=bg_color)
    username_label.pack(side="right", padx=(0, 10))

    separator = tk.Frame(content_frame, height=2, bg="white")
    separator.pack(fill="x", padx=20, pady=(0, 10))

    options = ["Language", "About", "Help & Support"]

    settings_frame = tk.Frame(content_frame, bg=bg_color)
    settings_frame.pack(pady=20)

    for option in options:
        button = ttk.Button(settings_frame, text=option, style="TButton")
        button.pack(pady=5)

    def confirm_logout():
        confirmation = messagebox.askyesno("Confirm Logout", "Are you sure you want to log out?")
        if confirmation:
            show_login_page()

    logout_button = ttk.Button(settings_frame, text="Logout", command=confirm_logout, style="TButton")
    logout_button.pack(pady=5)


def show_login_page():
    global toggle_button 
    toggle_button = None

    for widget in window.winfo_children():
        widget.destroy()

    main_frame = tk.Frame(window)
    main_frame.pack(expand=True, fill="both")

    left_frame = tk.Frame(main_frame, bg="white")
    left_frame.pack(side="right", expand=True, fill="both")

    right_frame = tk.Frame(main_frame, bg=bg_color, padx=20, pady=20)
    right_frame.pack(side="left", expand=True, fill="both")

    title_label = tk.Label(right_frame, text="Login", font=("Arial", 20), bg=bg_color, fg=text_color)
    title_label.pack(pady=20)

    username_label = tk.Label(right_frame, text="Username:", bg=bg_color, fg=text_color)
    username_label.pack()
    username_entry = ttk.Entry(right_frame)
    username_entry.pack(pady=5)

    password_label = tk.Label(right_frame, text="Password:", bg=bg_color, fg=text_color)
    password_label.pack()
    password_entry = ttk.Entry(right_frame, show="*")
    password_entry.pack(pady=5)

    role_label = tk.Label(right_frame, text="Role:", bg=bg_color, fg=text_color)
    role_label.pack()
    role_combobox = ttk.Combobox(right_frame, values=["Admin", "Teacher", "Student"], state="readonly")
    role_combobox.set("Admin") 
    role_combobox.pack(pady=5)

    def login():
        username = username_entry.get()
        password = password_entry.get()
        role = role_combobox.get()
        
        if username and password and role:
            connection = create_connection()
            if connection:
                cursor = connection.cursor()
                if role == "Admin":
                    cursor.execute("SELECT CONCAT(first_name, ' ', last_name) FROM Admin WHERE username = %s AND password = %s", (username, password))
                elif role == "Teacher":
                    cursor.execute("SELECT CONCAT(first_name, ' ', last_name) FROM Teacher WHERE username = %s AND password = %s", (username, password))
                elif role == "Student":
                    cursor.execute("SELECT CONCAT(first_name, ' ', last_name) FROM Student WHERE username = %s AND password = %s", (username, password))

                result = cursor.fetchone()
                cursor.close()
                connection.close()

                if result:
                    real_name = result[0]
                    print(real_name)
                    show_main_interface(real_name) if role == "Admin" else show_blank_page(role)
                else:
                    messagebox.showerror("Login Error", "Invalid username or password")
            else:
                messagebox.showerror("Database Error", "Unable to connect to the database.")
        else:
            messagebox.showerror("Login Error", "Please enter username, password, and select a role.")

    login_button = ttk.Button(right_frame, text="Login", command=login, style="TButton")
    login_button.pack(pady=10)

    login_button = ttk.Button(right_frame, text="Login", command=login, style="TButton")
    login_button.pack(pady=10)

style = ttk.Style()
style.configure("TButton",
                background=button_bg_color,
                foreground=text_color,
                borderwidth=0,
                padding=5)
style.map("TButton",
          background=[("active", "#fdd97e")],
          foreground=[("active", "black")])

show_login_page()

window.mainloop()
