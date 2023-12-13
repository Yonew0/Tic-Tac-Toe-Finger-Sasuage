import tkinter.messagebox
from tkinter import *
#TODO change import method, to from tkinter import module

#Constants
CANVAS_SIZE = 600
FIGURE_SIZE = 200
RATIO = CANVAS_SIZE // FIGURE_SIZE
BG_COLOR = 'black'
EMPTY = None

#Players setup
X = 'player 1'
O = 'player 2'
FIRST_PLAYER = X

class Board(Tk) :
    def __init__(self, start_player):
        super().__init__()
        self.title("Tic-tac")
        self.canvas = Canvas(height=CANVAS_SIZE, width=CANVAS_SIZE, bg=BG_COLOR)
        self.canvas.pack()
        self.figure_size = FIGURE_SIZE
        self.current_player = start_player
        self.canvas.bind('<Button-1>', self.click_event)
        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]

    def build_grid(self, color):
        x = CANVAS_SIZE // RATIO
        y1 = 0
        y2 = CANVAS_SIZE
        self.canvas.create_line(x, y1, x, y2, fill=color)
        self.canvas.create_line(x*2, y1, x*2, y2, fill=color)
        self.canvas.create_line(y1, x, y2, x, fill=color)
        self.canvas.create_line(y1, x * 2, y2, x * 2, fill=color)
    def render_cross(self, cords: list):
        f_size = self.figure_size
        self.canvas.create_line(cords[0], cords[1], cords[0] + f_size, cords[1] + f_size, fill='red', width=5)
        self.canvas.create_line(cords[0] + f_size, cords[1], cords[0], cords[1] + f_size, fill='red', width=5)
    def render_circle(self, posX, posY):
        f_size = self.figure_size
        self.canvas.create_oval(posX + 5, posY + 5, posX + f_size, posY + f_size, outline='blue', width=5)

    def check_winner(self, board, player):
        for y in range(3):
            if board[y] == [player, player, player]:
                return True
        for x in range(3):
            if board[0][x] == board[1][x] == board[2][x] == player :
                return True
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player :
            return True

        return False

    def check_draw(self, board):
        for row in board:
            if EMPTY in row:
                return False
            return True

    def change_player(self):
        if self.current_player == X:
            self.current_player = O
        else:
            self.current_player = X
    def winner(self, player=None):
        """display game end text."""
        center = CANVAS_SIZE // 2
        if player :
            text = f'Winner: {player}'
        else:
            text = 'Draw'
        self.canvas.create_text(center, center, text=text, fill='white', font='System 50')
        self.canvas.unbind('<Button-1>')

    def update_board(self, x, y):
        c_player = self.current_player
        self.board[x][y] = c_player
        if self.check_winner(self.board, c_player):
            self.winner(c_player)
        elif self.check_draw(self.board):
            self.winner()

    def make_move(self, x, y):
        position = {0: 0, 1: 200, 2: 400}
        current_player = self.current_player

        if self.board[x][y] == EMPTY :
             self.update_board(x, y)
             self.change_player()

             if current_player == X:
                 self.render_cross([position[x], position[y]])
             elif current_player == O :
                 self.render_circle(position[x], position[y])

    def click_event(self, event):
        x_coord = event.x // FIGURE_SIZE
        y_coord = event.y // FIGURE_SIZE
        self.make_move(x_coord, y_coord)

#Initialize game object and execute require methods
game_v1 = Board(start_player=FIRST_PLAYER)
game_v1.build_grid('white')

#Testing
#game_v1.render_cross([0,0])
#game_v1.render_circle(0, 0)
#game_v1.winner()

#Run the game
game_v1.mainloop()