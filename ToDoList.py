import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import json
from tkinter.messagebox import showerror


class Data:
    file_name = 'data_base1.json'
        
    @staticmethod
    def load_data():
        try:
            with open(Data.file_name, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        
    @staticmethod
    def save_data(data_base):
        with open(Data.file_name, 'w') as file:
            json.dump(data_base, file, indent=4)


class LogIn(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('To Do List Application')
        self.geometry('400x400')
        self.data_base = Data.load_data()
        self.log_in_user()

    def log_in_user(self):
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill='both', expand=True)

        self.welcome_frame = tk.Frame(self.main_frame)
        self.welcome_frame.pack(fill='y')

        tk.Label(self.welcome_frame, text='Welcome To To-Do List \nApplication', 
                 font=('Consolas', 15)).pack(fill='both', padx=10, pady=10)
    
        self.log_frame = tk.Frame(self.main_frame)
        self.log_frame.pack(fill='y', expand=True, pady=10)

        tk.Label(self.log_frame, text='Log-In Form', font=('Consolas', 20)).grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        tk.Label(self.log_frame, text='Email: ').grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        self.email_var = tk.StringVar()
        tk.Entry(self.log_frame, textvariable=self.email_var).grid(row=1, column=1, padx=5, pady=5, sticky='ew')

        tk.Label(self.log_frame, text='Password: ').grid(row=2, column=0, padx=10, pady=10, sticky='w')

        self.pass_var = tk.StringVar()
        tk.Entry(self.log_frame, textvariable=self.pass_var, show='*').grid(row=2, column=1, padx=5, pady=5, sticky='ew')

        tk.Button(self.log_frame, text='Log-in', command=self.log_in_direct, fg='white', bg='red').grid(row=3, column=0, padx=10, pady=10, sticky='ewns')
        tk.Button(self.log_frame, text='Register', command=self.register, fg='white', bg='blue').grid(row=3, column=1, padx=10, pady=10, sticky='ns')

    def register(self):
        self.main_frame.pack_forget()
        self.reg_main_frame = tk.Frame(self)
        self.reg_main_frame.pack(fill='y', expand=True, pady=15)

        tk.Label(self.reg_main_frame, text='Please Fill The Form', font=('Consolas', 15)).grid(row=0, column=0, columnspan=2, sticky='ew', pady=15)

        tk.Label(self.reg_main_frame, text='Name:').grid(row=1, column=0, padx=10, pady=10)
        
        self.reg_name_var = tk.StringVar()
        tk.Entry(self.reg_main_frame, textvariable=self.reg_name_var).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.reg_main_frame, text='Email:').grid(row=2, column=0, sticky='ew', padx=10, pady=10)
        
        self.reg_email_var = tk.StringVar()
        tk.Entry(self.reg_main_frame, textvariable=self.reg_email_var).grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.reg_main_frame, text='Password:').grid(row=3, column=0, sticky='ew', padx=10, pady=10)
        
        self.reg_pass_var = tk.StringVar()
        tk.Entry(self.reg_main_frame, textvariable=self.reg_pass_var, show='*').grid(row=3, column=1, padx=10, pady=10)

        tk.Button(self.reg_main_frame, command=self.reg_direct, text='Submit', bg='black', fg='white').grid(padx=10, pady=10, row=4, column=0, columnspan=2, sticky='ewns')

    def reg_direct(self):
        name = self.reg_name_var.get().strip()
        email = self.reg_email_var.get().strip()
        password = self.reg_pass_var.get().strip()

        if email and password and name:
                  
            if email not in self.data_base:
                self.data_base[email] = {
                    'name': name,
                    'password': password
                }

                Data.save_data(self.data_base)

                self.reg_main_frame.pack_forget()
                self.log_in_user()
            else:
                showerror(title='Registration Form', message='Email already exists')
        else:
            showerror(title='Registration Form', message='All fields required')


    def log_in_direct(self):
        email = self.email_var.get().strip()
        password = self.pass_var.get().strip()

        if not email:
            showerror(title='Registration Form', message='Enter email')
            return
        
        if not password:
            showerror(title='Registration Form', message='Enter password')
            return

        if email in self.data_base and self.data_base[email]['password'] == password:
            print(f"User {email} logged in")
            self.logged_in_user = email
            self.main_frame.pack_forget()
            ToDoListApp.main_app(self)
        else:
            showerror(title='Log In Form', message='all credentials required')
    
class ToDoListApp(LogIn):
    
    def __init__(self):
        super().__init__()

    def main_app(self):

        print("main_app called")
        self.main_app_frame = tk.Frame(self)
        self.main_app_frame.pack(fill='both', expand=True)

        self.menu = tk.Menu(self)
        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label='Quit', command=self.quit)
        file_menu.add_command(label='Focus', command=self.focus_mode)
        file_menu.add_command(label='task', command=self.view_task)
        self.menu.add_cascade(label='File', menu=file_menu)
        self.configure(menu=self.menu)


        self.task_frame = tk.Frame(self.main_app_frame)
        self.task_frame.pack(fill='both', expand=True)

        tk.Label(self.task_frame, text='Add Task',font=('Consolas',10)).grid(row=0, column=0, padx=10, pady=10)

        self.text_ = ScrolledText(self.task_frame, width=30, height=5)
        self.text_.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

        tk.Button(self.task_frame, command=self.add_task, text='Add', bg='red', fg='white').grid(row=2, column=0, padx=10, pady=10, sticky='ewns')
        tk.Button(self.task_frame, command=self.delete_task, text='Delete', bg='blue', fg='white').grid(row=2, column=1, padx=10, pady=10, sticky='ewns')

        self.view_task_frame = tk.Frame(self.main_app_frame)
        self.view_task_frame.pack(fill='both', expand=True)

        tk.Label(self.view_task_frame, text='Task List',font=('Consolas',10)).grid(row=0, column=0, ipadx=20)
        self.text_widget = tk.Text(self.view_task_frame,state='disabled', width=30, height=10)
        self.text_widget.grid(row=0, column=1)

        self.load_data()
        

    def add_task(self):
        text = self.text_.get('1.0',tk.END).strip()

        if text: 
            if hasattr(self,'logged_in_user'):
                print(f"Adding task: {text}")
                self.text_widget.config(state='normal')
                self.text_widget.insert(tk.END,text + '\n')
                self.text_widget.config(state='disabled')

                if 'task' not in self.data_base[self.logged_in_user]:
                    self.data_base[self.logged_in_user]['task'] = []
                self.data_base[self.logged_in_user]['task'].append(text)

                Data.save_data(self.data_base)
                self.text_.delete('1.0',tk.END)

        else:
            showerror(title='Task Error', message='Task cannot be empty')

    def delete_task(self):

        if hasattr(self,'logged_in_user'):
            print("Deleting all tasks")
            self.text_widget.config(state='normal')
            self.text_widget.delete('1.0',tk.END)
            self.text_widget.config(state='disabled')

            self.data_base[self.logged_in_user]['task'] = []
            Data.save_data(self.data_base)

    def load_data(self):

        task = self.data_base[self.logged_in_user]['task']
        print(f"Loading tasks for {self.logged_in_user}: {task}")

        if task:
            if hasattr(self,'logged_in_user') and 'task' in self.data_base[self.logged_in_user]:
                self.text_widget.config(state='normal')
                self.text_widget.delete('1.0',tk.END)

                
                for t in task:
                    self.text_widget.insert(tk.END,t + '\n')

                self.text_widget.config(state='disabled')

    def focus_mode(self):

        self.main_app_frame.pack_forget()
        self.running = False
        self.time_left = 0

        self.focus_frame = tk.Frame(self)
        self.focus_frame.pack(padx=10,pady=10)

        self.focus_frame.rowconfigure((0,1,2,3,4),weight=1)
        self.focus_frame.columnconfigure((0,1),weight=1)

        tk.Label(self.focus_frame,text='enter time (seconds) : ',font=('Consoals',20)).grid(row=0,column=0,columnspan=2,sticky='ew')
        
        self.enter_user = tk.Entry(self.focus_frame)
        self.enter_user.grid(row=1,column=0,columnspan=2,sticky='ew')

        self.time_var = tk.StringVar(value='00:00')
        tk.Label(self.focus_frame,textvariable=self.time_var,font=('Consoals',30)).grid(row=2,column=0,columnspan=2,sticky='ew')

        tk.Button(self.focus_frame,text='Start',command=self.start_focus).grid(row=3,column=0,sticky ='ew')
        tk.Button(self.focus_frame,text='Pause',command=self.pause_focus).grid(row=3,column=1,sticky ='ew')
        tk.Button(self.focus_frame,text='Reset',command=self.reset_focus).grid(row=4,column=0,columnspan=2,sticky ='ew')

    def start_focus(self):

        if not self.running:
            try:
                self.time_left = int(self.enter_user.get())
                self.running = True
                self.countdown()
            except ValueError:
                self.time_var.set('Invalid')

    def countdown(self):

        if self.running and self.time_left > 0:
            mins,secs = divmod(self.time_left,60)
            self.time_var.set(f'{mins:01} : {secs:01}')
            self.time_left -= 1
            self.after(1000,self.countdown)
        elif self.time_left == 0:
            self.time_var.set('Time\'s up!')

    def pause_focus(self):
        self.running = False

    def reset_focus(self):
        self.running = False
        self.time_left= 0
        self.time_var.set('00:00')

    def view_task(self):

        self.focus_frame.pack_forget()
        self.main_app()





       

if __name__ == '__main__':
    app = ToDoListApp()
    app.mainloop()
