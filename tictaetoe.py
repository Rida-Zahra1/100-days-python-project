import tkinter as tk

class TicTaeToe(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('TicTaeToe')
        self.resizable(0,0)
        self.menu()

        self.player_x = 'x'
        self.player_0 = 'o'
        self.curr = self.player_x
        self.game_over = False
        self.turn = 0

        self.board = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
        self.make_board()
        self.up()

    def menu(self):
        self.men = tk.Menu(self)
        self.config(menu=self.men)

        self.file = tk.Menu(self.men,tearoff=0)
        self.file.add_command(label='quit',command=self.quit)
        self.men.add_cascade(label='file',menu=self.file)

    def make_board(self):

        self.frame1 = tk.Frame(self)
        self.frame1.pack(fill = 'both',expand= True)

        self.label1 = tk.Label(self.frame1,text = f'{self.curr}\'s turn',font=('Consolas',30))
        self.label1.grid(row=0,column = 0,columnspan=3,sticky='ewns')

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                self.board[row][col] = tk.Button(self.frame1,text='',command=lambda row=row,col=col :self.set_tile(row,col),font=('Consolas',30),height=1,width=4)
                self.board[row][col].grid(row=row+1,column=col)

        self.restart = tk.Button(self.frame1,text='Restart',command=self.restart,font=('Consolas',30))
        self.restart.grid(row=4,column=0,columnspan=3,sticky='ewns')

    def up(self):
        self.update()
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        self.x = int((self.screen_width/2 ) - (self.width/2))
        self.y = int((self.screen_height/2 ) - (self.height/2))

        self.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')


    def set_tile(self,row,col):

        if self.game_over:
            return

        if self.board[row][col]['text'] != '':
            return
        
        self.board[row][col]['text'] = self.curr
        self.turn += 1

        if self.curr == self.player_0:
            self.curr = self.player_x
            self.label1.config(text=f'{self.curr}\'s turn')
        else:
            self.curr = self.player_0
            self.label1.config(text=f'{self.curr}\'s turn')

        self.check_winner()

    def check_winner(self):
        # for horiontal 
        for row in range(3):
            if self.board[row][0]['text'] == self.board[row][1]['text'] == self.board[row][2]['text'] and self.board[row][0]['text'] != '':
                self.label1.config(text=f'{self.board[row][0]['text']} is winner')

                for col in range(3):
                    self.board[row][col].config(bg='gray')

                self.game_over = True
                return
            
        # for vertical
        for col in range(3):
            if self.board[0][col]['text'] == self.board[1][col]['text'] == self.board[2][col]['text'] and self.board[0][col]['text'] != '':
                self.label1.config(text=f'{self.board[0][col]['text']} is winner')

                for row in range(3):
                    self.board[row][col].config(bg='gray')

                self.game_over = True
                return
            
        # for diagonal
        if self.board[0][0]['text'] == self.board[1][1]['text'] == self.board[2][2]['text'] and self.board[0][0]['text'] != '':
            self.label1.config(text=f'{self.board[0][0]['text']} is winner')

            self.board[0][0].config(bg='gray')
            self.board[1][1].config(bg='gray')
            self.board[2][2].config(bg='gray')
        
            self.game_over = True
            return
    
        if self.board[0][2]['text'] == self.board[1][1]['text'] == self.board[2][0]['text'] and self.board[0][2]['text'] != '':
            self.label1.config(text=f'{self.board[0][2]['text']} is winner')

            self.board[0][2].config(bg='gray')
            self.board[1][1].config(bg='gray')
            self.board[2][0].config(bg='gray')

            self.game_over = True
            return
        
        if self.turn == 9:
            self.label1.config(text='Tie')
            self.game_over = True
            return
        
    def restart(self):
        self.curr = self.player_x
        self.turn = 0
        self.game_over = False
        
        for row in range(3):
            for col in range(3):
                self.board[row][col].config(text='',bg='white')
        self.label1.config(text=f'{self.curr}\'s turn')
    

if __name__ == '__main__':
    app = TicTaeToe()
    app.mainloop()
