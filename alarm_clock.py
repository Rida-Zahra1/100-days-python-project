import datetime
import tkinter as tk
from tkinter.messagebox import showinfo,showerror


class AlarmClock(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('App')
        self.geometry('250x200')
        self.frame()
  
    def frame(self):

        tk.Label(self,text='Enter Time HH:MM:SS').pack(pady=10)
        self.user_var = tk.StringVar()
        tk.Entry(self,textvariable=self.user_var).pack(pady=5)
        tk.Button(self,text='Enter',bg='red',fg='white',command=self.set_alarm).pack(pady=5)
        self.display = tk.Label(self,)
        self.display.pack(pady=5)

    def set_alarm(self):

        user_input = self.user_var.get()
        try:
            self.alarm_time = datetime.datetime.strptime(user_input,"%H:%M:%S").time()
            showinfo(title="Alarm Set",message=f"Alarm set for {self.alarm_time}")
            self.alarm()

        except:
            showerror("Invalid Input", "Please enter time in HH:MM:SS format")

    def alarm(self):

        current = datetime.datetime.now().time()
        self.display.config(text=f'Current Time: {current.strftime("%H:%M:%S")}')

        if self.alarm_time and (self.alarm_time.hour,self.alarm_time.minute,self.alarm_time.second) == (current.hour,current.minute,current.second):
            showinfo('alarm time',"wake up")
            return
                

        self.after(1000,self.alarm)


if __name__ == "__main__":
    app = AlarmClock()
    app.mainloop()