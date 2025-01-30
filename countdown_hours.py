import tkinter as tk
import datetime

class Countdown(tk.Tk):

    def __init__(self):
        super().__init__()

        self.geometry('250x200')
        self.title('App')
        self.config(bg='red')
        self.running = False
        self.time_left = 0
        self.frame()

    def frame(self):

        self.menu_bar = tk.Menu(self)
        self.configure(menu=self.menu_bar)

        self.app_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='file',menu=self.app_menu)
        self.menu_bar.add_command(label='Quit',command = self.quit)

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill='both',expand=True)

        self.main_frame.rowconfigure(0,weight=1)
        self.main_frame.columnconfigure((0,1),weight=1)

        tk.Label(self.main_frame,text='Enter Time in H/M/S : ',font=('Arial',12)).grid(padx=10,row =0,column=0,columnspan=2,pady=10,sticky='ew')
        self.enter = tk.Entry(self.main_frame,width=15)
        self.enter.grid(row =1,column=0,columnspan=2,pady=5,sticky='ew',padx=5)

        tk.Button(self.main_frame,text='Start',command=self.start,bg='black',fg='white').grid(padx=5,sticky='ew',row =2,column=0,pady=5)
        tk.Button(self.main_frame,text='Pause',command=self.pause,bg='black',fg='white').grid(padx=5,sticky='ew',row =2,column=1,pady=5)
        tk.Button(self.main_frame,text='Reset',command=self.reset,bg='black',fg='white').grid(padx=5,sticky='ew',row =3,column=0,pady=5)
        tk.Button(self.main_frame,text='Resume',command=self.resume,bg='black',fg='white').grid(padx=5,sticky='ew',row =3,column=1,pady=5)

        self.show_var = tk.StringVar(value = '00:00:00')
        tk.Label(self.main_frame,textvariable=self.show_var).grid(row =4,column=0,columnspan=2,pady=10,padx=5)

    def start(self):

        if not self.running:
            print('in start')
            try:

                time_ = self.enter.get().strip()
                hours,min,secs = map(int,time_.split(':'))
                self.time_left = hours * 3600 + min * 60 + secs
                self.running = True
                self.countdown()
            except ValueError as e:
                self.show_var.set('invalid input')
                print(e)

    def countdown(self):
        print('in countdown')

        if self.running and self.time_left > 0:
            hours, remainder = divmod(self.time_left,3600)
            mins,secs = divmod(remainder,60)
            self.show_var.set(f'{hours:02}:{mins:02}:{secs:02}')
            self.time_left -= 1
            self.after(1000,self.countdown)
        elif self.time_left == 0:
            self.show_var.set('Times up')

    def pause(self):
        
        self.running = False

    def resume(self):
        if not self.running and self.time_left > 0:
            self.running = True
            self.countdown()

    def reset(self):
        
        self.running = False
        self.time_left = 0
        self.show_var.set('00:00:00')
    



if __name__ == '__main__':
    app = Countdown()
    app.mainloop()


