import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from mysql.connector import Error
from db import create_connection

window = tk.Tk()
window.title("E-Learning")
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
    
    # Destroy any existing widgets in the window
    for widget in window.winfo_children():
        widget.destroy()
    
    # Sidebar setup with a wider layout but less vertical space between items
    sidebar_frame = tk.Frame(window, width=300, bg=bg_color)  # Sidebar width
    separator_frame = tk.Frame(window, width=2, bg="white")
    content_frame = tk.Frame(window, bg=bg_color)
    
    # Grid layout
    sidebar_frame.grid(row=0, column=0, sticky="ns")
    separator_frame.grid(row=0, column=1, sticky="ns")
    content_frame.grid(row=0, column=2, sticky="nsew")

    # Icon placeholder at the top of the sidebar
    icon_placeholder = tk.Frame(sidebar_frame, width=60, height=60, bg="white")
    icon_placeholder.pack(pady=(10, 10), padx=20)  # Adjusted top padding here

    # Sidebar button style
    sidebar_button_style = "Sidebar.TButton"
    style.configure(sidebar_button_style,
                    background=bg_color,
                    foreground=text_color,
                    borderwidth=0,
                    padding=10)  # Button padding
    style.map(sidebar_button_style,
              background=[("active", bg_color)],
              foreground=[("active", text_color)])

    # Add a horizontal line (divider)
    line = tk.Frame(sidebar_frame, height=2, bg="white")
    line.pack(fill=tk.X, padx=20)  # Increased the padding for the line

    # Sidebar buttons with reduced vertical padding between items
    home_button = ttk.Button(sidebar_frame, text="    Home", command=lambda: show_home_page(real_name), style=sidebar_button_style)
    home_button.pack(pady=(5, 10), padx=40)  # Reduced top and bottom padding

    teacher_button = ttk.Button(sidebar_frame, text="󱪌  Teacher", command=lambda: show_teacher_form(real_name), style=sidebar_button_style)
    teacher_button.pack(pady=10, padx=40)

    student_button = ttk.Button(sidebar_frame, text="  Student", command=lambda: show_student_form(real_name), style=sidebar_button_style)
    student_button.pack(pady=10, padx=40)

    # Add another horizontal line (divider)
    line = tk.Frame(sidebar_frame, height=2, bg="white")
    line.pack(fill=tk.X, padx=20, pady=(10, 5))  # Reduced padding around the line

    admin_button = ttk.Button(sidebar_frame, text="󰘰   Admin", command=lambda: show_admin_form(real_name), style=sidebar_button_style)
    admin_button.pack(pady=10, padx=40)

    setting_button = ttk.Button(sidebar_frame, text="   Settings", command=lambda: show_settings_page(real_name), style=sidebar_button_style)
    setting_button.pack(pady=10, padx=40)

    # Display the home page initially
    show_home_page(real_name)

def show_home_page(real_name):
    for widget in content_frame.winfo_children():
        widget.destroy()

    header_frame = tk.Frame(content_frame, bg=bg_color)
    header_frame.pack(pady=(10, 0), fill="x", anchor="center")

    title_label = tk.Label(header_frame, text="Home", font=("Arial", 16), fg=text_color, bg=bg_color)
    title_label.pack(side="left", padx=(10, 0))

    username_label = tk.Label(header_frame, text=f"{real_name}", font=("Arial", 12), fg=text_color, bg=bg_color)
    username_label.pack(side="right", padx=(0, 10))

    line = tk.Frame(content_frame, height=1, bg="white")
    line.pack(fill="x", padx=20, pady=(0, 30))

    welcome_label = tk.Label(content_frame, text="WELCOME ADMIN!", font=("Arial", 26, "bold"), fg=button_bg_color, bg=bg_color)
    welcome_label.pack(pady=20, anchor="center")

    prompt_label = tk.Label(content_frame, text="Who do you want to create an account?", font=("Arial", 12), bg=bg_color, fg=text_color)
    prompt_label.pack(pady=10, anchor="center")

    button_frame = tk.Frame(content_frame, bg=bg_color)
    button_frame.pack(anchor="center", pady=10)

    button_frame.grid_columnconfigure((0, 1, 2), weight=1)

    admin_button = ttk.Button(button_frame, text="ADMIN", command=lambda: show_admin_form(real_name))
    admin_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    teacher_button = ttk.Button(button_frame, text="TEACHER", command=lambda: show_teacher_form(real_name))
    teacher_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    student_button = ttk.Button(button_frame, text="STUDENT", command=lambda: show_student_form(real_name))
    student_button.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

    content_frame.grid_rowconfigure(0, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)

def show_admin_form(real_name):
    for widget in content_frame.winfo_children():
        widget.destroy()

    header_frame = tk.Frame(content_frame, bg=bg_color)
    header_frame.pack(pady=(10, 0), fill="x")

    title_label = tk.Label(header_frame, text="Admin Dashboard", font=("Arial", 16), fg=text_color, bg=bg_color)
    title_label.pack(side="left", padx=(10, 0))

    username_label = tk.Label(header_frame, text=f"{real_name}", font=("Arial", 12), fg=text_color, bg=bg_color)
    username_label.pack(side="right", padx=(0, 10))

    line = tk.Frame(content_frame, height=1, bg="white")
    line.pack(fill="x", padx=20, pady=(0, 30))

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

    username_label = tk.Label(header_frame, text=f"{real_name}", font=("Arial", 12), fg=text_color, bg=bg_color)
    username_label.pack(side="right", padx=(0, 10))

    line = tk.Frame(content_frame, height=1, bg="white")
    line.pack(fill="x", padx=20, pady=(0, 30))

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

    username_label = tk.Label(header_frame, text=f"{real_name}", font=("Arial", 12), fg=text_color, bg=bg_color)
    username_label.pack(side="right", padx=(0, 10))

    line = tk.Frame(content_frame, height=1, bg="white")
    line.pack(fill="x", padx=20, pady=(0, 30))

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

    username_label = tk.Label(header_frame, text=f"{real_name}", font=("Arial", 12), fg=text_color, bg=bg_color)
    username_label.pack(side="right", padx=(0, 10))

    line = tk.Frame(content_frame, height=1, bg="white")
    line.pack(fill="x", padx=20, pady=(0, 30))

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

def create_main_frame():
    global content_frame
    
    for widget in window.winfo_children():
        widget.destroy()
    
    content_frame = tk.Frame(window, bg=bg_color)
    content_frame.pack(expand=True, fill="both")
    
    return content_frame

def show_student_dashboard():
    content_frame = create_main_frame()

    header_frame = tk.Frame(content_frame, bg=bg_color)
    header_frame.pack(pady=(10, 30), fill="x")

    logo_placeholder = tk.Frame(content_frame, width=500, height=150, bg="white")
    logo_placeholder.pack(pady=(5, 10), padx=10)

    buttons_frame = tk.Frame(content_frame, bg=bg_color)
    buttons_frame.pack(pady=(20, 10))

    def on_button_click(activity):
        messagebox.showinfo("Button Clicked", f"You clicked: {activity}")

    button1 = ttk.Button(buttons_frame, text="Sining at Aktibidad", command=lambda: on_button_click("Sining at Aktibidad"), style="TButton")
    button1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    button2 = ttk.Button(buttons_frame, text="Alamat", command=lambda: on_button_click("Alamat"), style="TButton") 
    button2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    button3 = ttk.Button(buttons_frame, text="Mga Aralin", command=lambda: on_button_click("Mga Aralin"), style="TButton")
    button3.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

    def confirm_logout():
        confirmation = messagebox.askyesno("Confirm Logout", "Are you sure you want to log out?")
        if confirmation:
            show_login_page()

    button4 = ttk.Button(buttons_frame, text="Logout", command=confirm_logout, style="TButton")
    button4.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

def show_teacher_dashboard(real_name):
    content_frame = create_main_frame()

    circle_frame = tk.Frame(content_frame, bg=bg_color)
    circle_frame.pack(pady=(10, 0), fill="x")

    circle_canvas = tk.Canvas(circle_frame, width=50, height=50, bg=bg_color, highlightthickness=0)
    circle_canvas.pack(side="left", padx=5)
    circle_canvas.create_oval(5, 5, 45, 45, fill="white")

    teacher_label = tk.Label(circle_frame, text="Teacher    ", font=("Arial", 12), fg=text_color, bg=bg_color)
    teacher_label.pack(side="left", padx=5)

    vertical_line = tk.Frame(circle_frame, width=1, bg="white")
    vertical_line.pack(side="left", fill="y", padx=(5, 0))

    real_name_label = tk.Label(circle_frame, text=real_name, font=("Arial", 12), fg=text_color, bg=bg_color)
    real_name_label.pack(side="right", padx=5)

    # Add the Dashboard label here
    dashboard_label = tk.Label(circle_frame, text="Dashboard", font=("Arial", 12, "bold"), fg=text_color, bg=bg_color)
    dashboard_label.pack(side="left", padx=(10, 0))

    line = tk.Frame(content_frame, height=1, bg="white")
    line.pack(fill=tk.X, padx=10)

    sidebar_frame = tk.Frame(content_frame, bg=bg_color)
    sidebar_frame.pack(side="left", padx=20, pady=(0, 0), anchor="n")

    sidebar_line = tk.Frame(content_frame, width=1, bg="white")
    sidebar_line.pack(side="left", fill="y", padx=(5, 0), pady=(10, 0))
    dashboard_button = ttk.Button(sidebar_frame, text="Dashboard", style="Sidebar.TButton")
    dashboard_button.pack(pady=10, fill="x")

    portfolio_button = ttk.Button(sidebar_frame, text="Portfolio", style="Sidebar.TButton")
    portfolio_button.pack(pady=10, fill="x")

    students_button = ttk.Button(sidebar_frame, text="Students", style="Sidebar.TButton")
    students_button.pack(pady=10, fill="x")

    reports_button = ttk.Button(sidebar_frame, text="Reports", style="Sidebar.TButton")
    reports_button.pack(pady=10, fill="x")

    line = tk.Frame(sidebar_frame, height=1, bg="white")
    line.pack(fill="x", padx=10)

    profile_button = ttk.Button(sidebar_frame, text="My Profile", style="Sidebar.TButton")
    profile_button.pack(pady=10, fill="x")

    settings_button = ttk.Button(sidebar_frame, text="Settings", style="Sidebar.TButton")
    settings_button.pack(pady=10, fill="x")

    line = tk.Frame(sidebar_frame, height=1, bg="white")
    line.pack(fill="x", padx=10)

    help_button = ttk.Button(sidebar_frame, text="Help & Support", style="Sidebar.TButton")
    help_button.pack(pady=10, fill="x")

    def confirm_logout():
        confirmation = messagebox.askyesno("Confirm Logout", "Are you sure you want to log out?")
        if confirmation:
            show_login_page()

    logout_button = ttk.Button(sidebar_frame, text="Logout", command=confirm_logout, style="Sidebar.TButton")
    logout_button.pack(pady=(30, 10), fill="x")

    main_content_frame = tk.Frame(content_frame, bg=bg_color)
    main_content_frame.pack(side="right", padx=20, pady=(10, 0), fill="both", expand=True)

    students_label = tk.Label(main_content_frame, text="Students: 30", font=("Arial", 14), fg=text_color, bg=bg_color)
    students_label.grid(row=0, column=0, padx=10, pady=10)

    attendance_label = tk.Label(main_content_frame, text="Attendance: 30", font=("Arial", 14), fg=text_color, bg=bg_color)
    attendance_label.grid(row=0, column=1, padx=10, pady=10)

    grades_label = tk.Label(main_content_frame, text="Grades: 89%", font=("Arial", 14), fg=text_color, bg=bg_color)
    grades_label.grid(row=0, column=2, padx=10, pady=10)

    add_button = ttk.Button(main_content_frame, text="Add New", style="Main.TButton")
    add_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    delete_button = ttk.Button(main_content_frame, text="Delete", style="Main.TButton")
    delete_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    edit_button = ttk.Button(main_content_frame, text="Edit", style="Main.TButton")
    edit_button.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

    lesson_label = tk.Label(main_content_frame, text="Lessons", font=("Arial", 14), fg=text_color, bg=bg_color)
    lesson_label.grid(row=2, column=0, padx=10, pady=(10, 5), sticky="w")

    sort_var = tk.StringVar(main_content_frame)
    sort_var.set("Sort by")

    sort_dropdown = ttk.OptionMenu(main_content_frame, sort_var, "Time", "Time", "Name", "Date")
    sort_dropdown.grid(row=2, column=3, padx=10, pady=(10, 5), sticky="e")

    square1 = tk.Frame(main_content_frame, bg="white", width=100, height=100)
    square1.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

    square2 = tk.Frame(main_content_frame, bg="white", width=100, height=100)
    square2.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

    square3 = tk.Frame(main_content_frame, bg="white", width=100, height=100)
    square3.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

    main_content_frame.grid_columnconfigure(0, weight=1)
    main_content_frame.grid_columnconfigure(1, weight=1)
    main_content_frame.grid_columnconfigure(2, weight=1)
    main_content_frame.grid_columnconfigure(3, weight=0)

    style = ttk.Style()
    style.configure("Sidebar.TButton", background=bg_color, foreground=text_color)
    style.configure("Main.TButton", background=button_bg_color, foreground=text_color)

def show_login_page():
    global content_frame
    content_frame = create_main_frame()
    main_frame = tk.Frame(content_frame)
    main_frame.pack(expand=True, fill="both")
    left_frame = tk.Frame(main_frame, bg="white")
    left_frame.pack(side="right", expand=True, fill="both")
    right_frame = tk.Frame(main_frame, bg=bg_color, padx=20, pady=20)
    right_frame.pack(side="left", expand=True, fill="both")
    title_label = tk.Label(right_frame, text="Login", font=("Arial", 30, "bold"), bg=bg_color, fg=button_bg_color)
    title_label.pack(pady=20)

    style = ttk.Style()
    style.configure('White.TButton', background="white", foreground='black')

    username_label = tk.Label(right_frame, text="Username", bg=bg_color, fg=text_color)
    username_label.pack()
    username_entry = ttk.Entry(right_frame, width=32)
    username_entry.pack(pady=5)

    password_label = tk.Label(right_frame, text="Password", bg=bg_color, fg=text_color)
    password_label.pack()
    password_frame = tk.Frame(right_frame, bg=bg_color)
    password_frame.pack(pady=5)
    password_entry = ttk.Entry(password_frame, show="•", width=24)
    password_entry.pack(side="left")

    def toggle_password():
        if password_entry.cget('show') == '':
            password_entry.config(show='•')
            show_hide_button.config(text='Show')
        else:
            password_entry.config(show='')
            show_hide_button.config(text='Hide')

    show_hide_button = ttk.Button(password_frame, text='Show',command=toggle_password,  width=6, style='White.TButton')
    show_hide_button.pack(side="left")

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
                    if role == "Admin":
                        show_main_interface(real_name)
                    elif role == "Student":
                        show_student_dashboard()
                    else:
                        show_teacher_dashboard(real_name)
                else:
                    messagebox.showerror("Login Error", "Invalid username or password")
            else:
                messagebox.showerror("Database Error", "Unable to connect to the database.")
        else:
            messagebox.showerror("Login Error", "Please enter username, password, and select a role.")

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
