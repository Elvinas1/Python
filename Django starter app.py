import os
import tkinter as tk
from tkinter import messagebox

def create_project():
    project_path = entry_path.get()
    project_name = entry_name.get()

    # Check if the project directory already exists
    if os.path.isdir(f"{project_path}/{project_name}"):
        messagebox.showerror("Error", "Project directory already exists!")
        return

    # Create the project directory
    os.makedirs(f"{project_path}/{project_name}")
    os.chdir(f"{project_path}/{project_name}")

    # Create a virtual environment and activate it
    os.system(f"python3 -m venv venv && source venv/bin/activate")

    # Install Django
    os.system("pip install django")

    # Create a new Django project
    os.system(f"django-admin startproject {project_name}")

    # Create a new Django app
    app_name = entry_app.get()
    os.chdir(project_name)
    os.system(f"source venv/bin/activate && python manage.py startapp {app_name}")

    # Set the correct permissions on the project directory
    os.system(f"sudo chmod -R 777 {project_name}")

    messagebox.showinfo("Success", "Django project created successfully!")

# Create the GUI
window = tk.Tk()
window.title("Django Project Creator")

# Create the widgets
label_path = tk.Label(text="Project path:")
entry_path = tk.Entry(width=50)
label_name = tk.Label(text="Project name:")
entry_name = tk.Entry(width=50)
label_app = tk.Label(text="App name:")
entry_app = tk.Entry(width=50)
button_create = tk.Button(text="Create project", command=create_project)

# Bind the <Return> event to the create_project function
window.bind('<Return>', lambda event=None: button_create.invoke())

# Layout the widgets
label_path.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_path.grid(row=0, column=1, padx=5, pady=5)
label_name.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_name.grid(row=1, column=1, padx=5, pady=5)
label_app.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
entry_app.grid(row=2, column=1, padx=5, pady=5)
button_create.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the GUI
window.mainloop()
