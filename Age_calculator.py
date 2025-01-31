import tkinter as tk
import datetime as datetime 

class AgeCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x150')
        self.title('Age Calculator App')
        self.frame()

    def frame(self):
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill='y')

        tk.Label(self.main_frame,text='Enter your age DD/MM/YYYY :',font=('Arial',15)).pack(fill='x',pady=5)

        self.entry = tk.Entry(self.main_frame)
        self.entry.pack(fill='x',ipady=10)

        self.show_var = tk.StringVar()
        tk.Label(self.main_frame,textvariable=self.show_var).pack(fill='x',pady=5)

        tk.Button(self.main_frame,command=self.calculate,text='Enter',bg='red',fg='white',width=10).pack(padx=10,pady=10)

    def calculate(self):

        try:
            self.now = datetime.datetime.now()
            self.user_age = datetime.datetime.strptime(self.entry.get().strip(),"%d/%m/%Y")
            self.diff = (self.now - self.user_age).days // 365
            self.show_var.set(self.diff)
        except ValueError:
            self.show_var.set('invalid input')


if __name__ == "__main__":
    app = AgeCalculator()
    app.mainloop()
