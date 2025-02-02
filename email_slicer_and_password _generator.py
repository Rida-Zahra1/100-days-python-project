import re
import tkinter as tk
import random
import string

class EmailSlicer(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Email Slicer')
        self.geometry('300x250') 
        self.frame()
        self.email_()

    def frame(self):
        self.main_frame = tk.Menu(self)
        self.configure(menu=self.main_frame)

        self.file = tk.Menu(self.main_frame,tearoff=0)
        self.file.add_command(label='Password Generator', command=self.direct_password)
        self.file.add_command(label='Email Slicer', command=self.direct_email)
        self.file.add_command(label='Quit', command=self.quit)
        self.main_frame.add_cascade(label='File', menu=self.file)

    def email_(self):
        """Creates the Email Slicer UI"""
        self.slicer_frame = tk.Frame(self)
        self.slicer_frame.pack(fill='both', expand=True)

        tk.Label(self.slicer_frame, text='Enter your Email', font=('Helvetica', 15)).pack(pady=10)
        self.enter_var = tk.StringVar()
        tk.Entry(self.slicer_frame, width=25, textvariable=self.enter_var).pack(pady=5)
        tk.Button(self.slicer_frame, text='Enter', bg='red', fg='white', command=self.email_slicer).pack(pady=5)

        self.username = tk.Label(self.slicer_frame, text='')
        self.username.pack(pady=3)

        self.domain = tk.Label(self.slicer_frame, text='')
        self.domain.pack(pady=3)

    def email_slicer(self):
        """Extracts username and domain from the email"""
        email = self.enter_var.get()
        pattern = r"([^@]+)@([a-z]+)"
        match = re.match(pattern, email)

        if match:
            self.username.config(text=f'UserName: {match.group(1)}')
            self.domain.config(text=f'Domain: {match.group(2)}')
        else:
            self.username.config(text="Invalid Email")
            self.domain.config(text="")

    def password_generator(self):
        """Creates the Password Generator UI"""
        self.password_frame = tk.Frame(self)
        self.password_frame.pack(fill='both', expand=True)

        tk.Label(self.password_frame, text='Enter password length', font=('Helvetica', 15)).pack(pady=10)
        self.pass_var = tk.StringVar()
        tk.Entry(self.password_frame, width=10, textvariable=self.pass_var).pack(pady=5)
        tk.Button(self.password_frame, text='Generate', bg='red', fg='white', command=self.pass_generate).pack(pady=5)

        self.password = tk.Label(self.password_frame, text='')
        self.password.pack(pady=3)

    def pass_generate(self):
        """Generates a random password"""
        try:
            length = int(self.pass_var.get())
            if length < 4:
                self.password.config(text="Length must be at least 4")
                return

            characters = list(string.ascii_letters + string.digits + string.punctuation)
            random.shuffle(characters)
            password = ''.join(random.choices(characters,k=length))

            self.password.config(text=f'Generated Password: {password}')
        except ValueError:
            self.password.config(text="Enter a valid number")

    def direct_email(self):
        """Switch to Email Slicer UI"""

        self.password_frame.destroy()
        self.email_()

    def direct_password(self):
        """Switch to Password Generator UI"""

        self.slicer_frame.destroy()
        self.password_generator()


if __name__ == '__main__':
    app = EmailSlicer()
    app.mainloop()
