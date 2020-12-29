import math
import random 

class Player:
    def __init__(self,letter):
        # x or o for letter
        self.letter = letter
    def get_move(self, game):
        pass

class RandomComputerP(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanP(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_sqr = False
        val = None
        while not valid_sqr:
            sqr = input(self.letter + '\'s turn. Input move (0-9)')
            try:
                val = int(sqr)
                if val not in game.available_moves():
                    raise ValueError
                valid_sqr = True
            except ValueError:
                print('Invalid input, please try agin')
