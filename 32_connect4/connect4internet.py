### connectfour.py
###
### ICS 32 Spring 2015
### Project #2: Send Me On My Way
##
##'''
##This module contains the game logic that underlies a Connect Four
##game, implementing such functionality as tracking the state of a game,
##updating that state as players make moves, and determining if there is a
##winner.  No user interface or network functionality is included; this is
##strictly a collection of tools for implementing the game logic.
##'''
##
##import collections
##import socket
##
### These constants specify the concepts of "no player", the "red player"
### and the "yellow player".  Your code should use these constants in
### place of their hard-coded values.  Note that these values are not
### intended to be displayed to a user; they're simply intended as a
### universal way to distinguish which player we're talking about (e.g.,
### which player's turn it is, or which player (if any) has a piece in a
### particular cell on the board).
##
##NONE = '.'
##RED = 'R'
##YELLOW = 'Y'
##
##
### These constants specify the size of the game board (i.e., the number
### of rows and columns it has).  It should be possible to change these
### constants and re-run your program so that the board will have a
### different size; be sure that you're not hard-coding these values
### anywhere in your own code, because this is something we'll be
### attempting when we test your program.
##
##BOARD_COLUMNS = 7
##BOARD_ROWS = 6
##
##
### ConnectFourGameState is a namedtuple that tracks everything important
### about the state of a Connect Four game as it progresses.  It contains
### two fields:
###
###     'board', which is a two-dimensional list of strings describing
###     the game board.  Each string represents one cell on the board
###     and is either NONE, RED, or YELLOW, depending on whether the
###     cell contains a red piece, a yellow piece, or is empty
###
###     'turn', which specifies which player will make the next move;
###     its value will always be either RED or YELLOW
##
##ConnectFourGameState = collections.namedtuple('ConnectFourGameState', ['board', 'turn'])
##
##
##
### This is the simplest example of how you create new kinds of exceptions
### that are specific to your own program.  We'll see later in the quarter
### in more detail what this notation means; in short, we're introducing
### new types into our program and stating that they have strong similarities
### to the existing type called Exception.
##
##
##class InvalidMoveError(Exception):
##    '''Raised whenever an invalid move is made'''
##    pass
##
##
##class GameOverError(Exception):
##    '''
##    Raised whenever an attempt is made to make a move after the game is
##    already over
##    '''
##    pass
##
##
##
##
### The next four functions are the "public" functions that are provided
### by this module.  You'll need to call all four of these functions, but
### will not need (or want) to call any of the others.
##
##
##
##def new_game_state() -> ConnectFourGameState:
##    '''
##    Returns a ConnectFourGameState representing a brand new game
##    in which no moves have been made yet.
##    '''
##    return ConnectFourGameState(board = _new_game_board(), turn = RED)
##
##
##
##def drop_piece(game_state: ConnectFourGameState, column_number: int) -> ConnectFourGameState:
##    '''
##    Given a game state and a column number, returns the game state
##    that results when the current player (whose turn it is) drops a piece
##    into the given column.  If the column number is invalid, a ValueError
##    is raised.  If the game is over, a GameOverError is raised.  If a move
##    cannot be made in the given column because the column is filled already,
##    an InvalidMoveError is raised.
##    '''
##    _require_valid_column_number(column_number)
##    _require_game_not_over(game_state)
##
##    empty_row = _find_bottom_empty_row_in_column(game_state.board, column_number)
##
##    if empty_row == -1:
##        raise InvalidMoveError()
##
##    else:
##        new_board = _copy_game_board(game_state.board)
##        new_board[column_number][empty_row] = game_state.turn
##        new_turn = _opposite_turn(game_state.turn)
##        return ConnectFourGameState(board = new_board, turn = new_turn)
##
##
##
##def pop_piece(game_state: ConnectFourGameState, column_number: int) -> ConnectFourGameState:
##    '''
##    Given a game state and a column number, returns the game state that
##    results when the current player (whose turn it is) pops a piece from the
##    bottom of the given column.  If the column number is invalid, a ValueError
##    is raised.  If the game is over, a GameOverError is raised.  If a piece
##    cannot be popped from the bottom of the given column because the column
##    is empty or because the piece at the bottom of the column belongs to the
##    other player, an InvalidMoveError is raised.
##    '''
##    _require_valid_column_number(column_number)
##    _require_game_not_over(game_state)
##
##    if game_state.turn == game_state.board[column_number][BOARD_ROWS - 1]:
##        new_board = _copy_game_board(game_state.board)
##
##        for row in range(BOARD_ROWS - 1, -1, -1):
##            new_board[column_number][row] = new_board[column_number][row - 1]
##
##        new_board[column_number][row] = NONE
##
##        new_turn = _opposite_turn(game_state.turn)
##
##        return ConnectFourGameState(board = new_board, turn = new_turn)
##
##    else:
##        raise InvalidMoveError()
##
##
##
##def winning_player(game_state: ConnectFourGameState) -> str:
##    '''
##    Determines the winning player in the given game state, if any.
##    If the red player has won, RED is returned; if the yellow player
##    has won, YELLOW is returned; if no player has won yet, NONE is
##    returned.
##    '''
##    winner = NONE
##    
##    for col in range(BOARD_COLUMNS):
##        for row in range(BOARD_ROWS):
##            if _winning_sequence_begins_at(game_state.board, col, row):
##                if winner == NONE:
##                    winner = game_state.board[col][row]
##                elif winner != game_state.board[col][row]:
##                    # This handles the rare case of popping a piece
##                    # causing both players to have four in a row;
##                    # in that case, the last player to make a move
##                    # is the winner.
##                    return _opposite_turn(game_state.turn)
##
##    return winner
##    
##
##
##
### Modules often contain functions, variables, or classes whose names begin
### with underscores.  This is no accident; in Python, this is the agreed-upon
### standard for specifying functions, variables, or classes that should be
### treated as "private" or "hidden".  The rest of your program should not
### need to call any of these functions directly; they are utility functions
### called by the functions above, so that those functions can be shorter,
### simpler, and more readable.
##
##
##
##def _new_game_board() -> [[str]]:
##    '''
##    Creates a new game board.  Initially, a game board has the size
##    BOARD_COLUMNS x BOARD_ROWS and is comprised only of strings with the
##    value NONE
##    '''
##    board = []
##
##    for col in range(BOARD_COLUMNS):
##        board.append([])
##        for row in range(BOARD_ROWS):
##            board[-1].append(NONE)
##
##    return board
##
##
##
##def _copy_game_board(board: [[str]]) -> [[str]]:
##    '''Copies the given game board'''
##    board_copy = []
##
##    for col in range(BOARD_COLUMNS):
##        board_copy.append([])
##        for row in range(BOARD_ROWS):
##            board_copy[-1].append(board[col][row])
##
##    return board_copy
##
##
##
##def _find_bottom_empty_row_in_column(board: [[str]], column_number: int) -> int:
##    '''
##    Determines the bottommost empty row within a given column, useful
##    when dropping a piece; if the entire column in filled with pieces,
##    this function returns -1
##    '''
##    for i in range(BOARD_ROWS - 1, -1, -1):
##        if board[column_number][i] == NONE:
##            return i
##
##    return -1
##
##
##
##def _opposite_turn(turn: str) -> str:
##    '''Given the player whose turn it is now, returns the opposite player'''
##    if turn == RED:
##        return YELLOW
##    else:
##        return RED
##
##
##
##def _winning_sequence_begins_at(board: [[str]], col: int, row: int) -> bool:
##    '''
##    Returns True if a winning sequence of pieces appears on the board
##    beginning in the given column and row and extending in any of the
##    eight possible directions; returns False otherwise
##    '''
##    return _four_in_a_row(board, col, row, 0, 1) \
##            or _four_in_a_row(board, col, row, 1, 1) \
##            or _four_in_a_row(board, col, row, 1, 0) \
##            or _four_in_a_row(board, col, row, 1, -1) \
##            or _four_in_a_row(board, col, row, 0, -1) \
##            or _four_in_a_row(board, col, row, -1, -1) \
##            or _four_in_a_row(board, col, row, -1, 0) \
##            or _four_in_a_row(board, col, row, -1, 1)
##    
##
##
##def _four_in_a_row(board: [[str]], col: int, row: int, coldelta: int, rowdelta: int) -> bool:
##    '''
##    Returns True if a winning sequence of pieces appears on the board
##    beginning in the given column and row and extending in a direction
##    specified by the coldelta and rowdelta
##    '''
##    start_cell = board[col][row]
##
##    if start_cell == NONE:
##        return False
##    else:
##        for i in range(1, 4):
##            if not _is_valid_column_number(col + coldelta * i) \
##                    or not _is_valid_row_number(row + rowdelta * i) \
##                    or board[col + coldelta *i][row + rowdelta * i] != start_cell:
##                return False
##        return True
##    
##
##
##def _require_valid_column_number(column_number: int) -> None:
##    '''Raises a ValueError if its parameter is not a valid column number'''
##    if type(column_number) != int or not _is_valid_column_number(column_number):
##        raise ValueError('column_number must be int between 0 and {}'.format(BOARD_COLUMNS - 1))
##
##
##
##def _require_game_not_over(game_state: ConnectFourGameState) -> None:
##    '''
##    Raises a GameOverError if the given game state represents a situation
##    where the game is over (i.e., there is a winning player)
##    '''
##    if winning_player(game_state) != NONE:
##        raise GameOverError()
##
##
##
##def _is_valid_column_number(column_number: int) -> bool:
##    '''Returns True if the given column number is valid; returns False otherwise'''
##    return 0 <= column_number < BOARD_COLUMNS
##
##
##
##def _is_valid_row_number(row_number: int) -> bool:
##    '''Returns True if the given row number is valid; returns False otherwise'''
##    return 0 <= row_number < BOARD_ROWS





import socket
import connectfour
import collections
ConnectFourGameState = collections.namedtuple('ConnectFourGameState', ['board', 'turn'])
game_start = connectfour.new_game_state()




def print_board(game: ConnectFourGameState) -> None:
    """ Prints the board"""
    print('1  2  3  4  5  6  7')
    for row in range(connectfour.BOARD_ROWS):
        for col in range(connectfour.BOARD_COLUMNS):
            if game.board[col][row] == 0:
                print('.', end = '  ')
            elif game.board[col][row] == 1:
                print('R', end = '  ')
            elif game.board[col][row] == 2:
                print('Y', end = '  ')
        print()

def user_input(game: ConnectFourGameState) -> ConnectFourGameState:
    """Handles the user input"""
    while True:
        if game.turn == 1:
            print("RED'S TURN")
        else:
            print("YELLOW'S TURN")
        print_board(game)
        user_command = input('Input DROP col# or POP col# (ex. DROP 1): ')
        user_command2 = user_command.split()
        if user_command2[0] == 'DROP':
            if int(user_command2[1]) not in range(1, 8):
                print('Not a valid column')
                
            else:
                try:
                    return(connectfour.drop_piece(game, int(user_command2[1])-1))
                except:
                    print('Column is full')
                    
        elif user_command2[0] == 'POP':
            if int(user_command2[1]) not in range(1, 8):
                print('Not a valid column')
                
            else:
                try:
                    return(connectfourpop_piece(game, int(user_command2[1])-1))
                except:
                    print('Invalid column')
                    
        else:
            print('Not a valid command')
        




    








connect4connection = collections.namedtuple( 'connect4connection', 'socket input output')

def read_host() -> str:
    """ Prompts for host"""
    while True:
        host = input('Host: ').strip()

        if len(host) == 0:
            print('Please specift a host (either a name or an IP address)')
        else:
            return host
        
def read_port() -> int:
    """ Prompts for port number"""
    while True:
        try:
            port = int(input('Port: ').strip())

            if port < 0 or port > 65535:
                print('Ports must be an integer between 0 and 65535')
            else:
                return port

        except ValueError:
            print('Ports must be an integer between 0 and 65535')

        
def connect(host: str, port: int) -> connect4connection:
    """Connects to the socket"""
    connect4_socket = socket.socket()

    connect4_socket.connect((host, port))

    connect4_input = connect4_socket.makefile('r')
    connect4_output = connect4_socket.makefile('w')

    return connect4connection(connect4_socket, connect4_input, connect4_output)
    
def close_socket(connection: connect4connection) -> None:
    """Closes the socket"""
    connection.input.close()
    connection.output.close()
    connection.socket.close()
    print('Connection closed')
    
def user_initiate_contact() -> str:
    """Prompts for Username"""
    while True:
        user_input = input('Type "I32CFSP_HELLO" followed by username:')
        user_input2 = user_input.split()
        
        if len(user_input2) > 2:
            print('Invalid character(s): No spaces. Please re-enter input')
        elif len(user_input2) < 2:
            print('Please enter valid Username')
        else:
            return user_input

def send_message(connection: connect4connection, message: str) -> None:
    """Sends a message"""
    connection.output.write(message + '\r\n')
    connection.output.flush()


def recieve_message(connection: connect4connection) -> str:
    """recieves a message"""
    message = connection.input.readline()[:-1]
    return message


def play_game(connection : connect4connection, game: ConnectFourGameState) -> None:
    """Main Code for playing"""
    while True:

        okay_message = ''
        AI_move_message = ''
        ready_message = ''

        user_command = input('Input DROP or POP + column # (ex. DROP 1): ')
        user_command2 = user_command.split()
        message_sent = send_message(connection, user_command)
        okay_message = recieve_message(connection)  #message 1
        
        if not okay_message == 'OKAY' and not okay_message == 'INVALID' and not okay_message == 'WINNER_RED':
            close_socket(connection)
            break
        
        print(okay_message)
        if not 'WINNER' in okay_message:
            try:
                AI_move_message = recieve_message(connection) #message 2
                if not 'POP' in AI_move_message and not 'DROP' in AI_move_message and AI_move_message != '' and AI_move_message !='READY':
                    close_socket(connection)
                    break
                print(AI_move_message)
                
            except:
                close_socket(connection)
                break
            else:
                if not AI_move_message == 'READY' and not 'WINNER' in okay_message:
                    ready_message = recieve_message(connection) #message 3
                    if not ready_message == 'READY' and not ready_message == 'WINNER_YELLOW' and not ready_message == '':
                        close_socket(connection)
                        break
                    print(ready_message)
                if 'INVALID' in okay_message:
                    pass
                elif okay_message == 'OKAY' or 'WINNER' in okay_message:
                    if user_command2[0] == 'DROP':
                        game = connectfour.drop_piece(game, int(user_command2[1])-1)
                        if not 'WINNER' in okay_message:
                            AI_move_message2 = AI_move_message.split()
                            if AI_move_message2[0] == 'DROP':
                                game = connectfour.drop_piece(game, int(AI_move_message2[1])-1)
                            else:
                                game = connectfour.pop_piece(game, int(AI_move_message2[1])-1)
                    else:
                        game = connectfour.pop_piece(game, int(user_command2[1])-1)
                        if not 'WINNER' in okay_message:
                            AI_move_message2 = AI_move_message.split()
                            if AI_move_message2[0] == 'DROP':
                                game = connectfour.drop_piece(game, int(AI_move_message2[1])-1)
                            else:
                                game = connectfour.pop_piece(game, int(AI_move_message2[1])-1)
                is_winner = connectfour.winning_player(game)
                if is_winner == 2:
                    print_board(game)
                    print('Yellow HAS WON!')
                    return None
                print_board(game)
        else:
            user_command2 = user_command.split()
            if user_command2[0] == 'DROP':
                game = connectfour.drop_piece(game, int(user_command2[1])-1)
                print_board(game)
                print('Red HAS WON!')
                break
            else:
                game = connectfour.pop_piece(game. int(user_command2[1])-1)
                print_board(game)
                print('Red HAS WON!')
                break


if __name__ == '__main__':
    host = read_host()
    port = read_port()

    OK = True
    while OK:
        print('Connecting...')
        try:
            connection = connect(host, port)
            print('Connection complete')
            
        except:
            print('ERROR')
            break
        else:
            user_input = user_initiate_contact()                #user types in username
            send_message(connection, user_input)
            recieved_message = recieve_message(connection)      #user recieves welcome

            if recieved_message == 'ERROR':
                break

            print(recieved_message)
            command = input()                                   #user types in 'AI_GAME'
            if not command == 'AI_GAME':
                print('ERROR')
                close_socket(connection)
                break
            else:
                send_message(connection, command)
                recieved_message = recieve_message(connection)      #user recieves 'READY'
                print(recieved_message)
                play_game(connection, game_start)

                if recieved_message == 'ERROR': #if recieved message not READY
                    break
                break





    
        
        print(recieved_message)

