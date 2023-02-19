#
# state.py (Final project)
#
# A State class for the Eight Puzzle
#
# name: Steven Yao
# email: styao@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Sashank Krishna
# partner's email: sashank@bu.edu
#

from board import *

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Add your method definitions here. ###
    
    def __init__(self, board, predecessor, move):
        """constructs the State object"""
        self.board = board
        self.predecessor = predecessor
        self.move = move
        if self.predecessor == None:
            self.num_moves = 0
        else:
            self.num_moves = predecessor.num_moves + 1

    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def is_goal(self):
        """ checks if the state of the board is the goal state"""
        if self.board.num_misplaced() == 0:
            return True
        else:
            return False
        
    def generate_successors(self):
        """ returns a list of State objects for all successor states of the 
            called State object
        """
        successors = []
        MOVES = ['up', 'down', 'left', 'right']
        for move in MOVES:
            b_copy = self.board.copy()
            if b_copy.move_blank(move):
                successors += [State(b_copy,self, move)]
        return successors
                
        return successors
    
    def print_moves_to(self):
        '''Prints the process of moves taken from initial to goal State'''
        if self.move == 'init':    # base case
            print('initial state:')
            print(self.board)
        else:
            pred = self.predecessor
            pred.print_moves_to()
            print("move the blank " + str(self.move) + ":")
            print(self.board)
            
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True
