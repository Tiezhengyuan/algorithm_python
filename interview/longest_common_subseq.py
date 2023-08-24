'''
given two sequences, find the longest sharing sub seq
suppose sub common seq is consecutive

solution: generate all possible sub sequnces find the longest
'''
#step1: subsequences given length
def sub_seq(seq, k):
    yield seq[:k]
    if len(seq)>k:
        yield from sub_seq(seq[1:], k)

#step2: get all subsequence
def lcs(seq, k=None):
    if k is None:
        k = len(seq)
    while k>2:
        yield from sub_seq(seq,k)
        k -= 1

def main(seq1, seq2):
    # suppose seq1>= seq2
    if len(seq1) < len(seq2):
        seq1, seq2 = seq2, seq1
    iters = lcs(seq2)
    for subseq in iters:
        if subseq in seq1:
            print(subseq)
            return(len(subseq))



if __name__ == '__main__':
    seq1='ATGCTGGCGTTT'
    seq2 = 'CTGGCGCA'
    main(seq1, seq2)

