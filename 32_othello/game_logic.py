#This file will be imported by the file othello_gui.py. Put in the same folder as othello_gui.py in order for othello_gui.py to work
class Othello:
    def __init__(self, row, column, arrangement, win_condition):
        self._column = column
        self._row = row
        self._arrangement = arrangement
        self._win_condition = win_condition
        self.board = []
        self.turn = 'W'

    def get_row(self):
        return self._row

    def get_column(self):
        return self._column

    def print_board(self) -> None:
        for row in range(self._row):
            for col in range(self._column):
                if self.board[row][col] == '.':
                    print('.', end = '  ')
                elif self.board[row][col] == 'B':
                    print('B', end = '  ')
                elif self.board[row][col] == 'W':
                    print('W', end = '  ')
            print()


    def new_board(self) -> list:
        '''Creates a new, starting board'''
        for i in range(self._row):
            self.board.append(['.'] * self._column)
            middle_row = int((self._row/2)-1)
            middle_column = int((self._column/2)-1)
        if self._arrangement == 'B':
            self.board[middle_row][middle_column] = 'B'
            self.board[middle_row][middle_column + 1] = 'W'
            self.board[middle_row + 1][middle_column] = 'W'
            self.board[middle_row + 1][middle_column + 1] = 'B'
        elif self._arrangement == 'W':
            self.board[middle_row][middle_column] = 'W'
            self.board[middle_row][middle_column + 1] = 'B'
            self.board[middle_row + 1][middle_column] ='B'
            self.board[middle_row + 1][middle_column + 1] = 'W'
            
    def on_board(self, r, c):
        '''Checks to see if tile is on the board'''
        return r >= 0 and r <= self._row and c >= 0 and c <= self._column

    def is_valid_move(self, r, c):
        if self.board[r][c] != '.' or not self.on_board(r, c): # check to see if move is valid
            return False

        self.board[r][c] = self.turn #place piece on board

        if self.turn == 'B':
            opposite = 'W'
        else:
            opposite = 'B'

        tiles_to_flip = []
        for left_right, up_down in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            try:# all possible directions
                x, y = r, c
                x += left_right
                y += up_down
                if self.on_board(x,y) and self.board[x][y] == opposite:
                    x += left_right
                    y += up_down
                    if not self.on_board(x,y):
                        continue
                    while self.board[x][y] == opposite:
                        x += left_right
                        y += up_down
                        if not self.on_board(x,y):
                            break
                    if not self.on_board(x, y):
                        continue
                    if self.board[x][y] == self.turn:
                        while True:
                            x -= left_right
                            y -= up_down
                            if x == r and y == c:
                                break
                            tiles_to_flip.append([x, y])
            except:
                continue
        self.board[r][c] = '.'
        if len(tiles_to_flip) == 0:#if there was nothing to flip, then the move is invalid and return false
            return False
        return tiles_to_flip

    def possible_moves(self)->list:
        '''Return a list of possible next moves. If there are no possible next moves, return an empty list'''
        moves = []
        for r in range(self._row):
            for c in range(self._column):
                if self.is_valid_move(r,c) != False:
                    moves.append([r,c])
        return moves

    def make_a_move(self, row: int, col: int):
        if self.is_valid_move(row, col) != False:
            tiles_to_flip = self.is_valid_move(row,col)
            for x in tiles_to_flip:
                self.board[x[0]][x[1]] = self.turn
            self.board[row][col] = self.turn
            self.switch_turn()
        else:
            pass

    def switch_turn(self):
        '''Switches the turn'''
        if self.turn == 'W':
            self.turn = 'B'
        elif self.turn == 'B':
            self.turn = 'W'

    def get_score(self):
        black_score = 0
        white_score = 0
        for x in self.board:
            for y in x:
                if y == 'B':
                    black_score += 1
                elif y == 'W':
                    white_score += 1
        return (black_score, white_score)

    def determine_first(self, first: str):
        if first == 'B':
            self.turn = 'B'
        elif first == 'W':
            self.turn = 'B'

    def determine_winner(self):
        moves = self.possible_moves()
        black_count = 0
        white_count = 0
        if len(moves) == 0:
            for x in self.board:
                for y in x:
                    if y == 'B':
                        black_count += 1
                    elif y == 'W':
                        white_count += 1
            if self._win_condition == '>':
                if black_count > white_count:
                    return 'B'
                elif white_count > black_count:
                    return 'W'
                elif white_count == black_count:
                    return 'T'
            elif self._win_condition == '<':
                if black_count < white_count:
                    return 'B'
                elif white_count < black_count:
                    return 'W'
                elif white_count == black_count:
                    return 'T'
        else:
            return None
                
