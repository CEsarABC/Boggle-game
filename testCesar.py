from string import ascii_uppercase
from random import choice


def make_grid(width, height):
    '''
    crates a grid to hold all the tiles 
    for boogle
    '''
    return{(row, col): choice(ascii_uppercase) 
        for row in range(height)
        for col in range(width)
    }
    
def neighbours_of_position(coords):
    '''
    geta the neighboura of a given position
    '''
    row = coords[0]
    col = coords[1]
    
    # assign each of the neigbours
    # top left to top right 
    top_left = (row -1, col - 1)
    top_center = (row -1, col)
    top_right = (row -1, col + 1)
    #left to right
    left = (row, col -1)
    # the coordinates passed to this 
    # function situated here
    right = (row, col + 1)
    
    #bottom-left to bottom-right
    bottom_left = (row + 1, col - 1)
    bottom_center = (row +1, col)
    bottom_right = (row +1, col + 1)
    
    return [top_left , top_center, top_right,
            left, right,
            bottom_left, bottom_center, bottom_right]

def all_grid_neighbours(grid):
    '''
    get all of the possible neigbours for each position 
    in the grid
    '''
    neigbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neigbours[position] = [p for p in position_neighbours if p in grid]
        
    return neigbours


def test_all_grid_neighbours():
        '''
        ensure that all the grid positions have neighbours
        '''
        grid = make_grid(2,2)
        neighbours = all_grid_neighbours(grid)
        assert len(neighbours) == len(grid)
        for pos in grid:
            others = list(grid) # creates a new list from the dictionary's keys
            others.remove(pos)
            assert sorted(neighbours[pos]) == sorted(others)