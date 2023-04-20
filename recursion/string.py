

def search_char(seq:str, nt:str, pos:int=None):
    '''
    return index of a character in a string
    '''
    if pos is None:
        pos = 0
    if not seq:
        return None
    if seq[0] == nt:
        return pos
    return search_char(seq[1:], nt, pos + 1)
    