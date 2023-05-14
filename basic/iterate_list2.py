'''
matrix or 2D array
'''



def by_row_forward(input:list):
    '''
    -->
    -->
    '''
    for row in input:
        for val in row:
            yield val

def by_row_backward(input:list):
    '''
    <--
    <--
    '''
    # Note the end index is minus of length and one
    for r in range(-1, -len(input)-1, -1):
        row = input[r]
        for c in range(-1, -len(row)-1, -1):
            yield row[c]

def by_col_top_left(input:list):
    '''
    | |
    v v
    '''
    for c in range(0, len(input[0])):
        for r in range(0, len(input)):
            yield input[r][c]

def by_row_snake(input:list):
    '''
    -->
    <--
    '''
    for r in range(0, len(input)):
        row = input[r]
        cols = range(0, len(row)) if r%2==0 else \
            range(-1, -len(row)-1, -1)
        for c in cols:
            yield row[c]

def by_col_snake(input:list):
    '''
    | ^
    v |
    '''
    for c in range(0, len(input[0])):
        rows = range(0, len(input)) if c%2 == 0 else \
            range(-1,-len(input)-1, -1)
        for r in rows:
            yield input[r][c]


def traverse(input:list, start:tuple, visited:list[tuple]):
    '''
    Given a start *, clockwise walk through all points
    0 0 0
    0 * 0
    0 0 0 
    args: start tuple is (row index, col index)
    '''
    nrow, ncol = len(input), len(input[0])
    # four possible directions
    for move in [(-1,0), (0,1), (1,0), (0,-1)]:
        next_row = start[0] + move[0]
        next_col = start[1] + move[1]
        if 0 <= next_row < nrow and 0 <= next_col < ncol :
            next = (next_row, next_col)
            if next not in visited:
                visited.append(next)
                # return coordinate of that point
                yield next
                # yield input[next_row][next_col]
                yield from traverse(input, next, visited)

def traverse_binary(input:list, start:tuple):
    '''
    Given a start , walk through all points. all visited are ones
    0 0 0
    0 1 0
    0 0 1 
    args: start tuple is (row index, col index)
    '''
    nrow, ncol = len(input), len(input[0])
    for move in [(-1,0), (0,1), (1,0), (0,-1)]:
        next_row = start[0] + move[0]
        next_col = start[1] + move[1]
        if 0 <= next_row < nrow and 0 <= next_col < ncol:
            next = (next_row, next_col)
            is_visited = input[next_row][next_col]
            if is_visited == 0:
                yield next
                input[next_row][next_col] = 1
                yield from traverse_binary(input, next)

def zigzag_walk(input:list, vertical_first:bool):
    '''
    matrix: 3X3
    |  /|   _ _ _
    | / |     /
    |/  |,  _ _ _
    direction: vertical first, horizontal first
    '''
    nrow, ncol = len(input), len(input[0])
    start = (0, 0)
    next, path = start, []
    direction = 'north_south' if vertical_first is True else 'west_east'
    while next:
        # print('#', direction, next)
        path.append(next)
        next, direction = zigzag_step(nrow, ncol, next, direction)
    return path

def zigzag_step(nrow:int, ncol:int, start:tuple, walk:str):
    '''
    matrix should be square matrix: nrow = ncol
    coordinator: (row, col)
    vertical first:
        'north_south': from north to sourth
        'west_north': from west south to east north
    horizontal first:
        'west_east': from west to east
        '
    '''
    # print(start, walk)
    # vertical first
    if walk == 'north_south':
        if start[0]+1 < nrow:
            return (start[0]+1, start[1]), walk
        # the last column
        if start[1]+1 < ncol:
            return zigzag_step(nrow, ncol, start, 'west_north')
    elif walk == 'west_north':
        # print(start[0]-1, start[1]+1)
        if start[0]-1 >= 0 and start[1]+1 < ncol:
            return (start[0]-1, start[1]+1), walk
        return zigzag_step(nrow, ncol, start, 'north_south')
    # horizontal first
    elif walk == 'west_east':
        if start[1]+1 < ncol:
            return (start[0], start[1]+1), walk
        # the last row
        if start[0]+1 < nrow:
            return zigzag_step(nrow, ncol, start, 'north_west')
    elif walk == 'north_west':
        if start[0]+1 < nrow and start[1]-1 >= 0:
            return (start[0]+1, start[1]-1), walk
        return zigzag_step(nrow, ncol, start, 'west_east')
    return None, None

def zigzag_iteration(nrow:int, row_index, col_index, walk):
    '''
    specify rows only, 
    |  /|  /|  /|
    | / | / | / |
    |/  |/  |/  |...
    '''
    if walk == 'north_south':
        if row_index+1 < nrow:
            yield row_index+1, col_index, walk
            row_index += 1
        else:
            walk = 'west_north'
    elif walk == 'west_north':
        if row_index-1 >= 0:
            yield row_index-1, col_index+1, walk
            row_index -= 1
            col_index += 1
        else:
            walk = 'north_south'
    yield from zigzag_iteration(nrow, row_index, col_index, walk)
