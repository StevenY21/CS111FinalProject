#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Steven Yao
# email:styao@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Sashank Krishna
# partner's email: sashank@bu.edu
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###

    def __init__(self, depth_limit):
        '''Constructor for Searcher object'''
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        
        
    def  add_state(self, new_state):
        '''Adds a state object to the searchers list of untested states'''
        self.states+=[new_state]
        
    def should_add(self, state):
        '''Checks if a state object should be added to the searcher object'''
        if (self.depth_limit < state.num_moves) \
        and self.depth_limit != -1:
            return False
        elif state.creates_cycle():
            return False
        else:
            return True
    
    def add_states(self, new_states):
        '''Checks and takes states from a list new_states and adds 
        them to the untested states list'''
        for st in new_states:
            if self.should_add(st):
                self.add_state(st)
                
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        '''Finds the solution in the list of states starting 
        with the init_state'''
        self.add_state(init_state)
        while self.states != []:
            s = self.next_state()
            self.num_tested+=1
            if s.is_goal():
                return s
            else:
                self.add_states(s.generate_successors())
        return None
        
        
    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s

### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    """ BFS is a subclass of Searcher that chooses one the untested states 
        that has the smallest depth
    
    """
    def next_state(self):
        """ chooses the state that has been in the list the longest, 
            removing it from the list and returning it
        """
        s = self.states[0]
        self.states.remove(s)
        return s

class DFSearcher(Searcher):
    """ DFS is a subclass of Searcher that chooses one the untested states 
        that has the largest depth
    """
    def next_state(self):
        """ chooses the state that was most recently added to the list, 
            removing it from the list and returning it
        """
        s = self.states[-1]
        self.states.remove(s)
        return s


def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###
def h1(state):
    """ a heuristic function that always returns an estimate of how many 
    additional moves are needed to get from state to the goal state 
    """
    h = Board.num_misplaced(state.board)
    return h

def h2(state):
    """ a heuristic function that always returns the sum of the distances
        of the tiles in the state from goal state
    """
    GOAL_TILES = [['0', '1', '2'],
                  ['3', '4', '5'],
                  ['6', '7', '8']]
    state_tiles = state.board.tiles
    sum_dist=0
    for r in range(3):
        for c in range(3):
            if state_tiles[r][c] != GOAL_TILES[r][c]:
                if state_tiles[r][c] != '0': 
                    tile = state_tiles[r][c]

                    goal_row = 0
                    goal_col = 0
                    for i in range(3):
                        for j in range(3):
                            if GOAL_TILES[i][j] == tile:
                                goal_row = i
                                goal_col = j
                    sum_dist += (abs(r - goal_row) + abs(c - goal_col))

    return sum_dist

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def  __init__(self, heuristic):
        super().__init__(-1)
        self.heuristic = heuristic

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)

    def  add_state(self, new_state):
        ''' Adds a sublist that includes both priority and the state to the list
            of untested states
        '''
        self.states+=[[self.priority(new_state),new_state]]
    
    def next_state(self):
        """ chooses one of the states with the highest priority, 
            removing it from the list and returning it
        """
        s = max(self.states)
        self.states.remove(s)
        return s[-1]
        
### Add your AStarSeacher class definition below. ###
class AStarSearcher(GreedySearcher):
    """ A GreedySearcher subclass that performs A* search, a search that assigns 
        priority and takes into account the cost that has already been expended 
        to get to that state
    """
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * (self.heuristic(state) + state.num_moves)
    
    
    
    
    
    
    
    
    