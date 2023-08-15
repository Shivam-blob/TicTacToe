#Grid Format = 3 space, line, 3 space, line, 3 space as follows

'''
       |   |   
    ---+---+---
       |   |   
    ---+---+---
       |   |   

'''
'''
{row1}
    ---+---+---
{row2}
    ---+---+---
{row3}

'''
class TttGrid:


    
    
    def __init__(self) -> str:
        test =      "012345678901234"
        self.row1 = "       |   |   "
        self.row2 = "       |   |   "
        self.row3 = "       |   |   "
        self.row_list = [self.row1, self.row2, self.row3]
        self.grid = f'''
        {self.row_list[0]}
            ---+---+---
        {self.row_list[1]}
            ---+---+---
        {self.row_list[2]}
        '''
    
    def x_index(self, num):
        #1, 5   2, 9   3, 13
        indexdict = {1:5, 2:9, 3:13}
        return indexdict[num]
    
    def update_grid(self, x, y, letter):
        self.row_list[y-1] = (self.row_list[y-1])[:self.x_index(x)] + letter + (self.row_list[y-1])[self.x_index(x) + 1:]
        
    
    
    def __str__(self):
        self.grid = f'''
        {self.row_list[0]}
            ---+---+---
        {self.row_list[1]}
            ---+---+---
        {self.row_list[2]}
        '''
        return self.grid
    def reset_grid(self):
        self.row_list = [self.row1, self.row2, self.row3]



class AvailableMoves:
    def __init__(self) :
        self.available = [[1,2,3], [4,5,6], [7,8,9]]
        self.movelist = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
        #tuple with moves
    def update_moves(self, x, y, letter):
        if (type(x), type(y)) == (int, int) and letter.lower() in ('o', 'x'):
            self.available[x - 1][y - 1] = letter
            move_to_remove = (x, y)
            
            # Find the index of the move and remove it
            for idx, move in enumerate(self.movelist):
                if move == move_to_remove:
                    self.movelist.pop(idx)
                    break
    def win(self):
        # Check rows
        for row in self.available:
            if row[0] == row[1] == row[2] and row[0] != 3:
                return True
        
        # Check columns
        for col in range(3):
            if self.available[0][col] == self.available[1][col] == self.available[2][col] and self.available[0][col] != 3:
                return True
        
        # Check diagonals
        if self.available[0][0] == self.available[1][1] == self.available[2][2] and self.available[0][0] != 3:
            return True
        if self.available[0][2] == self.available[1][1] == self.available[2][0] and self.available[0][2] != 3:
            return True
        
        return False





    
