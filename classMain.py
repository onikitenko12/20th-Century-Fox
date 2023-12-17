import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("20th Century Fox Presents")
        self.iconbitmap('icon.ico')
        self.width = 800
        self.height = 600
        self.geometry(f"{self.width}x{self.height}")
        self.center_window()

        # Add lines
        canvas = tk.Canvas(self, height=1, bg="black")
        canvas.grid(row=0, column=0, columnspan=4, pady=5, sticky="we")
        canvas = tk.Canvas(self, height=1, bg="black")
        canvas.grid(row=6, column=0, columnspan=4, pady=20, sticky="we")
        canvas = tk.Canvas(self, height=1, bg="black")
        canvas.grid(row=9, column=0, columnspan=4, pady=20, sticky="we")

        # Add labels
        label = tk.Label(self, text="  Address Book Management:  ", font=("Helvetica", 12))
        label.grid(row=0, column=0, columnspan=4, pady=10)
        label = tk.Label(self, text="  Notes Management:  ", font=("Helvetica", 12))
        label.grid(row=6, column=0, columnspan=4, pady=10)
        label = tk.Label(self, text="  Other Actions:  ", font=("Helvetica", 12))
        label.grid(row=9, column=0, columnspan=4, pady=10)

        # Add buttons
        self.add_buttons()

    def center_window(self):        
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def add_buttons(self):
        PADX = 40
        PADY = 5
        WIDTH = 16
        HEIGHT = 2

        # For Contacts 1:
        btn_add_contact = tk.Button(self, text="Add contact", command=self.show_add_contact_window, width=WIDTH, height=HEIGHT)
        btn_add_phone = tk.Button(self, text="Add phone", command=self.show_add_phone_window, width=WIDTH, height=HEIGHT)
        btn_add_email = tk.Button(self, text="Add email", command=self.show_add_email_window, width=WIDTH, height=HEIGHT)
        btn_add_address = tk.Button(self, text="Add address", command=self.show_add_address_window, width=WIDTH, height=HEIGHT)
        btn_add_birthday = tk.Button(self, text="Add birthday", command=self.show_add_birthday_window, width=WIDTH, height=HEIGHT)

        btn_add_contact.grid(row=1, column=0, sticky="w", padx=PADX, pady=PADY)
        btn_add_phone.grid(row=2, column=0, sticky="w", padx=PADX, pady=PADY)
        btn_add_email.grid(row=3, column=0, sticky="w", padx=PADX, pady=PADY)
        btn_add_address.grid(row=4, column=0, sticky="w", padx=PADX, pady=PADY)
        btn_add_birthday.grid(row=5, column=0, sticky="w", padx=PADX, pady=PADY)

        # For Contacts 2:
        btn_search_contact = tk.Button(self, text="Search contact", command=self.show_search_contact_window, width=WIDTH, height=HEIGHT)
        btn_search_phone = tk.Button(self, text="Search phone", command=self.search_phone, width=WIDTH, height=HEIGHT)
        btn_search_email = tk.Button(self, text="Search email", command=self.search_email, width=WIDTH, height=HEIGHT)
        btn_search_address = tk.Button(self, text="Search address", command=self.search_address, width=WIDTH, height=HEIGHT)
        btn_search_birthday = tk.Button(self, text="Search birthday", command=self.search_birthday, width=WIDTH, height=HEIGHT)

        btn_search_contact.grid(row=1, column=1, sticky="e", padx=PADX, pady=PADY)
        btn_search_phone.grid(row=2, column=1, sticky="e", padx=PADX, pady=PADY)
        btn_search_email.grid(row=3, column=1, sticky="e", padx=PADX, pady=PADY)
        btn_search_address.grid(row=4, column=1, sticky="e", padx=PADX, pady=PADY)
        btn_search_birthday.grid(row=5, column=1, sticky="e", padx=PADX, pady=PADY)

        # For Contacts 3:
        btn_change_contact = tk.Button(self, text="Change contact", command=self.change_contact, width=WIDTH, height=HEIGHT)
        btn_change_phone = tk.Button(self, text="Change phone", command=self.change_phone, width=WIDTH, height=HEIGHT)
        btn_change_email = tk.Button(self, text="Change email", command=self.change_email, width=WIDTH, height=HEIGHT)
        btn_change_address = tk.Button(self, text="Change address", command=self.change_address, width=WIDTH, height=HEIGHT)
        btn_change_birthday = tk.Button(self, text="Change birthday", command=self.change_birthday, width=WIDTH, height=HEIGHT)

        btn_change_contact.grid(row=1, column=2, sticky="e", padx=PADX, pady=PADY)
        btn_change_phone.grid(row=2, column=2, sticky="e", padx=PADX, pady=PADY)
        btn_change_email.grid(row=3, column=2, sticky="e", padx=PADX, pady=PADY)
        btn_change_address.grid(row=4, column=2, sticky="e", padx=PADX, pady=PADY)
        btn_change_birthday.grid(row=5, column=2, sticky="e", padx=PADX, pady=PADY)

        # For Contacts 4:
        btn_delete_contact = tk.Button(self, text="Delete contact", command=self.delete_contact, width=WIDTH, height=HEIGHT)
        btn_delete_phone = tk.Button(self, text="Delete phone", command=self.delete_phone, width=WIDTH, height=HEIGHT)
        btn_delete_email = tk.Button(self, text="Delete email", command=self.delete_email, width=WIDTH, height=HEIGHT)
        btn_delete_address = tk.Button(self, text="Delete address", command=self.delete_address, width=WIDTH, height=HEIGHT)
        btn_delete_birthday = tk.Button(self, text="Delete birthday", command=self.delete_birthday, width=WIDTH, height=HEIGHT)

        btn_delete_contact.grid(row=1, column=3, sticky="e", padx=PADX, pady=PADY)
        btn_delete_phone.grid(row=2, column=3, sticky="e", padx=PADX, pady=PADY)
        btn_delete_email.grid(row=3, column=3, sticky="e", padx=PADX, pady=PADY)
        btn_delete_address.grid(row=4, column=3, sticky="e", padx=PADX, pady=PADY)
        btn_delete_birthday.grid(row=5, column=3, sticky="e", padx=PADX, pady=PADY)

        # For Notes 1:
        btn_add_note = tk.Button(self, text="Add note", command=self.add_note, width=WIDTH, height=HEIGHT)
        btn_add_tag = tk.Button(self, text="Add tag", command=self.add_tag, width=WIDTH, height=HEIGHT)

        btn_add_note.grid(row=7, column=0, sticky="w", padx=PADX, pady=PADY)
        btn_add_tag.grid(row=8, column=0, sticky="w", padx=PADX, pady=PADY)

        # For Notes 2:
        btn_search_note = tk.Button(self, text="Search note", command=self.search_note, width=WIDTH, height=HEIGHT)
        btn_search_tag = tk.Button(self, text="Search tag", command=self.search_tag, width=WIDTH, height=HEIGHT)

        btn_search_note.grid(row=7, column=1, sticky="e", padx=PADX, pady=PADY)
        btn_search_tag.grid(row=8, column=1, sticky="e", padx=PADX, pady=PADY)

        # For Notes 3:
        btn_change_note = tk.Button(self, text="Change note", command=self.change_note, width=WIDTH, height=HEIGHT)
        btn_change_tag = tk.Button(self, text="Change tag", command=self.change_tag, width=WIDTH, height=HEIGHT)

        btn_change_note.grid(row=7, column=2, sticky="e", padx=PADX, pady=PADY)
        btn_change_tag.grid(row=8, column=2, sticky="e", padx=PADX, pady=PADY)

        # For Notes 4:
        btn_delete_note = tk.Button(self, text="Delete note", command=self.delete_note, width=WIDTH, height=HEIGHT)
        btn_delete_tag = tk.Button(self, text="Delete tag", command=self.delete_tag, width=WIDTH, height=HEIGHT)

        btn_delete_note.grid(row=7, column=3, sticky="e", padx=PADX, pady=PADY)
        btn_delete_tag.grid(row=8, column=3, sticky="e", padx=PADX, pady=PADY)

        # For Sorting Files:
        btn_sorting_files = tk.Button(self, text="Sorting files", command=self.sorting_files, width=WIDTH, height=HEIGHT)

        btn_sorting_files.grid(row=10, column=0, sticky="w", padx=PADX, pady=PADY)


    def show_add_contact_window(self):
        add_contact_window = AddContactWindow(self)
        add_contact_window.center_window()
        # messagebox.showinfo("Action", "Adding contact")

    def show_add_phone_window(self):
        add_phone_window = AddPhoneWindow(self)
        add_phone_window.center_window()
        # messagebox.showinfo("Action", "Adding phone")

    def show_add_email_window(self):
        add_email_window = AddEmailWindow(self)
        add_email_window.center_window()
        # messagebox.showinfo("Action", "Adding email")

    def show_add_address_window(self):
        add_address_window = AddAddressWindow(self)
        add_address_window.center_window()
        # messagebox.showinfo("Action", "Adding address")

    def show_add_birthday_window(self):
        add_birthday_window = AddBirthdayWindow(self)
        add_birthday_window.center_window()
        # messagebox.showinfo("Action", "Adding birthday")


    def show_search_contact_window(self):
        search_contact_window = SearchContactWindow(self)
        search_contact_window.center_window()
        # messagebox.showinfo("Action", "Search contact")

    def search_phone(self):
        messagebox.showinfo("Action", "Search phone")

    def search_email(self):
        messagebox.showinfo("Action", "Search email")

    def search_address(self):
        messagebox.showinfo("Action", "Search address")

    def search_birthday(self):
        messagebox.showinfo("Action", "Search birthday")


    def change_contact(self):
        messagebox.showinfo("Action", "Change contact")

    def change_phone(self):
        messagebox.showinfo("Action", "Change phone")

    def change_email(self):
        messagebox.showinfo("Action", "Change email")

    def change_address(self):
        messagebox.showinfo("Action", "Change address")

    def change_birthday(self):
        messagebox.showinfo("Action", "Change birthday")


    def delete_contact(self):
        messagebox.showinfo("Action", "Delete contact")

    def delete_phone(self):
        messagebox.showinfo("Action", "Delete phone")

    def delete_email(self):
        messagebox.showinfo("Action", "Delete email")

    def delete_address(self):
        messagebox.showinfo("Action", "Delete address")

    def delete_birthday(self):
        messagebox.showinfo("Action", "Delete birthday")


    def add_note(self):
        messagebox.showinfo("Action", "Add note")

    def add_tag(self):
        messagebox.showinfo("Action", "Add tag")


    def search_note(self):
        messagebox.showinfo("Action", "Search note")

    def search_tag(self):
        messagebox.showinfo("Action", "Search tag")


    def change_note(self):
        messagebox.showinfo("Action", "Change note")

    def change_tag(self):
        messagebox.showinfo("Action", "Change tag")


    def delete_note(self):
        messagebox.showinfo("Action", "Delete note")

    def delete_tag(self):
        messagebox.showinfo("Action", "Delete tag")


    def sorting_files(self):
        messagebox.showinfo("Action", "Sorting files")



class AddContactWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Add Contact")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.date_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        phone_label = tk.Label(self, text="Phone:")
        phone_entry = tk.Entry(self, width=30, textvariable=self.phone_var)

        email_label = tk.Label(self, text="Email:")
        email_entry = tk.Entry(self, width=30, textvariable=self.email_var)

        address_label = tk.Label(self, text="Address:")
        address_entry = tk.Entry(self, width=30, textvariable=self.address_var)

        # Date entry field
        date_label = tk.Label(self, text="Birthday:")
        date_entry = tk.Entry(self, width=30, textvariable=self.date_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        phone_entry.grid(row=1, column=1, padx=10, pady=5)

        email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        email_entry.grid(row=2, column=1, padx=10, pady=5)

        address_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        address_entry.grid(row=3, column=1, padx=10, pady=5)

        date_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        date_entry.grid(row=4, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.save_contact, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=5, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=5, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def save_contact(self):
        user = self.user_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()
        date = self.date_var.get()

        # <--  Сюди логіку збереження контатку
        
        messagebox.showinfo("Contact Information", f"User: {user}\nPhone: {phone}\nEmail: {email}\nAddress: {address}\nBirthday: {date}")
        self.destroy()



class AddPhoneWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Add Phone")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.phone_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        phone_label = tk.Label(self, text="Phone:")
        phone_entry = tk.Entry(self, width=30, textvariable=self.phone_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        phone_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.save_phone, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=3, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=3, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def save_phone(self):
        user = self.user_var.get()
        phone = self.phone_var.get()

        # <--  Сюди логіку збереження телефону
        
        messagebox.showinfo("Contact Information", f"User: {user}\nPhone: {phone}\n")
        self.destroy()



class AddEmailWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Add Email")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.email_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        email_label = tk.Label(self, text="Email:")
        email_entry = tk.Entry(self, width=30, textvariable=self.email_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        email_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        email_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.save_email, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=2, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=2, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def save_email(self):
        user = self.user_var.get()
        email = self.email_var.get()

        # <--  Сюди логіку збереження Email
        
        messagebox.showinfo("Contact Information", f"User: {user}\nEmail: {email}\n")
        self.destroy()



class AddAddressWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Add Address")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.address_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        address_label = tk.Label(self, text="Address:")
        address_entry = tk.Entry(self, width=30, textvariable=self.address_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        address_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        address_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.save_address, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=2, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=2, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def save_address(self):
        user = self.user_var.get()
        address = self.address_var.get()

        # <--  Сюди логіку збереження адреси
        
        messagebox.showinfo("Contact Information", f"User: {user}\nAddress: {address}\n")
        self.destroy()



class AddBirthdayWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Add Birthday")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.date_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        # Date entry field
        date_label = tk.Label(self, text="Birthday:")
        date_entry = tk.Entry(self, width=30, textvariable=self.date_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        date_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        date_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.save_birthday, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=2, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=2, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def save_birthday(self):
        user = self.user_var.get()
        date = self.date_var.get()

        # <--  Сюди логіку збереження дати народження
        
        messagebox.showinfo("Contact Information", f"User: {user}\nBirthday: {date}")
        self.destroy()




class SearchContactWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Search Contact")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.date_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        phone_label = tk.Label(self, text="Phone:")
        phone_entry = tk.Entry(self, width=30, textvariable=self.phone_var)

        email_label = tk.Label(self, text="Email:")
        email_entry = tk.Entry(self, width=30, textvariable=self.email_var)

        address_label = tk.Label(self, text="Address:")
        address_entry = tk.Entry(self, width=30, textvariable=self.address_var)

        # Date entry field
        date_label = tk.Label(self, text="Birthday:")
        date_entry = tk.Entry(self, width=30, textvariable=self.date_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        phone_entry.grid(row=1, column=1, padx=10, pady=5)

        email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        email_entry.grid(row=2, column=1, padx=10, pady=5)

        address_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        address_entry.grid(row=3, column=1, padx=10, pady=5)

        date_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        date_entry.grid(row=4, column=1, padx=10, pady=5)

        # Buttons "Search" and "Cancel"
        save_button = tk.Button(self, text="Search", command=self.show_contact_table, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=5, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=5, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def show_contact_table(self):
        user = self.user_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()
        date = self.date_var.get()

        # <--  Сюди логіку виведення інформації про контакт
        
        contact_data = {
            "user": user,
            "phones": ["123456789", "987654321"],
            "emails": ["user@example.com"],
            "address": "123 Main St",
            "birthday": "01/01/2000"
        }

        ContactTableWindow(self, contact_data)

class ContactTableWindow(tk.Toplevel):
    def __init__(self, search_contact_window, contact_data, *args, **kwargs):
        tk.Toplevel.__init__(self, search_contact_window, *args, **kwargs)
        self.title("Contact Information")
        self.iconbitmap('icon.ico')
        self.width = 950
        self.height = 300
        self.geometry(f"{self.width}x{self.height}")
        self.center_window()

        columns_info = {
            "user": {"text": "User", "width": 150},
            "phones": {"text": "Phones", "width": 200},
            "emails": {"text": "Emails", "width": 200},
            "address": {"text": "Address", "width": 200},
            "birthday": {"text": "Birthday", "width": 150}
        }

        tree = ttk.Treeview(self, columns=list(columns_info.keys()), show="headings")

        for col, info in columns_info.items():
            tree.heading(col, text=info["text"])
            tree.column(col, width=info["width"])

        # Adding data to the table
        tree.insert("", "end", values=(contact_data["user"], ", ".join(contact_data["phones"]),
                                       ", ".join(contact_data["emails"]), contact_data["address"],
                                       contact_data["birthday"]))

        tree.pack(padx=10, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')





if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()