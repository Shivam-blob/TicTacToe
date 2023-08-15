import math
import random

#Player Base Superclass for human and computer player
class Player:
    def __init__(self, letter):
        self.letter = letter
    def get_move(self, game):
        pass
    
# Human Player Class
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def player_dialouge(self):
        print('Human Player\'s turn: ')
    def win_dialogue(self):
        print('You WON!')
    def get_move(self, available_moves):
        x_move = input('enter column number (1-3): ')
        y_move = input('enter row number (1-3): ')
        return (int(x_move), int(y_move), self.letter)
#Computer Player
class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def player_dialouge(self):
        print('Computer Player\'s turn: ')
    def win_dialogue(self):
        print('Computer Player has WON')
    def get_move(self, available_moves):
        move_tuple = (*random.choice(available_moves), self.letter)
        return move_tuple
    
