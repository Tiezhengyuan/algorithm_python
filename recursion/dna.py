

def reverse(dnaseq):
    return dnaseq[::-1]

def complement(nt):
    c= {'A':'T', 'T':'A','G':'C','C':'G'}
    if nt in c:
        return c[nt]
    return 'N'
    
def reverse_complement(dnaseq):
    if len(dnaseq)==0:
        return ''
    else:
        return complement(dnaseq[-1]) + reverse_complement(dnaseq[:-1])

def count_nt(dnaseq:str, nt:str):
    '''
    count number of a certain nucleotide
    '''
    if len(dnaseq) == 0:
        return 0
    count = 1 if dnaseq[0] == nt else 0
    return count + count_nt(dnaseq[1:], nt)