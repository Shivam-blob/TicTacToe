from Grid import TttGrid, AvailableMoves
from Players import HumanPlayer, ComputerPlayer

def tictactoe():
    #initializing objects
    opposite_key = {'o':'x', 'x': 'o'}
    human_letter = input('would you like to play as x , or , o? \n>').lower()
    computer_letter = opposite_key[human_letter]
    
    if human_letter == 'o':
        OPlayer = HumanPlayer('o')
        XPlayer = ComputerPlayer('x')
    else:
        XPlayer = HumanPlayer('o')
        OPlayer = ComputerPlayer('x')
    
    display_grid = TttGrid()
    move_logistics =  AvailableMoves()
    print('X player always goes first')
    print(display_grid)
    while True:
        xwin = False
        
        XPlayer.player_dialouge()
        Xmove = XPlayer.get_move(move_logistics.movelist)#gives: x, y, letter
        display_grid.update_grid(Xmove[0], Xmove[1], Xmove[2])
        move_logistics.update_moves(Xmove[0], Xmove[1], Xmove[2])
        print(display_grid)
        if move_logistics.win():
            win = True
            xwin = True
            break
        if len(move_logistics.movelist) == 0:
            win = False
            break
        OPlayer.player_dialouge()
        Omove = OPlayer.get_move(move_logistics.movelist)
        display_grid.update_grid(Omove[0], Omove[1], Omove[2])
        move_logistics.update_moves(Omove[0], Omove[1], Omove[2])
        print(display_grid)
        if move_logistics.win():
            win = True
            xwin = False
            break
        if len(move_logistics.movelist) == 0:
            win = False
            break
    if win:
        if xwin:
            XPlayer.win_dialogue()
        else:
            OPlayer.win_dialogue()
    else:
        print('It\'s a Tie :(')
        
        
input('\n' *5 + 'This is a game of Tic Tac Toe against a robot. (press enter to begin)\n>')   
tictactoe()