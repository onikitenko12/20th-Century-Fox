import tkinter as tk
from tkinter import messagebox

def add_contact():
    messagebox.showinfo("Action", "Adding contact")

def add_phone():
    messagebox.showinfo("Action", "Adding phone")

def add_email():
    messagebox.showinfo("Action", "Adding email")

def add_address():
    messagebox.showinfo("Action", "Adding address")

def add_birthday():
    messagebox.showinfo("Action", "Adding birthday")


def search_contact():
    messagebox.showinfo("Action", "Search contact")

def search_phone():
    messagebox.showinfo("Action", "Search phone")

def search_email():
    messagebox.showinfo("Action", "Search email")

def search_address():
    messagebox.showinfo("Action", "Search address")

def search_birthday():
    messagebox.showinfo("Action", "Search birthday")


def change_contact():
    messagebox.showinfo("Action", "Change contact")

def change_phone():
    messagebox.showinfo("Action", "Change phone")

def change_email():
    messagebox.showinfo("Action", "Change email")

def change_address():
    messagebox.showinfo("Action", "Change address")

def change_birthday():
    messagebox.showinfo("Action", "Change birthday")


def delete_contact():
    messagebox.showinfo("Action", "Delete contact")

def delete_phone():
    messagebox.showinfo("Action", "Delete phone")

def delete_email():
    messagebox.showinfo("Action", "Delete email")

def delete_address():
    messagebox.showinfo("Action", "Delete address")

def delete_birthday():
    messagebox.showinfo("Action", "Delete birthday")


def add_note():
    messagebox.showinfo("Action", "Add note")

def add_tag():
    messagebox.showinfo("Action", "Add tag")


def search_note():
    messagebox.showinfo("Action", "Search note")

def search_tag():
    messagebox.showinfo("Action", "Search tag")


def change_note():
    messagebox.showinfo("Action", "Change note")

def change_tag():
    messagebox.showinfo("Action", "Change tag")


def delete_note():
    messagebox.showinfo("Action", "Delete note")

def delete_tag():
    messagebox.showinfo("Action", "Delete tag")


def sorting_files():
    messagebox.showinfo("Action", "Sorting files")


class CenteredWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("20th Century Fox Presents")
        self.width = 800
        self.height = 600

        self.center_window()
        self.iconbitmap('icon.ico')

        # Додавання горизонтальної лінії
        canvas = tk.Canvas(self, height=1, bg="black")
        canvas.grid(row=0, column=0, columnspan=4, pady=5, sticky="we")
        canvas = tk.Canvas(self, height=1, bg="black")
        canvas.grid(row=6, column=0, columnspan=4, pady=20, sticky="we")
        canvas = tk.Canvas(self, height=1, bg="black")
        canvas.grid(row=9, column=0, columnspan=4, pady=20, sticky="we")

        # Додавання мітки
        label = tk.Label(self, text="  Address Book Management:  ", font=("Helvetica", 12))
        label.grid(row=0, column=0, columnspan=4, pady=10)
        label = tk.Label(self, text="  Notes Management:  ", font=("Helvetica", 12))
        label.grid(row=6, column=0, columnspan=4, pady=10)
        label = tk.Label(self, text="  Other Actions:  ", font=("Helvetica", 12))
        label.grid(row=9, column=0, columnspan=4, pady=10)



# Notes Management
        

        # Додавання кнопок
        self.add_buttons()

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - self.width) // 2
        y = (screen_height - self.height) // 2

        self.geometry(f'{self.width}x{self.height}+{x}+{y}')

    def add_buttons(self):
        PADX = 40
        PADY = 5
        WIDTH = 16
        HEIGHT = 2
        # For Contacts 1:
        btn_add_contact = tk.Button(self, text="Add contact", command=add_contact, width=WIDTH, height=HEIGHT)
        btn_add_phone = tk.Button(self, text="Add phone", command=add_phone, width=WIDTH, height=HEIGHT)
        btn_add_email = tk.Button(self, text="Add email", command=add_email, width=WIDTH, height=HEIGHT)
        btn_add_address = tk.Button(self, text="Add address", command=add_address, width=WIDTH, height=HEIGHT)
        btn_add_birthday = tk.Button(self, text="Add birthday", command=add_birthday, width=WIDTH, height=HEIGHT)

        btn_add_contact.grid(row=1, column=0, sticky="w", padx=PADX, pady=PADY)
        btn_add_phone.grid(row=2, column=0, sticky="w", padx=PADX, pady=PADY)
        btn_add_email.grid(row=3, column=0, sticky="w", padx=PADX, pady=PADY)
        btn_add_address.grid(row=4, column=0, sticky="w", padx=PADX, pady=PADY)
        btn_add_birthday.grid(row=5, column=0, sticky="w", padx=PADX, pady=PADY)

        # For Contacts 2:
        btn_search_contact = tk.Button(self, text="Search contact", command=search_contact, width=WIDTH, height=HEIGHT)
        btn_search_phone = tk.Button(self, text="Search phone", command=search_phone, width=WIDTH, height=HEIGHT)
        btn_search_email = tk.Button(self, text="Search email", command=search_email, width=WIDTH, height=HEIGHT)
        btn_search_address = tk.Button(self, text="Search address", command=search_address, width=WIDTH, height=HEIGHT)
        btn_search_birthday = tk.Button(self, text="Search birthday", command=search_birthday, width=WIDTH, height=HEIGHT)

        btn_search_contact.grid(row=1, column=1, sticky="e", padx=PADX, pady=PADY)
        btn_search_phone.grid(row=2, column=1, sticky="e", padx=PADX, pady=PADY)
        btn_search_email.grid(row=3, column=1, sticky="e", padx=PADX, pady=PADY)
        btn_search_address.grid(row=4, column=1, sticky="e", padx=PADX, pady=PADY)
        btn_search_birthday.grid(row=5, column=1, sticky="e", padx=PADX, pady=PADY)

        # For Contacts 3:
        btn_change_contact = tk.Button(self, text="Change contact", command=change_contact, width=WIDTH, height=HEIGHT)
        btn_change_phone = tk.Button(self, text="Change phone", command=change_phone, width=WIDTH, height=HEIGHT)
        btn_change_email = tk.Button(self, text="Change email", command=change_email, width=WIDTH, height=HEIGHT)
        btn_change_address = tk.Button(self, text="Change address", command=change_address, width=WIDTH, height=HEIGHT)
        btn_change_birthday = tk.Button(self, text="Change birthday", command=change_birthday, width=WIDTH, height=HEIGHT)

        btn_change_contact.grid(row=1, column=2, sticky="e", padx=PADX, pady=PADY)
        btn_change_phone.grid(row=2, column=2, sticky="e", padx=PADX, pady=PADY)
        btn_change_email.grid(row=3, column=2, sticky="e", padx=PADX, pady=PADY)
        btn_change_address.grid(row=4, column=2, sticky="e", padx=PADX, pady=PADY)
        btn_change_birthday.grid(row=5, column=2, sticky="e", padx=PADX, pady=PADY)

        # For Contacts 4:
        btn_delete_contact = tk.Button(self, text="Delete contact", command=delete_contact, width=WIDTH, height=HEIGHT)
        btn_delete_phone = tk.Button(self, text="Delete phone", command=delete_phone, width=WIDTH, height=HEIGHT)
        btn_delete_email = tk.Button(self, text="Delete email", command=delete_email, width=WIDTH, height=HEIGHT)
        btn_delete_address = tk.Button(self, text="Delete address", command=delete_address, width=WIDTH, height=HEIGHT)
        btn_delete_birthday = tk.Button(self, text="Delete birthday", command=delete_birthday, width=WIDTH, height=HEIGHT)

        btn_delete_contact.grid(row=1, column=3, sticky="e", padx=PADX, pady=PADY)
        btn_delete_phone.grid(row=2, column=3, sticky="e", padx=PADX, pady=PADY)
        btn_delete_email.grid(row=3, column=3, sticky="e", padx=PADX, pady=PADY)
        btn_delete_address.grid(row=4, column=3, sticky="e", padx=PADX, pady=PADY)
        btn_delete_birthday.grid(row=5, column=3, sticky="e", padx=PADX, pady=PADY)

        # For Notes 1:
        btn_add_note = tk.Button(self, text="Add note", command=add_note, width=WIDTH, height=HEIGHT)
        btn_add_tag = tk.Button(self, text="Add tag", command=add_tag, width=WIDTH, height=HEIGHT)

        btn_add_note.grid(row=7, column=0, sticky="w", padx=PADX, pady=PADY)
        btn_add_tag.grid(row=8, column=0, sticky="w", padx=PADX, pady=PADY)

        # For Notes 2:
        btn_search_note = tk.Button(self, text="Search note", command=search_note, width=WIDTH, height=HEIGHT)
        btn_search_tag = tk.Button(self, text="Search tag", command=search_tag, width=WIDTH, height=HEIGHT)

        btn_search_note.grid(row=7, column=1, sticky="e", padx=PADX, pady=PADY)
        btn_search_tag.grid(row=8, column=1, sticky="e", padx=PADX, pady=PADY)

        # For Notes 3:
        btn_change_note = tk.Button(self, text="Change note", command=change_note, width=WIDTH, height=HEIGHT)
        btn_change_tag = tk.Button(self, text="Change tag", command=change_tag, width=WIDTH, height=HEIGHT)

        btn_change_note.grid(row=7, column=2, sticky="e", padx=PADX, pady=PADY)
        btn_change_tag.grid(row=8, column=2, sticky="e", padx=PADX, pady=PADY)

        # For Notes 4:
        btn_delete_note = tk.Button(self, text="Delete note", command=delete_note, width=WIDTH, height=HEIGHT)
        btn_delete_tag = tk.Button(self, text="Delete tag", command=delete_tag, width=WIDTH, height=HEIGHT)

        btn_delete_note.grid(row=7, column=3, sticky="e", padx=PADX, pady=PADY)
        btn_delete_tag.grid(row=8, column=3, sticky="e", padx=PADX, pady=PADY)


        # For Sorting Files:
        btn_sorting_files = tk.Button(self, text="Sorting files", command=sorting_files, width=WIDTH, height=HEIGHT)

        btn_sorting_files.grid(row=10, column=0, sticky="w", padx=PADX, pady=PADY)
 


if __name__ == "__main__":
    app = CenteredWindow()
    app.mainloop()
