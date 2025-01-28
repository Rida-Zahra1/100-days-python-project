import tkinter as tk
from tkinter.messagebox import showerror
import json

class To_List(tk.Tk):

    data_file = 'data_base.json'

    def __init__(self):
        super().__init__()
        self.title('To Do List Application')
        self.geometry('400x400')

        To_List.data_base = self.load_data()

        self.log_in()


    @staticmethod
    def load_data():
        try:
            with open(To_List.data_file,'r') as file:
                return json.load(file)
        except Exception as e:
            return {}
        
    @staticmethod
    def save_data():
        with open(To_List.data_file,'w') as file:
            json.dump(To_List.data_base,file)

    def direct_existing_user(self):

        email = self.email_var.get()
        password = self.pass_var.get()
        if email in To_List.data_base:
            if To_List.data_base[email]['password'] == password:
                self.main.pack_forget()
                self.main_app()
            else:
                showerror(title='Form',message='wrong password')
        else:
            showerror(title='Form',message='Invalid email')

    def direct_new_user(self):

        name = self.name_var.get()
        email = self.email_new_var.get()
        password = self.pass_new_var.get()

        if email not in To_List.data_base:
            To_List.data_base[email] = {
                'name' : name,
                'password' : password 
            }
            To_List.save_data()
            self.main_frame.pack_forget()
            self.log_in()
        else:
            showerror(title='Registration Form',message='email already exist try new one')

    def log_in(self):

        self.main = tk.Frame(self)
        self.main.pack(fill='y')

        self.welcome_label = tk.Frame(self.main)
        self.welcome_label.pack(padx=20,pady=15)

        self.welcome = tk.Label(self.welcome_label,text='Welcome to To_Do_List \nApplication',font=('Consolas', 15))
        self.welcome.pack(fill='both')
      
        self.frame1 = tk.Frame(self.main)
        self.frame1.pack(fill='y', padx=30, pady=10, side='top')

        self.label_log = tk.Label(self.frame1, text='Log-in Form', font=('Consolas', 15), anchor='w')
        self.label_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='w')

        self.email_label = tk.Label(self.frame1, text='Email: ')
        self.email_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.email_var = tk.StringVar()
        self.email_entry = tk.Entry(self.frame1, textvariable=self.email_var)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

        self.pass_label = tk.Label(self.frame1, text='Password: ')
        self.pass_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        self.pass_var = tk.StringVar()
        self.pass_entry = tk.Entry(self.frame1, textvariable=self.pass_var, show="*")
        self.pass_entry.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

        self.frame1.columnconfigure(1, weight=1)

        self.log_in_button = tk.Button(self.frame1,text='log in',command=self.direct_existing_user,bg='red',fg='white')
        self.log_in_button.grid(row=3,column=0,pady=10,sticky='ewns')

        self.register_here = tk.Button(self.frame1,text='Register',command=self.new_member,bg='blue',fg='white')
        self.register_here.grid(row=3,column=1,pady=10,sticky='ns')



    def new_member(self):

        self.main.pack_forget()

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill='y')

        self.upper_frame = tk.Frame(self.main_frame)
        self.upper_frame.pack()

        self.register_here_label = tk.Label(self.upper_frame,text='Please fill the form',font=('Consolas', 15))
        self.register_here_label.pack(fill='both',padx=30,pady=30)

        self.lower_frame = tk.Frame(self.main_frame)
        self.lower_frame.pack()

        self.name_label = tk.Label(self.lower_frame,text='Name : ')
        self.name_label.grid(row=0,column=0,sticky='n',padx=10,pady=10)

        self.name_var = tk.StringVar()
        self.enter_name = tk.Entry(self.lower_frame,textvariable=self.name_var)
        self.enter_name.grid(row=0,column=1,padx=10,pady=10)

        self.email = tk.Label(self.lower_frame,text='Email : ')
        self.email.grid(row=1,column=0,padx=10,pady=10)

        self.email_new_var = tk.StringVar()
        self.email_new_usr = tk.Entry(self.lower_frame,textvariable=self.email_new_var)
        self.email_new_usr.grid(row=1,column=1,padx=10,pady=10)

        self.pass_new = tk.Label(self.lower_frame,text='Password : ')
        self.pass_new.grid(row=2,column=0,padx=10,pady=10,sticky='ew')

        self.pass_new_var = tk.StringVar()
        self.pass_new_enter = tk.Entry(self.lower_frame,textvariable=self.pass_new_var)
        self.pass_new_enter.grid(row=2,column=1,padx=10,pady=10,sticky='ew')

        self.lower_frame.columnconfigure(1, weight=1)

        self.new_btn = tk.Button(self.lower_frame,command=self.direct_new_user,text='Submit',bg='black',fg='white')
        self.new_btn.grid(row=3,column=0,padx=10,pady=10,sticky='ewns')


    def main_app(self):
        pass

if __name__ == '__main__':
    app = To_List()
    app.mainloop()
    print(To_List.data_base)
