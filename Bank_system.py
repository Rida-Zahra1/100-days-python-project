import tkinter as tk
from tkinter.scrolledtext import ScrolledText 
from tkinter.messagebox import showerror,showinfo 
from tkcalendar import DateEntry
from datetime import datetime
import json

class Data(tk.Tk):
     
    file_name = 'bank_system_data.json'

    def __init__(self):
        super().__init__()
        self.data_base = Data.load_data() 
        self.email = None

    @staticmethod
    def load_data():
        print('in load data')
        try:
            with open(Data.file_name,'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}  
        except json.JSONDecodeError:
            return {}
        
    @staticmethod
    def save_data(data_base):
        print('in savae data')
        try:
            with open(Data.file_name,'w') as file:
                json.dump(data_base,file,indent=4)

        except Exception as e:
            print(e)

    def bank_Account_Creation(self,user_name,father_name,birth_date,pin_code,amounts):
        print('in bank account creation')
        name = user_name
        father = father_name
        birth = str(birth_date)
        pin = pin_code
        amount = amounts
        
        if name and father and birth and pin and int(amount):
            print('in saving process')
            self.data_base[self.email]['Account_info'] = {
                'name' : name,
                'father' : father,
                'DOB' : birth,
                'pin' : pin,
                'amount' : amount

            }
            Data.save_data(self.data_base)
            showinfo(title='Account Creation Successfull',message='Information are successfully added to the system.')
            print(self.data_base)
            self.showing_frame()

        else:
            showerror(title='Account_Creation',message='All Fields Required')

    def showing_frame(self):

        self.new_frame.destroy()
        self.frame()

    def check_info_withdraw(self,user_name,pin_code):

        name = user_name
        pin = pin_code

        print(f"Stored Name: '{self.data_base[self.email]['Account_info']['name']}'")
        print(f"Entered Name: '{name}'")
        print(f"Checking for email: {self.email}")
        print(f"Database: {self.data_base}")


        if isinstance(self,Bank):
            if self.data_base[self.email]['Account_info']['name'].lower().strip() == name.lower().strip():
                if self.data_base[self.email]['Account_info']['pin'] == pin.strip():
                    self.Withdraw_window()
                else:
                    showerror('Bank','not correct pin')
            else:
                showerror('Bank','not correct name')

    def check_info_Deposit(self,user_name,pin_code):

        name = user_name
        pin = pin_code

        if isinstance(self,Bank):
            if self.data_base[self.email]['Account_info']['name'] == name:
                if self.data_base[self.email]['Account_info']['pin'] == pin:
                    self.Deposit_window()
                else:
                    showerror('Bank','not correct pin')
            else:
                showerror('Bank','not correct name')

    def process_withdrawal(self, amounts):
        print('in process withdrawal')
        withdraw_amount = int(amounts)

        if isinstance(self, Bank):
            user_amount = self.data_base[self.email]['Account_info']['amount']
            
            if user_amount >= withdraw_amount:
                user_amount -= withdraw_amount
                self.data_base[self.email]['Account_info']['amount'] = user_amount
                Data.save_data(self.data_base)
                showinfo('Withdraw', 'Withdrawal Successful')

                self.report.config(state='normal')
                self.report.delete(1.0, tk.END)  
                self.report.insert(tk.END, f"Account_info : \n Name :  {self.data_base[self.email]['Account_info']['name']},"
                                        f"\n Father_Name : {self.data_base[self.email]['Account_info']['father']},"
                                        f"\n Date_Birth : {self.data_base[self.email]['Account_info']['DOB']},"
                                        f"\n Amount : {self.data_base[self.email]['Account_info']['amount']}")
                
                self.report.config(state='disabled') 

            else:
                showerror('Withdraw', 'Withdrawal amount is greater than deposited amount')

    def deposit_process(self, amounts):
        print('in deposit process')
        deposit_amount = int(amounts)

        if isinstance(self, Bank): 
            user_amount = self.data_base[self.email]['Account_info']['amount']
            user_amount = int(user_amount)
            
            if deposit_amount: 
                user_amount += deposit_amount
                self.data_base[self.email]['Account_info']['amount'] = user_amount
                Data.save_data(self.data_base)
                showinfo('Deposit', 'Deposit Successful')

                self.report.config(state='normal')
                self.report.delete(1.0, tk.END) 
                self.report.insert(tk.END, f"Account_info : \n Name :  {self.data_base[self.email]['Account_info']['name']},"
                                        f"\n Father_Name : {self.data_base[self.email]['Account_info']['father']},"
                                        f"\n Date_Birth : {self.data_base[self.email]['Account_info']['DOB']},"
                                        f"\n Amount : {self.data_base[self.email]['Account_info']['amount']}")
                
                self.report.config(state='disabled')  
            
            else:
                showerror('Deposit', 'Invalid input to deposit amount')

class LogIn(Data):

    def __init__(self):
        super().__init__()
        self.title('To Do List Application')
        self.geometry('400x400')
        self.data_base = Data.load_data()
        print(self.data_base)
        self.log_in_user()

    def log_in_user(self):
        
        # Create main frame with padding and background color
        self.main_frame = tk.Frame(self, bg="#2c3e50")
        self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Welcome Frame (Title)
        self.welcome_frame = tk.Frame(self.main_frame, bg="#2c3e50")
        self.welcome_frame.pack(fill='x', pady=10)

        tk.Label(
            self.welcome_frame, text="Welcome To ATM", font=("Helvetica", 18, "bold"),
            bg="#2c3e50", fg="white"
        ).pack(fill='both', padx=10, pady=10)

        # Login Frame
        self.log_frame = tk.Frame(self.main_frame, bg="#34495e", padx=20, pady=20)
        self.log_frame.pack(pady=10)

        # Configure grid layout
        self.log_frame.columnconfigure(0, weight=1)
        self.log_frame.columnconfigure(1, weight=2)

        # Title
        tk.Label(
            self.log_frame, text="Log-In Form", font=("Helvetica", 20, "bold"), 
            bg="#34495e", fg="white"
        ).grid(row=0, column=0, columnspan=2, pady=5)

        # Email
        tk.Label(
            self.log_frame, text="Email:", font=("Helvetica", 13, "bold"), 
            bg="#34495e", fg="white"
        ).grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.email_var = tk.StringVar()
        tk.Entry(
            self.log_frame, textvariable=self.email_var, font=("Helvetica", 12), 
            bg="#ecf0f1", relief="solid", width=25
        ).grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Password
        tk.Label(
            self.log_frame, text="Password:", font=("Helvetica", 13, "bold"), 
            bg="#34495e", fg="white"
        ).grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.pass_var = tk.StringVar()
        tk.Entry(
            self.log_frame, textvariable=self.pass_var, show="*", font=("Helvetica", 12), 
            bg="#ecf0f1", relief="solid", width=25
        ).grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Login & Register Buttons
        tk.Button(
            self.log_frame, text="Log In", font=("Helvetica", 14, "bold"), 
            bg="#e74c3c", fg="white", relief="raised", borderwidth=3, width=12,
            command=self.log_in_direct
        ).grid(row=3, column=0, padx=10, pady=15, sticky="e")

        tk.Button(
            self.log_frame, text="Register", font=("Helvetica", 14, "bold"), 
            bg="#3498db", fg="white", relief="raised", borderwidth=3, width=12,
            command=self.register
        ).grid(row=3, column=1, padx=10, pady=15, sticky="w")

    def register(self):
        # Hide the main frame
        self.main_frame.pack_forget()

        # Create registration frame with background color and padding
        self.reg_main_frame = tk.Frame(self, bg="#2c3e50", padx=20, pady=20)
        self.reg_main_frame.pack(fill='y', expand=True, pady=15)

        # Title Label
        tk.Label(
            self.reg_main_frame, text="Please Fill The Form", 
            font=("Helvetica", 18, "bold"), bg="#2c3e50", fg="white"
        ).grid(row=0, column=0, columnspan=2, pady=15)

        # Grid Configuration
        self.reg_main_frame.columnconfigure(0, weight=1)
        self.reg_main_frame.columnconfigure(1, weight=2)

        # Name Field
        tk.Label(
            self.reg_main_frame, text="Name:", font=("Helvetica", 13, "bold"), 
            bg="#2c3e50", fg="white"
        ).grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.reg_name_var = tk.StringVar()
        tk.Entry(
            self.reg_main_frame, textvariable=self.reg_name_var, font=("Helvetica", 12), 
            bg="#ecf0f1", relief="solid", width=25
        ).grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Email Field
        tk.Label(
            self.reg_main_frame, text="Email:", font=("Helvetica", 13, "bold"), 
            bg="#2c3e50", fg="white"
        ).grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.reg_email_var = tk.StringVar()
        tk.Entry(
            self.reg_main_frame, textvariable=self.reg_email_var, font=("Helvetica", 12), 
            bg="#ecf0f1", relief="solid", width=25
        ).grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Password Field
        tk.Label(
            self.reg_main_frame, text="Password:", font=("Helvetica", 13, "bold"), 
            bg="#2c3e50", fg="white"
        ).grid(row=3, column=0, padx=10, pady=5, sticky="e")

        self.reg_pass_var = tk.StringVar()
        tk.Entry(
            self.reg_main_frame, textvariable=self.reg_pass_var, show="*", font=("Helvetica", 12), 
            bg="#ecf0f1", relief="solid", width=25
        ).grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Submit Button with rounded corners
        submit_btn = tk.Button(
            self.reg_main_frame, text="Submit", font=("Helvetica", 14, "bold"), 
            bg="#e74c3c", fg="white", relief="raised", borderwidth=3, width=12,
            command=self.reg_direct
        )
        submit_btn.grid(row=4, column=0, columnspan=2, pady=15)

        # Hover Effect
        def on_enter(e):
            submit_btn.config(bg="#c0392b")

        def on_leave(e):
            submit_btn.config(bg="#e74c3c")

        submit_btn.bind("<Enter>", on_enter)
        submit_btn.bind("<Leave>", on_leave)

    def reg_direct(self):

        name = self.reg_name_var.get().strip()
        email = self.reg_email_var.get().strip()
        password = self.reg_pass_var.get().strip()

        if email and password and name:

            if email in self.data_base:
                showerror(title='Registration',message='Email Already Exist')
                return
                
            self.data_base[email] = {
                'Name' : name ,
                'Password' : password
            }

            Data.save_data(self.data_base)
            showinfo(title='Success', message='Registration Successful')
            self.reg_main_frame.destroy()
            self.log_in_user()

        else:
            showerror(title='Registration',message='All fields required')
            return



    def log_in_direct(self):

        email = self.email_var.get().strip()
        password = self.pass_var.get().strip()

        if email in self.data_base:
            if self.data_base[email]['Password'] == password:
                showinfo(title="Success", message="Login Successful")
                self.main_frame.destroy()
                if isinstance(self, Bank):
                    self.email = email
                    self.frame()
            else:
                showerror(title='Log_in', message='enter valid password')
        else:
            showerror(title='Log_in', message='enter valid email and password')



class Bank(LogIn):
    def __init__(self):
        super().__init__()
        self.email = None

    def frame(self):
        print(self.data_base)
        # Create main frame with background color
        self.main_frame = tk.Frame(self, bg="#2c3e50")  
        self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Configure layout
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        for i in range(6):  
            self.main_frame.rowconfigure(i, weight=1)

        # Title Label
        tk.Label(self.main_frame, text="Welcome To ATM", font=("Helvetica", 20, "bold"), 
                bg="#2c3e50", fg="white").grid(row=0, column=0, columnspan=2, pady=20)

        # Name Entry
        self.name_var = tk.StringVar()
        tk.Label(self.main_frame, text="Name:", font=("Helvetica", 13, "bold"), 
                bg="#2c3e50", fg="white").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        tk.Entry(self.main_frame, textvariable=self.name_var, font=("Helvetica", 12), relief="solid", 
                bg="#ecf0f1", width=20).grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # PIN Entry
        self.pin_var = tk.StringVar()
        tk.Label(self.main_frame, text="Pin Code:", font=("Helvetica", 13, "bold"), 
                bg="#2c3e50", fg="white").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        tk.Entry(self.main_frame, textvariable=self.pin_var, font=("Helvetica", 12), relief="solid", 
                bg="#ecf0f1", show="*", width=20).grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Withdraw Button
        tk.Button(self.main_frame, text="Withdraw", font=("Helvetica", 14, "bold"), bg="#e74c3c", fg="white",
                relief="raised", borderwidth=3, width=15,
                command=lambda: self.check_info_withdraw(self.name_var.get().strip(), self.pin_var.get().strip())
                ).grid(row=3, column=0, pady=10, padx=5, sticky="e")

        # Deposit Button
        tk.Button(self.main_frame, text="Deposit", font=("Helvetica", 14, "bold"), bg="#27ae60", fg="white",
                relief="raised", borderwidth=3, width=15,
                command=lambda: self.check_info_Deposit(self.name_var.get().strip(), self.pin_var.get().strip())
                ).grid(row=3, column=1, pady=10, padx=5, sticky="w")

        # New Member Button
        tk.Button(self.main_frame, text="New Member", font=("Helvetica", 14, "bold"), bg="#3498db", fg="white",
                relief="raised", borderwidth=3, width=32,
                command=self.Create_account).grid(row=4, column=0, columnspan=2, pady=15, padx=10, sticky="ew")

    def Create_account(self):

        self.main_frame.destroy()

        # Create new frame with background color
        self.new_frame = tk.Frame(self, bg="#e6f2ff")  
        self.new_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Configure layout
        self.new_frame.columnconfigure(0, weight=1)
        self.new_frame.columnconfigure(1, weight=2)

        for i in range(7):  
            self.new_frame.rowconfigure(i, weight=1)

        # Title Label
        tk.Label(self.new_frame, text="Create New Account", font=("Helvetica", 18, "bold"), 
                bg="#e6f2ff", fg="black").grid(row=0, column=0, columnspan=2, pady=15)

        # Name Field
        self.new_name_var = tk.StringVar()
        tk.Label(self.new_frame, text="Full Name:", font=("Helvetica", 13, "bold"), 
                bg="#e6f2ff").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(self.new_frame, textvariable=self.new_name_var, font=("Helvetica", 12), relief="solid").grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Father Name
        self.Father_name_var = tk.StringVar()
        tk.Label(self.new_frame, text="Father's Name:", font=("Helvetica", 13, "bold"), 
                bg="#e6f2ff").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(self.new_frame, textvariable=self.Father_name_var, font=("Helvetica", 12), relief="solid").grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        # Date of Birth
        tk.Label(self.new_frame, text="Date of Birth:", font=("Helvetica", 13, "bold"), 
                bg="#e6f2ff").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.Date_birth = DateEntry(self.new_frame, font=("Helvetica", 12), relief="solid")
        self.Date_birth.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        # Pin Code
        self.new_pin_var = tk.StringVar()
        tk.Label(self.new_frame, text="Pin Code:", font=("Helvetica", 13, "bold"), 
                bg="#e6f2ff").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(self.new_frame, textvariable=self.new_pin_var, font=("Helvetica", 12), relief="solid", show="*").grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        # Deposit Amount
        self.deposit_amount_var = tk.StringVar()
        tk.Label(self.new_frame, text="Initial Deposit (Min 1000):", font=("Helvetica", 13, "bold"), 
                bg="#e6f2ff").grid(row=5, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(self.new_frame, textvariable=self.deposit_amount_var, font=("Helvetica", 12), relief="solid").grid(row=5, column=1, padx=10, pady=5, sticky="ew")

        # Submit Button
        tk.Button(self.new_frame, text="Create Account", bg="#ff4d4d", fg="white", font=("Helvetica", 14, "bold"),
                relief="raised", borderwidth=3, width=20,
                command=lambda: self.bank_Account_Creation(
                    self.new_name_var.get().strip(),
                    self.Father_name_var.get().strip(),
                    self.Date_birth.get_date(),
                    self.new_pin_var.get(),
                    self.deposit_amount_var.get().strip()
                )).grid(row=6, column=0, columnspan=2, pady=15, padx=10, sticky="ew")



    def Withdraw_window(self):
        self.main_frame.destroy()

        # Create the withdraw frame with a soft blue background
        self.withdraw_frame = tk.Frame(self, bg="#e6f2ff")  
        self.withdraw_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Configure row and column for alignment
        self.withdraw_frame.columnconfigure((0, 1), weight=1)

        self.amount_var = tk.IntVar()

        # Heading Label
        tk.Label(self.withdraw_frame, text="Withdraw Amount", font=("Helvetica", 16, "bold"), 
                bg="#e6f2ff", fg="black").grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Label and Entry Field
        tk.Label(self.withdraw_frame, text="Amount:", font=("Helvetica", 14), 
                bg="#e6f2ff").grid(row=1, column=0, padx=10, pady=5, sticky='e')

        tk.Entry(self.withdraw_frame, textvariable=self.amount_var, font=("Helvetica", 12), width=20, 
                relief="solid").grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Buttons (Enter and Sign Out)
        tk.Button(self.withdraw_frame, text="Enter", bg="#ff4d4d", fg="white", font=("Helvetica", 12, "bold"),
                relief="raised", borderwidth=3, width=15,
                command=lambda: self.process_withdrawal(self.amount_var.get())).grid(row=2, column=0, pady=10, padx=10)

        tk.Button(self.withdraw_frame, text="Sign Out", bg="#ff4d4d", fg="white", font=("Helvetica", 12, "bold"),
                relief="raised", borderwidth=3, width=15,
                command=self.sign_out_withdraw).grid(row=2, column=1, pady=10, padx=10)

        # Report Text Widget (for displaying messages)
        self.report = tk.Text(self.withdraw_frame, state="disabled", height=6, width=45, font=("Helvetica", 12),
                            bg="#f0f0f0", relief="sunken", bd=2)
        self.report.grid(row=3, column=0, columnspan=2, pady=15, padx=10, sticky="ew")


    def Deposit_window(self):
        self.main_frame.destroy()

        # Create the deposit frame
        self.deposit_frame = tk.Frame(self, bg="#e6f2ff")  
        self.deposit_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Column Configuration for proper alignment
        self.deposit_frame.columnconfigure((0, 1), weight=1)

        self.dep_amount_var = tk.IntVar()

        # Heading Label
        tk.Label(self.deposit_frame, text="Deposit Amount", font=("Helvetica", 16, "bold"), bg="#e6f2ff").grid(
            row=0, column=0, columnspan=2, pady=(0, 10))

        # Label and Entry Field
        tk.Label(self.deposit_frame, text="Amount:", font=("Helvetica", 14), bg="#e6f2ff").grid(
            row=1, column=0, padx=10, pady=5, sticky='e')

        tk.Entry(self.deposit_frame, textvariable=self.dep_amount_var, font=("Helvetica", 12), width=20, relief="solid").grid(
            row=1, column=1, padx=10, pady=5, sticky='ew')

        # Buttons (Enter and Sign Out)
        tk.Button(self.deposit_frame, text="Enter", bg="#ff4d4d", fg="white", font=("Helvetica", 12, "bold"),
                relief="raised", borderwidth=3, width=15,
                command=lambda: self.deposit_process(self.dep_amount_var.get())).grid(
            row=2, column=0, pady=10, padx=10)

        tk.Button(self.deposit_frame, text="Sign Out", bg="#ff4d4d", fg="white", font=("Helvetica", 12, "bold"),
                relief="raised", borderwidth=3, width=15,
                command=self.sign_out_deposit).grid(
            row=2, column=1, pady=10, padx=10)

        # Report Text Widget (for displaying messages)
        self.report = tk.Text(self.deposit_frame, state="disabled", height=6, width=45, font=("Helvetica", 12),
                            bg="#f0f0f0", relief="sunken", bd=2)
        self.report.grid(row=3, column=0, columnspan=2, pady=15, padx=10, sticky="ew")


    def sign_out_withdraw(self):

        self.withdraw_frame.destroy()
        self.frame()
        
    def sign_out_deposit(self):

        self.deposit_frame.destroy()
        self.frame()

    def sign_in(self):

        self.new_frame.destroy()
        self.main_frame.pack(fill='both',expand= True)


if __name__ == '__main__':
    app = Bank()
    app.mainloop()



