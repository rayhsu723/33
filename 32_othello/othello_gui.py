#Raymond Hsu 80042296
import tkinter
import game_logic

_DEFAULT_FONT = ('Consolas', 20)
class gui():
    def __init__(self, state: game_logic.Othello):
        self._state = state
        self._root_window = tkinter.Tk()

        self.draw_pieces(state)
    
        self._score = Score(state)
        
        # The game will automatically resize the pieces after every click. I know it is not ideal, but it was the best I could think of.
        
##        self._root_window.bind('<Configure>', self._on_resize)
        self._root_window.bind('<Button-1>', self._on_canvas_clicked)

    def draw_pieces(self, state: game_logic.Othello):
        '''Draws the state of the board'''
        for x in range(state.get_row()):
            for y in range(state.get_column()):
                canvas = tkinter.Canvas(master = self._root_window, width = 50, height = 50,
                                        borderwidth = 0, highlightthickness = 1,
                                        background = '#006000', highlightbackground = 'black')
                canvas.grid(row = x, column = y, padx = 0, pady = 0,
                            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
                
                if self._state.board[x][y] == 'B':
                    canvas.update()
                    canvas.create_oval(2, 2, canvas.winfo_width() - 2,
                                       canvas.winfo_height() - 2, fill = 'black',
                                       outline = 'black')
                elif self._state.board[x][y] == 'W':
                    canvas.update()
                    canvas.create_oval(2, 2, canvas.winfo_width() - 2,
                                       canvas.winfo_height() - 2, fill = 'white',
                                       outline = 'white')
                    
                self._root_window.rowconfigure(x, weight = 1)
                self._root_window.columnconfigure(y, weight = 1)

                    
    def start(self):
        self._root_window.mainloop()

    def _on_canvas_clicked(self, event: tkinter.Event):
        '''Updates the board after every click and updates the score as well.
           Will display winner if there are no more moves available'''
        try:
            grid_info = event.widget.grid_info()
            move = (int(grid_info['row']), int(grid_info['column']))
            self._state.make_a_move(move[0], move[1])
            self.draw_pieces(self._state)
            self._score.update_score()
        except:
            pass

#This class is for inputting the initial parameters of the game.
class Dialog:
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()

        #TITLE
        title_label = tkinter.Label(
            master = self._dialog_window, text = 'Othello',
            font = _DEFAULT_FONT)

        title_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        #ROWS
        row_label = tkinter.Label(
            master = self._dialog_window, text = '# of Rows: ',
            font = _DEFAULT_FONT)

        row_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._row_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = _DEFAULT_FONT)

        self._row_entry.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        #COLUMNS
        column_label = tkinter.Label(
            master = self._dialog_window, text = '# of Columns: ',
            font = _DEFAULT_FONT)

        column_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._column_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = _DEFAULT_FONT)

        self._column_entry.grid(
            row = 2, column = 1 , padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        #ARRANGEMENT
        arrangement_label = tkinter.Label(
            master = self._dialog_window, text = 'Arrangement (B or W): ',
            font = _DEFAULT_FONT)

        arrangement_label.grid(
            row = 3, column = 0 ,padx = 10, pady = 10,
            sticky = tkinter.W)

        self._arrangement_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = _DEFAULT_FONT)

        self._arrangement_entry.grid(
            row = 3, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        #WIN
        win_label = tkinter.Label(
            master = self._dialog_window, text = 'Win Condition (< or >): ',
            font = _DEFAULT_FONT)

        win_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._win_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = _DEFAULT_FONT)

        self._win_entry.grid(
            row = 4, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        #FIRST
        first_label = tkinter.Label(
            master = self._dialog_window, text = 'First (B or W): ',
            font = _DEFAULT_FONT)

        first_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._first_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = _DEFAULT_FONT)

        self._first_entry.grid(
            row = 5, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)


        #OK CANCEL
        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 6, column = 0, columnspan = 2, padx = 10, pady = 10)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = _DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0 ,column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = _DEFAULT_FONT,
            command = self._on_cancel_button)
        
        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        #for later use
        self._dialog_window.rowconfigure(6, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)

        self._ok_clicked = False
        self._row = ''
        self._column = ''
        self._arrangement = ''
        self._win = ''
        self._first = ''

    def show(self) -> None:
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def was_ok_clicked(self) -> bool:
        return self._ok_clicked

    def get_row(self) -> str:
        return self._row

    def get_column(self) -> str:
        return self._column

    def get_arrangement(self) -> str:
        return self._arrangement

    def get_win(self) -> str:
        return self._win

    def get_first(self) -> str:
        return self._first

    def _on_ok_button(self) -> None:
        self._ok_clicked = True
        try:
            self._row = int(self._row_entry.get())
            self._column = int(self._column_entry.get())
        except:
            pass
        self._arrangement = self._arrangement_entry.get()
        self._win = self._win_entry.get()
        self._first = self._first_entry.get()
        
        invalid = Invalid()
        
        if (int(self._row) < 4) or (int(self._row) > 16) or (int(self._row)%2 != 0):
            print('1')
            invalid.show()
        elif (int(self._column) < 4) or (int(self._column) > 16) or (int(self._column)%2 != 0):
            print('2')
            invalid.show()
        elif (self._arrangement != 'W') and (self._arrangement != 'B'):
            print('3')
            invalid.show()
        elif (self._win != '<') and (self._win != '>'):
            print('4')
            invalid.show()

        elif (self._first != 'W') and (self._first != 'B'):
            print('5')
            invalid.show()
            
        else:
            self._dialog_window.destroy()
            invalid._invalid_text.set('Game start')
            


    def _on_cancel_button(self) -> None:
        self._dialog_window.destroy()

#This class is for when there is an invalid input in the beginning dialog screen
class Invalid:
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()

        self._invalid_text = tkinter.StringVar()
        self._invalid_text.set('INVALID INPUT(S)')

        invalid_label = tkinter.Label(
            master= self._dialog_window, textvariable = self._invalid_text, font = _DEFAULT_FONT)
        invalid_label.pack()

    def show(self) -> None:
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

#This class if for displaying the score in a seperate window. Also displays winner when game is over.
class Score:
    def __init__(self, state: game_logic.Othello):
        self._dialog_window = tkinter.Toplevel()

        self._state = state
        
        self._score = tkinter.StringVar()
        self._score.set('White:2  Black:2  Turn:' + state.turn)

        self._score_label = tkinter.Label(
            master= self._dialog_window, textvariable = self._score, font = _DEFAULT_FONT)
        self._score_label.pack()

    def update_score(self):
        winner= self._state.determine_winner()
        if winner == 'B':
            self._score.set('Black wins!')
        elif winner == 'W':
            self._score.set('White wins!')
        elif winner == 'T':
            self._score.set('Tie game!')
        else:
            self._score.set('White:{}  Black:{}  Turn:{}'.format(self._state.get_score()[1],
                                                        self._state.get_score()[0], self._state.turn))


    def winner(self):
        winner = self._state.determine_winner()
        print(winner)
        if winner == 'B':
            self._score.set('Black wins!')
        elif winner== 'W':
            self._score.set('White wins!')
        elif winner == 'T':
            self._score.set('Tie game!')

    def show(self):
        self._dialog_window.grab_set()
                        
                        
    
        
        
if __name__ == '__main__':
    dialog = Dialog()
    dialog.show()
    stuff = game_logic.Othello(int(dialog._row),int(dialog._column), dialog._arrangement, dialog._win)
    
    stuff.determine_first(dialog._first)
    
    stuff.new_board()
    gui(stuff).start()
    

