import tkinter as tk
import tkinter.messagebox as showinfo
import json

class Data:
    file_name = 'movie_data_base.json'

    @staticmethod
    def load_data():
        try:
            with open(Data.file_name,'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    @staticmethod
    def save_data(data_base):
        with open(Data.file_name,'w') as file:
            return json.dump(data_base,file,indent=4)

    @staticmethod
    def add_data():

        movies_name = [
            'The Ten Commandments (1956)',
            'Ben-Hur (1959)',
            'The Passion of the Christ (2004)',
            'The Gospel According to St. Matthew (1964)',
            'The Prince of Egypt (1998):'
            ]
        
        movies_data = Data.load_data()

        for name in movies_name:
            if name not in movies_data:
                movies_data[name] = {'seat':5}

        Data.save_data(movies_data)


class MovieTicket(tk.Tk):

    ticket_number = 1

    def __init__(self):
        super().__init__()

        self.title('Movie Ticket Reservation')
        self.config(bg='black')
        self.geometry('400x500')
        self.resizable(0, 0)
        Data.add_data()
        self.data_base = Data.load_data()
        self.frame()

    def frame(self):

        self.main_frame = tk.Frame(self, bg='black', padx=20, pady=20)
        self.main_frame.pack(fill='both', expand=True, padx=5, pady=5)

        tk.Label(
            self.main_frame, text='Welcome to Cinema', font=('Helvetica', 18, 'bold'), fg='white', bg='black'
        ).pack(fill='x', pady=5)

        tk.Label(
            self.main_frame, text='Movies List', font=('Helvetica', 16, 'bold'), fg='white', bg='black'
        ).pack(fill='x', pady=5)

        # Adding a frame for the movie buttons to give them structure
        button_frame = tk.Frame(self.main_frame, bg='black')
        button_frame.pack(fill='x', pady=5)

        for name in self.data_base:
            movie_button = tk.Button(
                button_frame, text=name, font=('Helvetica', 12), command=lambda movie=name: self.show_movie_details(movie),
                fg='black', bg='#f8f8f8', width=30, height=2, relief='solid', bd=1
            )
            movie_button.pack(pady=3, padx=3, fill='x')

    def show_movie_details(self, movie):

        # Destroy the previous frame
        self.main_frame.destroy()
        
        # Create a new frame for movie details
        self.movie_frame = tk.Frame(self, bg='black')
        self.movie_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Configure grid rows and columns for responsive layout
        self.movie_frame.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.movie_frame.columnconfigure(0, weight=1)
        self.movie_frame.columnconfigure(1, weight=3)

        self.movie_name = movie

        for name in self.data_base:
            if self.movie_name == name:
                # Title label
                tk.Label(
                    self.movie_frame, text='You can book your seat now!', font=('Helvetica', 18, 'bold'), fg='white', bg='black'
                ).grid(row=0, column=0, columnspan=2, pady=15)

                # Movie Name
                tk.Label(
                    self.movie_frame, text='Movie Name:', font=('Helvetica', 12, 'bold'), fg='white', bg='black'
                ).grid(row=1, column=0, padx=5, sticky='e')

                tk.Label(
                    self.movie_frame, text=f'{name}', font=('Helvetica', 12), fg='white', bg='black'
                ).grid(row=1, column=1, padx=5)

                # Seats Available
                tk.Label(
                    self.movie_frame, text='Seats Available:', font=('Helvetica', 12, 'bold'), fg='white', bg='black'
                ).grid(row=2, column=0, padx=5, sticky='e')

                self.seat = tk.StringVar(value=f"{self.data_base[name]['seat']}")
                tk.Label(
                    self.movie_frame,textvariable=self.seat,text=f"{self.data_base[name]['seat']}", font=('Helvetica', 12), fg='white', bg='black'
                ).grid(row=2, column=1, padx=5)

                # Ticket Entry Section
                tk.Label(
                    self.movie_frame, text='Tickets to Book:', font=('Helvetica', 12, 'bold'), fg='white', bg='black'
                ).grid(row=3, column=0, padx=5, sticky='e')

                self.ticket_var = tk.IntVar()

                if self.data_base[self.movie_name]['seat'] > 0:

                    tk.Entry(
                        self.movie_frame, textvariable=self.ticket_var, font=('Helvetica', 12), fg='black', bg='white'
                    ).grid(row=3, column=1, padx=5)

                    # Name Entry Section
                    tk.Label(
                        self.movie_frame, text='Your Name:', font=('Helvetica', 12, 'bold'), fg='white', bg='black'
                    ).grid(row=4, column=0, padx=5, sticky='e')

                    self.name_var = tk.StringVar()
                    tk.Entry(
                        self.movie_frame, textvariable=self.name_var, font=('Helvetica', 12), fg='black', bg='white'
                    ).grid(row=4, column=1, padx=5)

                    # Buttons: Enter and Back
                    tk.Button(
                        self.movie_frame, text='Book Ticket', command=self.user_movie_ticket, bg='#4CAF50', fg='white', font=('Helvetica', 12), width=15, relief='solid', bd=1
                    ).grid(row=5, column=0, padx=5, pady=15)

                    tk.Button(
                        self.movie_frame, text='Back', command=self.return_back, bg='#f44336', fg='white', font=('Helvetica', 12), width=15, relief='solid', bd=1
                    ).grid(row=5, column=1, padx=5)

                    # Ticket Information Display
                    if not hasattr(self, 'text'):
                        self.text = tk.Text(self.movie_frame, state='disabled', height=5, width=40, bg='white', fg='black', font=('Helvetica', 12))
                        self.text.grid(row=6, column=0, columnspan=2, padx=5, pady=10)
                
                else:
                    tk.Entry(
                        self.movie_frame, text='House Full', font=('Helvetica', 12), fg='black', bg='white', state='readonly'
                    ).grid(row=3, column=1, padx=5)

                    tk.Button(
                        self.movie_frame, text='Back', command=self.return_back, bg='#f44336', fg='white', font=('Helvetica', 12), width=15, relief='solid', bd=1
                    ).grid(row=4, column=1, padx=5, pady=10)


    def return_back(self):
        self.movie_frame.destroy()
        self.frame()

    def user_movie_ticket(self):
        movie_name = self.movie_name
        user_name = self.name_var.get()
        ticket = self.ticket_var.get()

        if not user_name or ticket <= 0:
            showinfo.showerror("Error", "Please enter valid details (Name and Ticket count must be positive)")
            return

        if user_name and ticket > 0:
            if self.data_base[movie_name]['seat'] >= ticket:
                if 'audience_info' not in self.data_base[movie_name]:
                    self.data_base[movie_name]['audience_info'] = []

                self.data_base[movie_name]['audience_info'].append({
                    'name': user_name,
                    'ticket_obtained': ticket
                })

                self.data_base[movie_name]['seat'] -= ticket
                Data.save_data(self.data_base)
                self.seat.set(f'{self.data_base[movie_name]['seat']}')
                self.text.config(state='normal')
                self.text.delete('1.0', tk.END)
                self.text.insert('end', f"Name : {user_name}\nMovie_Name : {movie_name}\nticket : {MovieTicket.ticket_number}")
                self.text.config(state='disabled')
                self.ticket_var.set('')
                self.name_var.set('')
                MovieTicket.ticket_number += 1
            else:
                showinfo.showerror("Error", "Not enough seats available")
        else:
            showinfo.showerror("Error", "Enter valid details")

        print(self.data_base)


if __name__ == '__main__':
    app = MovieTicket()
    app.mainloop()
