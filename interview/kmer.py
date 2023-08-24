'''
slice sequence
'''
def kmer(input,k):
    yield input[0:k]
    if len(input)>k:
        yield from kmer(input[k:], k)
    

def main(input, k):
    iters= kmer(input,k)
    for x in iters:
        print(x)
    


if __name__ == '__main__':
    input = 'ATGCTAG'
    k=3
    main(input,k)

