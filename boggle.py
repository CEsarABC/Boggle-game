def make_grid(weight, height):
    '''
    crates a grid to hold all the tiles 
    for boogle
    '''
    return{(row, col): '' for row in range(height)
        for col in range(weight)
    }