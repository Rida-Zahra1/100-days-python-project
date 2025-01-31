import requests
import tkinter as tk
from tkinter import ttk

class RandomJoke(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('300x300')
        self.title('Random Joke Generator')
        self.resizable(0,0)
        self.url = f'https://official-joke-api.appspot.com/'
        self.types = [ '/random_joke', '/jokes/random','/jokes/random/']
        self.frame()

    def frame(self):

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill='both', expand=True, padx=10, pady=10)

        tk.Label(self.main_frame, text='Random Joke Generator', font=('Arial', 14, 'bold')).pack(pady=10)

        tk.Label(self.main_frame, text='Joke Type:', font=('Arial', 12)).pack()
        self.show_var = tk.StringVar()
        ttk.Combobox(self.main_frame, values=self.types, textvariable=self.show_var, state='readonly').pack(pady=5)
        self.show_var.set('/random_joke') 

        tk.Button(self.main_frame, text='Get Joke', bg='red', fg='white', font=('Arial', 12), command=self.fetch_joke).pack(pady=5)

        self.type = tk.Label(self.main_frame,font=('Arial',10))
        self.type.pack(pady=4)

        self.setup= tk.Label(self.main_frame,font=('Arial',10))
        self.setup.pack(pady=4)

        self.punchline = tk.Label(self.main_frame,font=('Arial',10))
        self.punchline.pack(pady=4)

    def fetch_joke(self):

        try:
            response = requests.get(f'{self.url+self.show_var.get()}')
            data = response.json()

            self.type.config(text=f'Type : {data['type']}')
            self.setup.config(text=f'SetUp : {data['setup']}')
            self.punchline.config(text=f'Punchline : {data['punchline']}')
            
        except Exception as e:
            print(e)

if __name__ == '__main__':
    app = RandomJoke()
    app.mainloop()