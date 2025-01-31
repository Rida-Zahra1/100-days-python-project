import tkinter as tk
from tkinter import ttk



class CurrencyConverter(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('400x300')
        self.resizable(0,0)
        self.title('Currency Converter')
        self.country = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF',
                        'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 
                        'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']
        self.frame()

    def frame(self):
        print('hi')
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill='both',expand= True)

        self.label_frame = tk.LabelFrame(self.main_frame,font=('Arial',15),bg='black',text='Currency Converter',width=80)
        self.label_frame.grid(row=0,column=0,padx=15,pady=15,)

        tk.Label(self.label_frame,text='Welcome to Currency converter',font=('Consolas',15)).grid(row=0,column=0,columnspan=2,padx=20,pady=5,sticky='ew')
        tk.Label(self.label_frame,text='From_Currency : ',font=('Arial',11)).grid(row=1,column=0,pady=5)

        self.from_curr_var = tk.StringVar() 
        self.combobox = ttk.Combobox(self.label_frame,textvariable= self.from_curr_var,value=self.country,width=20)
        self.combobox.grid(row=1,column=1,pady=5)

        tk.Label(self.label_frame,text='To_Currency : ',font=('Arial',11)).grid(row=2,column=0,pady=5)

        self.to_curr_var = tk.StringVar() 
        self.combobox2 = ttk.Combobox(self.label_frame,textvariable= self.to_curr_var,value=self.country,width=20)
        self.combobox2.grid(row=2,column=1,pady=5)

        tk.Label(self.label_frame,text='Amount : ',font=('Arial',11)).grid(row=3,column=0,pady=10)
        self.enter = tk.Entry(self.label_frame,)
        self.enter.grid(row=3,column=1,pady=10)

        tk.Button(self.label_frame,text='Enter',command=self.calculate,font=('Arial',10),fg='black',bg='white').grid(row=4,column=1,ipadx=10)

        self.answer = tk.Label(self.label_frame,font=('Arial',11))
        self.answer.grid(row=5,column=0,columnspan=2,pady=10)

    def calculate(self):
        
        rates = {'AUD': 1.6020701757,'BGN': 1.8718502913, 'BRL': 5.8660406146, 'CAD': 1.4393202607, 
                'CHF': 0.9060200954, 'CNY': 7.2333410044, 'CZK': 24.0735841713, 'DKK': 7.1558607965, 
                'EUR': 0.9588901064, 'GBP': 0.8027200827, 'HKD': 7.7880314673, 'HRK': 6.7954410736, 
                'HUF': 390.971019503,'IDR': 16119.078239504, 'ILS': 3.6106605272, 'INR': 86.3994808634, 
                'ISK': 139.580679686, 'JPY': 155.1310271297, 'KRW': 1440.2615663697, 'MXN': 20.5162331361, 
                'MYR': 4.3828504773, 'NOK': 11.2772921872, 'NZD': 1.7647003444, 'PHP': 58.4102200429, 
                'PLN': 4.0283406807, 'RON': 4.7700006215, 'RUB': 99.1667882255, 'SEK': 10.9904021633, 
                'SGD': 1.3483901572, 'THB': 33.7192641471, 'TRY': 35.7861960472, 'USD': 1, 'ZAR': 18.534232148}
        
        too = self.to_curr_var.get()
        from_ = self.from_curr_var.get()
        amount = self.enter.get()

        if too and from_ and amount:
            try:
                amount = float(amount)
                if too == from_:
                    self.answer.config(text='From and use currrencies cant be same')
                to_curr = rates.get(too)
                from_curr = rates.get(from_)
                if to_curr and from_curr:
                    converted_amount = (amount / from_curr) * to_curr
                    self.answer.config(text=f'{amount} {from_} = {converted_amount:.2f} {too}')
                else:
                        self.answer.config(text="Invalid currency")
            except ValueError:
                self.answer.config(text="Please enter a valid amount.")
        else:
            self.answer.config(text="Please select currencies and enter an amount.") 









if __name__ == '__main__':
    app = CurrencyConverter()
    app.mainloop()
