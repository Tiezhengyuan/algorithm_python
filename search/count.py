'''
1. count occurence using hash table
'''

from typing import List

class Count:

    
    @staticmethod
    def h_index(citations: List[int]) -> int:
        '''
        Given an array of integers citations where citations[i] 
        is the number of citations a researcher received 
        for their ith paper, return the researcher's h-index.
        According to the definition of h-index on Wikipedia: 
        The h-index is defined as the maximum value of h 
        such that the given researcher has published 
        at least h papers that have each been cited at least h times.
        '''
        res = {}
        for c in citations:
            if c in res:
                res[c] += 1
            else:
                res[c] = 1

        acc_count = 0
        for cited_count in sorted(res.items(), reverse=True):
            # print(cited_count, acc_count)
            if cited_count[0] == (cited_count[1] + acc_count):
                return cited_count[0]
            else:
                acc_count += cited_count[1]
        else:
            return cited_count[0]