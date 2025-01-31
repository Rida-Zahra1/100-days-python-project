import random
import tkinter as tk
from tkinter.messagebox import showerror,showinfo

class Hangman(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Hangman App')

        self.words_list = [
                        "apple", "banana", "cherry", "date", "elephant", "frog", "grape", 
                        "honey", "ice", "jungle", "kite", "lemon", "mango", "notebook", 
                        "orange", "pineapple", "quilt", "rose", "sunflower", "tree", 
                        "umbrella", "violet", "watermelon", "xylophone", "yellow", "zebra"
                    ]

        self.word = random.choice(self.words_list)
        self.word_dash = ['_' for i in range(len(self.word))]
        self.user_guess = set()

        self.max_atempts = 6
        self.user_atempts = self.max_atempts

        self.frame()

    def frame(self):

        self.canvas = tk.Canvas(self,width=300,height=300)
        self.canvas.pack(pady=10)

        self.label_dash = tk.Label(self,text=' '.join(self.word_dash),font=('Helvetic',15))
        self.label_dash.pack(pady=5)

        self.atempts = tk.Label(self,text=f'Remaining atempts : {self.user_atempts}')
        self.atempts.pack(pady=5)
        
        self.user_enter = tk.Entry(self)
        self.user_enter.pack(pady=5)

        tk.Button(self,text='Guess',command=self.guess,width=10).pack(pady=5)
        tk.Button(self,text='Reset',command=self.reset,width=10).pack(pady=10)

    def guess(self):
        
        letter = self.user_enter.get().lower().strip()
        self.user_enter.delete(0,tk.END)

        if not letter or len(letter) > 1:
            showerror(title='Invalid Input',message='Enter single Character')
            return

        if letter in self.user_guess:
            showerror(title='Invalid Input',message='Character Already Entered')
            return
        
        if letter in self.word:
            for index,char in enumerate(self.word):
                if letter == char:
                    self.word_dash[index] = char
                    self.update_labels()
        else:
            self.user_atempts -= 1
            self.draw_hangman()

        self.user_guess.add(letter)
        self.update_labels()
        self.check_winner()

    def update_labels(self):

        self.label_dash.config(text=' '.join(self.word_dash))
        self.atempts.config(text=f'Remaining atempts : {self.user_atempts}')

    def check_winner(self):

        if '_' not in self.word_dash:
            showinfo(title='Hangman Game',message='Congrajulation,You won the game')
            self.reset()
        
        elif self.user_atempts <= 0:
            showinfo(title='Hangman Game',message='Sorry,You lost the game')
            self.reset()

    def draw_hangman(self):

        if self.user_atempts == 5:
            self.canvas.create_oval(130,100,170,140,width=2) #head
        elif self.user_atempts == 4:
            self.canvas.create_line(150,140,150,200,width=2)
        elif self.user_atempts == 3:
            self.canvas.create_line(150,140,130,180,width=2)
            self.canvas.create_line(150,140,170,180,width=2)
        elif self.user_atempts ==2:
            self.canvas.create_line(150,200,130,240,width=2)
            self.canvas.create_line(150,200,170,240,width=2)
        elif self.user_atempts == 1:
            self.canvas.create_line(150,50,150,100,width=2)
        else:
            self.canvas.create_line(100,280,100,50,width=2)
            self.canvas.create_line(100,50,150,50,width=2)
            self.canvas.create_line(20,280,180,280,width=2)

    def reset(self):

        self.user_atempts = self.max_atempts
        self.word = random.choice(self.words_list)
        self.word_dash = ['_' for _ in self.word]
        self.user_guess.clear()
        self.canvas.delete('all')
        self.update_labels()

    def window(self):

        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        win_width = self.winfo_width()
        win_height = self.winfo_height()
        x = (screen_width/2) - (win_width/2)
        y = (screen_height/2) - (win_height/2)
        self.geometry(f'{win_width}{win_height}+{x}+{y}')








if __name__ == '__main__':
    app = Hangman()
    app.mainloop()