#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Steven Yao
# email: styao@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Sashank Krishna
# partner's email: sashank@bu.edu
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        index = 0
        for i in range(3):
            for j in range(3):
                self.tiles[i][j] = digitstr[index]
                index+=1
                if self.tiles[i][j] == '0':
                    self.blank_r = i
                    self.blank_c = j
                    
        
        
    ### Add your other method definitions below. ###
    
    def __repr__(self):
        '''returns the string representation of the board object'''
        returned =''
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] == '0':
                    returned+='_ '
                else:
                    returned+=self.tiles[i][j] + ' '
            returned+='\n'
        return returned
    
    
    def move_blank(self, direction):
        '''moves the blank on the specified board object to the given direction'''
        
        
        new_col = self.blank_c
        new_row = self.blank_r
        
        if direction == 'up':
            new_row -=1
        elif direction == 'down':
            new_row +=1
        elif direction == 'left':
            new_col-=1
        elif direction == 'right':
            new_col+=1
        else:
            return False
        
        if new_col<0 or new_col>2 or new_row<0 or new_row>2:
            return False
        else:
            self.tiles[self.blank_r][self.blank_c] = self.tiles[new_row][new_col]
            self.tiles[new_row][new_col] = '0'
            self.blank_c = new_col
            self.blank_r = new_row
            
            return True
            
    def digit_string(self):
        ''' Creates and returns a string version of the Board object'''
        returned =''
        for i in self.tiles:
            for j in i:
                returned +=j
        return returned
                
    def copy(self):
        '''Creates a deep copy of the board and returns it'''
        return Board(self.digit_string())
    
    def num_misplaced(self):
        '''counts and returns the number of tiles in the called Board object 
        that are not where they should be in the goal state.'''
        
        goal_state = '012345678'
        digitstr = self.digit_string()
        num_misplaced=0
        for i in range(9):
            if digitstr[i] != '0':
                if digitstr[i] != goal_state[i]:
                    num_misplaced+=1
        return num_misplaced
                    
    def __eq__(self,other):
        '''checks the equality of 2 Board objects'''
        return self.digit_string() == other.digit_string()
