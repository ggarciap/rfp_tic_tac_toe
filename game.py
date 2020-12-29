class TicTacToe:
    def __init__(self):
        # using a single list to represent board
        self.board = [' ' for _ in range(9)]
        # keeper of winner
        self.current_winner = None 

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]
            print(' | '  + ' | '.join(row) + ' | ')
    
    # static method can be called without an object for that # class
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]for j in range(3)]
        for row in number_board:
            print(' | '  + ' | '.join(row) + ' | ')

    def available_moves(self):
        moves = [i for i, x in enumerate(self.board) if x == ' ']
        return moves

    def empty_sqrs(self):
        return ' ' in self.board

    def num_empty_sqrs(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        ''''
            If the move is valid make the move (modify board to assing corr letter) then return True. if invalid, return false.
        ''''
        if self.board[square] == ' ':
            self.board[square] = letter
            return True
        else:
            return False
        
def play(game, x_p, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_sqrs():
        if letter = 'O':
            square = o_p.get_move(game)
        else:
            squre = x_p.get_move(game)
        
        # Making a move
        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board_nums()
        
            
