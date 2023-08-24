'''
Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
'''
def detect(seq, subseq, index):
    if index>=len(seq):
        return -1
    if seq[index:].startswith(subseq):
        return index
    return detect(seq, subseq, index+1)
    


def main(input):
    for seq, subseq in input:
        res = detect(seq, subseq, 0)
        print(res)


if __name__ == '__main__':
    input = [
        ('ATGTCATGGG', 'ATG'),
        ('ATGTTCGT', 'TTTC'),
        ('ATGTCATGGTCG', 'GTC'),
    ]
    main(input)

