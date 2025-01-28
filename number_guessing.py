import tkinter as tk
import random 

class NumGuess(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Number Guessing Game')
        self.config(bg='#00003f')
        self.geometry('250x150')
        self.random_number = random.randint(0,100)
        self.wind()

    def wind(self):

        self.label = tk.Label(self,text='Guess My Number',font=('Consolas',20),fg='yellow',bg='#00003f')
        self.label.pack(fill='both')

        self.frame = tk.Frame(self,bg='#00003f')
        self.frame.pack(fill='both',expand=True)

        self.frame2 = tk.Frame(self.frame)
        self.frame2.pack(fill='both',expand=True,padx=15,pady=15)

        self.var = tk.IntVar()
        self.enter = tk.Entry(self.frame2,textvariable=self.var)
        self.buton = tk.Button(self.frame2,text='Guess',command=self.check,bg='#66cdaa')
        self.enter.pack(fill='both',side='top',expand=True)
        self.buton.pack(fill='both',side='top',expand=True)

        self.restart_button = tk.Button(
            self.frame2, text='Restart', command=self.restart_game, bg='#ff6347', fg='white'
        )
        self.restart_button.pack(fill='both', side='top', expand=True)
        self.restart_button.pack_forget()

    def check(self):
        
        self.num = self.var.get()
        if self.num == self.random_number:
            self.label.config(text='Correct Guess')
            self.buton.config(state='disabled')
            self.enter.config(state='disabled')
            self.buton.pack_forget()
            self.restart_button.pack(fill='both',expand=True,side='top')
    
        elif self.num > self.random_number:
            self.label.config(text='too high')
        else:
            self.label.config(text='too low')

    def restart_game(self):
        self.random_number = random.randint(0, 100)
        self.label.config(text='Guess My Number')
        self.var.set(0)
        self.enter.delete(0, tk.END)
        self.enter.config(state='normal')
        self.buton.config(state='normal')
        self.restart_button.pack_forget()
        self.buton.pack(fill='both', side='top', expand=True)

if __name__ == '__main__':
    app = NumGuess()
    app.mainloop()
