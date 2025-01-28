import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator App')
        self.curr_exp = ''
        self.frame_()

    def frame_(self):
        self.frame1 = tk.Frame(self)
        self.frame1.pack(fill='both', expand=True)

        self.label1 = tk.Label(self.frame1, text='', font=('Consolas', 20), height=1, relief='sunken', justify='left', bg='black', fg='white')
        self.label1.grid(row=0, column=0, columnspan=4, sticky='ew')

        self.butons = [('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
                       ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
                       ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
                       ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3)]

        for text, row, col in self.butons:
            self.buton = tk.Button(self.frame1, command=lambda t=text: self.on_click(t), text=text, font=('Consolas', 30), height=1, width=3, bg='black', fg='white')
            self.buton.grid(row=row, column=col, sticky='ewns')

    def on_click(self, char):
        if char == 'C':
            self.label1.config(text='')
            self.curr_exp = ''
        elif char == '=':
            try:
                result = eval(self.curr_exp)
                self.label1.config(text=result)
                self.curr_exp = str(result)
            except Exception as e:
                self.label1.config(text='invalid input')
        else:
            self.curr_exp += str(char)
            self.label1.config(text=self.curr_exp)

if __name__ == '__main__':
    app = Calculator()
    app.mainloop()
