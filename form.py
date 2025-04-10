import tkinter as tk

def create_registration_form():
    # Create the main window
    root = tk.Tk()
    root.title("User Registration")

    # Create a vertical frame
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Add labels and entry fields
    tk.Label(frame, text="First Name:").pack(anchor="w", pady=5)
    entry_first_name = tk.Entry(frame)
    entry_first_name.pack(fill="x", pady=5)

    tk.Label(frame, text="Last Name:").pack(anchor="w", pady=5)
    entry_last_name = tk.Entry(frame)
    entry_last_name.pack(fill="x", pady=5)

    tk.Label(frame, text="Email:").pack(anchor="w", pady=5)
    entry_email = tk.Entry(frame)
    entry_email.pack(fill="x", pady=5)

    tk.Label(frame, text="Password:").pack(anchor="w", pady=5)
    entry_password = tk.Entry(frame, show="*")
    entry_password.pack(fill="x", pady=5)

    # Add a submit button
    submit_button = tk.Button(frame, text="Submit")
    submit_button.pack(pady=10)

    # Run the GUI event loop
    root.mainloop()

# Run the registration form
create_registration_form()
