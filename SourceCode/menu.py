from tkinter import *
from patient import Patient

class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")

        # Center the window
        window_width = 800
        window_height = 600
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.master.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        
        self.master.config(bg='lightblue')

        self.frame = Frame(self.master, bg='lightblue')
        self.frame.pack(pady=20)

        self.lblTitle = Label(self.frame, text="HOSPITAL - ADMIN", font=("Helvetica", 20, 'bold'), bg='lightblue', fg='#350d42')
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)

        self.LoginFrame = Frame(self.frame, width=400, height=300, relief="ridge", bg='lightblue', bd=20)
        self.LoginFrame.grid(row=1, column=0)

        # Buttons for each functionality
        self.btnRegister = Button(self.LoginFrame, text="Registration", width=30, font=("Helvetica", 14, 'bold'),
                                  bg='green', fg='white', command=self.open_registration)
        self.btnRegister.grid(row=1, column=0, pady=10)

        self.btnUpdate = Button(self.LoginFrame, text="Updation", width=30, font=("Helvetica", 14, 'bold'),
                                bg='blue', fg='white', command=self.open_updation)
        self.btnUpdate.grid(row=2, column=0, pady=10)

        self.btnSearch = Button(self.LoginFrame, text="Search", width=30, font=("Helvetica", 14, 'bold'),
                                bg='orange', fg='white', command=self.open_search)
        self.btnSearch.grid(row=3, column=0, pady=10)

        self.btnDelete = Button(self.LoginFrame, text="Delete", width=30, font=("Helvetica", 14, 'bold'),
                                bg='red', fg='white', command=self.open_delete)
        self.btnDelete.grid(row=4, column=0, pady=10)

        self.btnExit = Button(self.LoginFrame, text="Exit", width=30, font=("Helvetica", 14, 'bold'),
                              bg='black', fg='white', command=self.Exit)
        self.btnExit.grid(row=5, column=0, pady=10)

    def open_registration(self):
        self.newWindow = Toplevel(self.master)
        self.app = Patient(self.newWindow, mode="register")

    def open_updation(self):
        self.newWindow = Toplevel(self.master)
        self.app = Patient(self.newWindow, mode="update")

    def open_search(self):
        self.newWindow = Toplevel(self.master)
        self.app = Patient(self.newWindow, mode="search")

    def open_delete(self):
        self.newWindow = Toplevel(self.master)
        self.app = Patient(self.newWindow, mode="delete")

    def Exit(self):
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    menu = Menu(root)
    root.mainloop()
