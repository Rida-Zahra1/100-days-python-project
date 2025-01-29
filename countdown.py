import tkinter as tk

class Focus(tk.Tk):

    def __init__(self):
        super().__init__()


        self.running = False
        self.time_left = 0

    def focus_mode(self):

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

if __name__ == '__main__':
    app = Focus()
    app.mainloop()
