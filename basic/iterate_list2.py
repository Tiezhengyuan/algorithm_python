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
