import requests
import tkinter as tk
from tkinter import ttk

class WeatherApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Weather App')
        self.geometry('300x300')
        self.resizable(0,0)
        self.pakistan_cities = [
                                "Islamabad", "Karachi", "Lahore", "Faisalabad", "Rawalpindi", 
                                "Peshawar", "Quetta", "Multan", "Hyderabad", "Sialkot",
                                "Gujranwala", "Bahawalpur", "Sargodha", "Sukkur", "Larkana",
                                "Sheikhupura", "Jhelum", "Abbottabad", "Gujrat", "Mardan"
                            ]

        self.frame()

    def frame(self):

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(padx=10,pady=10,fill='both',expand=True)
        self.main_frame.rowconfigure((0,1,2,3,4,5,6),weight=1)
        self.main_frame.columnconfigure((0,1),weight=1)
        tk.Label(self.main_frame,text='Welcome',font=('Consoals',15)).grid(row=0,column=0,columnspan=2,pady=5,padx=5)

        self.combobox_var = tk.StringVar()
        ttk.Combobox(self.main_frame,font=('Arial',10),values=self.pakistan_cities,textvariable=self.combobox_var).grid(row=1,column=1,sticky='w',padx=5,pady=5)
        tk.Label(self.main_frame,text='CIty :  ',font=('Arial',10)).grid(row=1,column=0,sticky='e',pady=5,padx=5)

        tk.Button(self.main_frame,text='Enter',font=('Arial',10),command=self.answer_api,bg='red',fg='white').grid(row=2,pady=5,column=1,ipadx=5)

        self.country = tk.Label(self.main_frame, font=('Arial', 10), text='', anchor="w")
        self.country.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5)

        self.city = tk.Label(self.main_frame, font=('Arial', 10), text='', anchor="w")
        self.city.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5)

        self.temp_c = tk.Label(self.main_frame, font=('Arial', 10), text='', anchor="w")
        self.temp_c.grid(row=5, column=0, columnspan=2, sticky="ew", padx=5)

        self.condition = tk.Label(self.main_frame, font=('Arial', 10), text='', anchor="w")
        self.condition.grid(row=6, column=0, columnspan=2, sticky="ew", padx=5)

    def answer_api(self):

        location = self.combobox_var.get()
        api_key = "d71033db50d54e87afd93157253101" 
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"

        response = requests.get(url) 
        try:
            data = response.json()
            if 'error' in data:
                self.country.config(text="Invalid city or API limit reached")
                return

        
            self.country.config(text=f"Country : {data['location']['country']}")
            self.city.config(text=f"City : {data['location']['region']}")
            self.temp_c.config(text=f"Temperture : {data['current']['temp_c']}")
            self.condition.config(text=f"Condition : {data['current']['condition']['text']}")

        except Exception as e:
            self.country.config(text=f"Error: {str(e)}")

if __name__ == '__main__':
    app = WeatherApp()
    app.mainloop()

            






