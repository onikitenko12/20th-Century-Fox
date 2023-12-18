import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src import sorter


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

        # For "Add" Contacts. Group 1:
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

        # For "Search" Contacts. Group 2:
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

        # For "Change" Contacts. Group 3:
        btn_change_contact = tk.Button(self, text="Change contact", command=self.show_change_contact_window, width=WIDTH, height=HEIGHT)
        btn_change_phone = tk.Button(self, text="Change phone", command=self.show_change_phone_window, width=WIDTH, height=HEIGHT)
        btn_change_email = tk.Button(self, text="Change email", command=self.show_change_email_window, width=WIDTH, height=HEIGHT)
        btn_change_address = tk.Button(self, text="Change address", command=self.show_change_address_window, width=WIDTH, height=HEIGHT)
        btn_change_birthday = tk.Button(self, text="Change birthday", command=self.show_change_birthday_window, width=WIDTH, height=HEIGHT)

        btn_change_contact.grid(row=1, column=2, sticky="e", padx=PADX, pady=PADY)
        btn_change_phone.grid(row=2, column=2, sticky="e", padx=PADX, pady=PADY)
        btn_change_email.grid(row=3, column=2, sticky="e", padx=PADX, pady=PADY)
        btn_change_address.grid(row=4, column=2, sticky="e", padx=PADX, pady=PADY)
        btn_change_birthday.grid(row=5, column=2, sticky="e", padx=PADX, pady=PADY)

        # For "Delete" Contacts. Group 4:
        btn_delete_contact = tk.Button(self, text="Delete contact", command=self.show_delete_contact_window, width=WIDTH, height=HEIGHT)
        btn_delete_phone = tk.Button(self, text="Delete phone", command=self.show_delete_phone_window, width=WIDTH, height=HEIGHT)
        btn_delete_email = tk.Button(self, text="Delete email", command=self.show_delete_email_window, width=WIDTH, height=HEIGHT)
        btn_delete_address = tk.Button(self, text="Delete address", command=self.show_delete_address_window, width=WIDTH, height=HEIGHT)
        btn_delete_birthday = tk.Button(self, text="Delete birthday", command=self.show_delete_birthday_window, width=WIDTH, height=HEIGHT)

        btn_delete_contact.grid(row=1, column=3, sticky="e", padx=PADX, pady=PADY)
        btn_delete_phone.grid(row=2, column=3, sticky="e", padx=PADX, pady=PADY)
        btn_delete_email.grid(row=3, column=3, sticky="e", padx=PADX, pady=PADY)
        btn_delete_address.grid(row=4, column=3, sticky="e", padx=PADX, pady=PADY)
        btn_delete_birthday.grid(row=5, column=3, sticky="e", padx=PADX, pady=PADY)

        # For "Add" Notes. Group 1:
        btn_add_note = tk.Button(self, text="Add note", command=self.show_add_note_window, width=WIDTH, height=HEIGHT)
        btn_add_tag = tk.Button(self, text="Add tag", command=self.show_add_tag_window, width=WIDTH, height=HEIGHT)

        btn_add_note.grid(row=7, column=0, sticky="w", padx=PADX, pady=PADY)
        btn_add_tag.grid(row=8, column=0, sticky="w", padx=PADX, pady=PADY)

        # For "Search" Notes. Group 2:
        btn_search_note = tk.Button(self, text="Search note", command=self.show_search_note_window, width=WIDTH, height=HEIGHT)
        btn_search_tag = tk.Button(self, text="Search tag", command=self.show_search_tag_window, width=WIDTH, height=HEIGHT)

        btn_search_note.grid(row=7, column=1, sticky="e", padx=PADX, pady=PADY)
        btn_search_tag.grid(row=8, column=1, sticky="e", padx=PADX, pady=PADY)

        # For "Change" Notes. Group 3:
        btn_change_note = tk.Button(self, text="Change note", command=self.show_change_note_window, width=WIDTH, height=HEIGHT)
        btn_change_tag = tk.Button(self, text="Change tag", command=self.show_change_tag_window, width=WIDTH, height=HEIGHT)

        btn_change_note.grid(row=7, column=2, sticky="e", padx=PADX, pady=PADY)
        btn_change_tag.grid(row=8, column=2, sticky="e", padx=PADX, pady=PADY)

        # For "Delete" Notes. Group 4:
        btn_delete_note = tk.Button(self, text="Delete note", command=self.show_delete_note_window, width=WIDTH, height=HEIGHT)
        btn_delete_tag = tk.Button(self, text="Delete tag", command=self.show_delete_tag_window, width=WIDTH, height=HEIGHT)

        btn_delete_note.grid(row=7, column=3, sticky="e", padx=PADX, pady=PADY)
        btn_delete_tag.grid(row=8, column=3, sticky="e", padx=PADX, pady=PADY)

        # For Other. "Sorting Files":
        btn_sorting_files = tk.Button(self, text="Sorting files", command=self.show_sorting_files_window, width=WIDTH, height=HEIGHT)

        btn_sorting_files.grid(row=10, column=0, sticky="w", padx=PADX, pady=PADY)


    # "Add contact"
    def show_add_contact_window(self):
        add_contact_window = AddContactWindow(self)
        add_contact_window.center_window()

    # "Add phone"
    def show_add_phone_window(self):
        add_phone_window = AddPhoneWindow(self)
        add_phone_window.center_window()

    # "Add email"
    def show_add_email_window(self):
        add_email_window = AddEmailWindow(self)
        add_email_window.center_window()

    # "Add address"
    def show_add_address_window(self):
        add_address_window = AddAddressWindow(self)
        add_address_window.center_window()

    # "Add birthday"
    def show_add_birthday_window(self):
        add_birthday_window = AddBirthdayWindow(self)
        add_birthday_window.center_window()


    # "Search contact"
    def show_search_contact_window(self):
        search_contact_window = SearchContactWindow(self)
        search_contact_window.center_window()

    # "Search phone" - It is unclear whether it is necessary???
    def search_phone(self):
        messagebox.showinfo("Action", "Search phone")

    # "Search email" - It is unclear whether it is necessary???
    def search_email(self):
        messagebox.showinfo("Action", "Search email")

    # "Search address" - It is unclear whether it is necessary???
    def search_address(self):
        messagebox.showinfo("Action", "Search address")

    # "Search birthday" - It is unclear whether it is necessary???
    def search_birthday(self):
        messagebox.showinfo("Action", "Search birthday")


    # "Change contact"
    def show_change_contact_window(self):
        change_contact_window = ChangeContactWindow(self)
        change_contact_window.center_window()

    # "Change phone"
    def show_change_phone_window(self):
        change_phone_window = ChangePhoneWindow(self)
        change_phone_window.center_window()

    # "Change email"
    def show_change_email_window(self):
        change_email_window = ChangeEmailWindow(self)
        change_email_window.center_window()

    # "Change address"
    def show_change_address_window(self):
        change_address_window = ChangeAddressWindow(self)
        change_address_window.center_window()

    "Change birthday"
    def show_change_birthday_window(self):
        change_birthday_window = ChangeBirthdayWindow(self)
        change_birthday_window.center_window()


    # "Delete contact"
    def show_delete_contact_window(self):
        delete_contact_window = DeleteContactWindow(self)
        delete_contact_window.center_window()

    # "Delete phone"
    def show_delete_phone_window(self):
        delete_phone_window = DeletePhoneWindow(self)
        delete_phone_window.center_window()

    # "Delete email"
    def show_delete_email_window(self):
        delete_email_window = DeleteEmailWindow(self)
        delete_email_window.center_window()

    # "Delete address"
    def show_delete_address_window(self):
        delete_address_window = DeleteAddressWindow(self)
        delete_address_window.center_window()

    # "Delete birthday"
    def show_delete_birthday_window(self):
        delete_birthday_window = DeleteBirthdayWindow(self)
        delete_birthday_window.center_window()


    # "Add note"
    def show_add_note_window(self):
        add_note_window = AddNoteWindow(self)
        add_note_window.center_window()

    # "Add tag"
    def show_add_tag_window(self):
        add_tag_window = AddTagWindow(self)
        add_tag_window.center_window()


    # "Search note"
    def show_search_note_window(self):
        search_note_window = SearchNoteWindow(self)
        search_note_window.center_window()

    # "Search tag"
    def show_search_tag_window(self):
        search_tag_window = SearchTagWindow(self)
        search_tag_window.center_window()


    # "Change note"
    def show_change_note_window(self):
        change_note_window = ChangeNoteWindow(self)
        change_note_window.center_window()

    # "Change tag"
    def show_change_tag_window(self):
        change_tag_window = ChangeTagWindow(self)
        change_tag_window.center_window()


    # "Delete note"
    def show_delete_note_window(self):
        delete_note_window = DeleteNoteWindow(self)
        delete_note_window.center_window()

    # "Delete tag"
    def show_delete_tag_window(self):
        delete_tag_window = DeleteTagWindow(self)
        delete_tag_window.center_window()


    # Other - "Sorting files"
    def show_sorting_files_window(self):
        sorting_files_window = SortingFilesWindow(self)
        sorting_files_window.center_window()



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

        # <--  Here, the logic for "Add Contact"
        
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

        # <--  Here, the logic for "Add Phone"
        
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

        # <--  Here, the logic for "Add Email"
        
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

        # <--  Here, the logic for "Add Address"
        
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

        # <--  Here, the logic for "Add Birthday"
        
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

        # <--  Here, the logic for "Search Contact"
        
        contact_data = {
            "user": user,
            "phones": ["123456789", "987654321"],
            "emails": ["user@example.com"],
            "address": "123 Main St",
            "birthday": "01/01/2000"
        }

        ContactTableWindow(self, contact_data)



class ChangeContactWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Change Contact")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.new_user_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        new_user_label = tk.Label(self, text="New User Name:")
        new_user_entry = tk.Entry(self, width=30, textvariable=self.new_user_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        new_user_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        new_user_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.change_contact, width=10, height=1)
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

    def change_contact(self):
        user = self.user_var.get()
        new_user = self.new_user_var.get()

        # <--  Here, the logic for "Change Contact"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nNew User: {new_user}\n")
        self.destroy()


class ChangePhoneWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Change Phone")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.new_phone_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        phone_label = tk.Label(self, text="Phone:")
        phone_entry = tk.Entry(self, width=30, textvariable=self.phone_var)

        new_phone_label = tk.Label(self, text="New Phone:")
        new_phone_entry = tk.Entry(self, width=30, textvariable=self.new_phone_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        phone_entry.grid(row=1, column=1, padx=10, pady=5)

        new_phone_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        new_phone_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.change_phone, width=10, height=1)
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

    def change_phone(self):
        user = self.user_var.get()
        phone = self.phone_var.get()
        new_phone = self.new_phone_var.get()

        # <--  Here, the logic for "Change Phone"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nPhone: {phone}\nNew Phone: {new_phone}")
        self.destroy()


class ChangeEmailWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Change Email")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.new_email_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        email_label = tk.Label(self, text="Email:")
        email_entry = tk.Entry(self, width=30, textvariable=self.email_var)

        new_email_label = tk.Label(self, text="New Email:")
        new_email_entry = tk.Entry(self, width=30, textvariable=self.new_email_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        email_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        email_entry.grid(row=1, column=1, padx=10, pady=5)

        new_email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        new_email_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.change_email, width=10, height=1)
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

    def change_email(self):
        user = self.user_var.get()
        email = self.email_var.get()
        new_email = self.new_email_var.get()

        # <--  Here, the logic for "Change Email"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nEmail: {email}\nNew Email: {new_email}")
        self.destroy()



class ChangeAddressWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Change Address")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.address_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        address_label = tk.Label(self, text="New Address:")
        address_entry = tk.Entry(self, width=30, textvariable=self.address_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        address_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        address_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.change_address, width=10, height=1)
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

    def change_address(self):
        user = self.user_var.get()
        address = self.address_var.get()

        # <--  Here, the logic for "Change Address"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nNew Address: {address}")
        self.destroy()



class ChangeBirthdayWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Change Birthday")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.birthday_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        birthday_label = tk.Label(self, text="New Birthday:")
        birthday_entry = tk.Entry(self, width=30, textvariable=self.birthday_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        birthday_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        birthday_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.change_birthday, width=10, height=1)
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

    def change_birthday(self):
        user = self.user_var.get()
        birthday = self.birthday_var.get()

        # <--  Here, the logic for "Change Birthday"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nNew Birthday: {birthday}")
        self.destroy()



class DeleteContactWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Delete Contact")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="Delete User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.delete_contact, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=1, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=1, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def delete_contact(self):
        user = self.user_var.get()

        # <--  Here, the logic for "Delete Contact"
        
        messagebox.showinfo("Contact Information", f"Delete User: {user}")
        self.destroy()


class DeletePhoneWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Delete Phone")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.phone_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        phone_label = tk.Label(self, text="Delete Phone:")
        phone_entry = tk.Entry(self, width=30, textvariable=self.phone_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        phone_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.delete_phone, width=10, height=1)
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

    def delete_phone(self):
        user = self.user_var.get()
        phone = self.phone_var.get()

        # <--  Here, the logic for "Delete Phone"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nDelete Phone: {phone}")
        self.destroy()


class DeleteEmailWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Delete Email")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.email_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        email_label = tk.Label(self, text="Delete Email:")
        email_entry = tk.Entry(self, width=30, textvariable=self.email_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        email_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        email_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.delete_email, width=10, height=1)
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

    def delete_email(self):
        user = self.user_var.get()
        email = self.email_var.get()

        # <--  Here, the logic for "Delete Email"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nDelete Email: {email}")
        self.destroy()


class DeleteAddressWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Delete Address")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.delete_address, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=1, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=1, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def delete_address(self):
        user = self.user_var.get()

        # <--  Here, the logic for "Delete Address"
        
        messagebox.showinfo("Contact Information", f"For User: {user} Address deleted\n")
        self.destroy()


class DeleteBirthdayWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Delete Birthday")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.delete_birthday, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=1, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=1, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def delete_birthday(self):
        user = self.user_var.get()

        # <--  Here, the logic for "Delete Birthday"
        
        messagebox.showinfo("Contact Information", f"For User: {user} Birthday deleted\n")
        self.destroy()


# --- For Nones ---

class AddNoteWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Add Note")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.note_var = tk.StringVar()
        self.tag_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        note_label = tk.Label(self, text="Note:")
        note_entry = tk.Entry(self, width=30, textvariable=self.note_var)

        tag_label = tk.Label(self, text="Tag:")
        tag_entry = tk.Entry(self, width=30, textvariable=self.tag_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        note_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        note_entry.grid(row=1, column=1, padx=10, pady=5)

        tag_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tag_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.add_note, width=10, height=1)
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

    def add_note(self):
        user = self.user_var.get()
        note = self.note_var.get()
        tag = self.tag_var.get()

        # <--  Here, the logic for "Add Note"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nNote: {note}\nTag: {tag}")
        self.destroy()


class AddTagWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Add Note")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.tag_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        tag_label = tk.Label(self, text="Tag:")
        tag_entry = tk.Entry(self, width=30, textvariable=self.tag_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        tag_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tag_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.add_tag, width=10, height=1)
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

    def add_tag(self):
        user = self.user_var.get()
        tag = self.tag_var.get()

        # <--  Here, the logic for "Add Tag"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nTag: {tag}")
        self.destroy()



class SearchNoteWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Search Note")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        # Buttons "Search" and "Cancel"
        save_button = tk.Button(self, text="Search", command=self.show_note_table, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=1, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=1, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def show_note_table(self):
        user = self.user_var.get()

        # <--  Here, the logic for "Search Note"
        
        note_data = {
            "user": user,
            "note": "Lorem ipsum, Lorem ipsum, Lorem ipsum, Lorem ipsum",
            "tags": ["tag1", "tag2"],
        }

        NoteTableWindow(self, note_data)


class SearchTagWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Search Tag")
        self.iconbitmap('icon.ico')

        self.tag_var = tk.StringVar()

        # Text input fields
        tag_label = tk.Label(self, text="Tag:")
        tag_entry = tk.Entry(self, width=30, textvariable=self.tag_var)

        # Placing widgets on a window
        tag_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tag_entry.grid(row=0, column=1, padx=10, pady=5)

        # Buttons "Search" and "Cancel"
        save_button = tk.Button(self, text="Search", command=self.show_tag_table, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=1, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=1, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def show_tag_table(self):
        tag = self.tag_var.get()

        # <--  Here, the logic for "Search Tag"
        
        note_data = {
            "user": "user",
            "note": "Lorem ipsum, Lorem ipsum, Lorem ipsum, Lorem ipsum",
            "tags": [tag, "tag1", "tag2"],
        }

        NoteTableWindow(self, note_data)


class ChangeNoteWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Change Note")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.new_note_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        new_note_label = tk.Label(self, text="New Note:")
        new_note_entry = tk.Entry(self, width=30, textvariable=self.new_note_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        new_note_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        new_note_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.change_note, width=10, height=1)
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

    def change_note(self):
        user = self.user_var.get()
        new_note = self.new_note_var.get()

        # <--  Here, the logic for "Change Note"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nNew Note: {new_note}")
        self.destroy()


class ChangeTagWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Change Tag")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.tag_var = tk.StringVar()
        self.new_tag_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        tag_label = tk.Label(self, text="Tag:")
        tag_entry = tk.Entry(self, width=30, textvariable=self.tag_var)

        new_tag_label = tk.Label(self, text="New Tag:")
        new_tag_entry = tk.Entry(self, width=30, textvariable=self.new_tag_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        tag_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tag_entry.grid(row=1, column=1, padx=10, pady=5)

        new_tag_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        new_tag_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.change_tag, width=10, height=1)
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

    def change_tag(self):
        user = self.user_var.get()
        tag = self.tag_var.get()
        new_tag = self.new_tag_var.get()

        # <--  Here, the logic for "Change Tag"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nTag: {tag}\nNew Tag: {new_tag}")
        self.destroy()


class DeleteNoteWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Delete Note")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="Delete Note for User:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.delete_note, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=1, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=1, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def delete_note(self):
        user = self.user_var.get()

        # <--  Here, the logic for "Delete Note"
        
        messagebox.showinfo("Information", f"Delete Note for User: {user}")
        self.destroy()


class DeleteTagWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Delete Tag")
        self.iconbitmap('icon.ico')

        self.user_var = tk.StringVar()
        self.tag_var = tk.StringVar()

        # Text input fields
        user_label = tk.Label(self, text="User Name:")
        user_entry = tk.Entry(self, width=30, textvariable=self.user_var)

        tag_label = tk.Label(self, text="Delete Tag:")
        tag_entry = tk.Entry(self, width=30, textvariable=self.tag_var)

        # Placing widgets on a window
        user_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry.grid(row=0, column=1, padx=10, pady=5)

        tag_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tag_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.delete_tag, width=10, height=1)
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

    def delete_tag(self):
        user = self.user_var.get()
        tag = self.tag_var.get()

        # <--  Here, the logic for "Delete Tag"
        
        messagebox.showinfo("Contact Information", f"User: {user}\nDelete Tag: {tag}")
        self.destroy()


# --- For Other ---

class SortingFilesWindow(tk.Toplevel):
    def __init__(self, main_app, *args, **kwargs):
        tk.Toplevel.__init__(self, main_app, *args, **kwargs)

        self.title("Sorting Files")
        self.iconbitmap('icon.ico')

        self.path_var = tk.StringVar()

        # Text input fields
        path_label = tk.Label(self, text="Path for Sorting:")
        path_entry = tk.Entry(self, width=30, textvariable=self.path_var)

        # Placing widgets on a window
        path_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        path_entry.grid(row=0, column=1, padx=10, pady=5)

        # Buttons "Save" and "Cancel"
        save_button = tk.Button(self, text="Save", command=self.sorting_files, width=10, height=1)
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy, width=10, height=1)

        save_button.grid(row=1, column=0, sticky="e", padx=30, pady=10)
        cancel_button.grid(row=1, column=1, sticky="e", padx=30, pady=10)

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f'+{x}+{y}')

    def sorting_files(self):
        path_s = self.path_var.get()
        sorter.main(f'sort {path_s}')    
        # <--  Here, the logic for "Sorting Files"
        
        messagebox.showinfo("Information", f"Sorting files in a directory: {path_s}")
        self.destroy()



# --- For Show ---
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


class NoteTableWindow(tk.Toplevel):
    def __init__(self, search_note_window, note_data, *args, **kwargs):
        tk.Toplevel.__init__(self, search_note_window, *args, **kwargs)
        self.title("Note Information")
        self.iconbitmap('icon.ico')
        self.width = 750
        self.height = 300
        self.geometry(f"{self.width}x{self.height}")
        self.center_window()

        columns_info = {
            "user": {"text": "User", "width": 150},
            "note": {"text": "Notes", "width": 400},
            "tags": {"text": "Tags", "width": 200},
        }

        tree = ttk.Treeview(self, columns=list(columns_info.keys()), show="headings")

        for col, info in columns_info.items():
            tree.heading(col, text=info["text"])
            tree.column(col, width=info["width"])

        # Adding data to the table
        tree.insert("", "end", values=(note_data["user"], note_data["note"],
                                       ", ".join(note_data["tags"])))

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