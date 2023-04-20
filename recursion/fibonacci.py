'''
Fibonacci problems: compare various recursive approached

'''

def f1(n):
    '''
    function approach
    '''
    if n==1:
        return 1
    if n<=0:
        return 0
    return f1(n-1) + f1(n-2)

class Fibonacci:
    def __init__(self):
        self.output = []
        self.memo = {1:1}
    
    @staticmethod
    def f2(n:int):
        '''
        static method approach
        '''
        if n==1:
            return 1
        if n<=0:
            return 0
        return Fibonacci.f2(n-1) + Fibonacci.f2(n-2)

    def f3(self, n:int):
        '''
        object approach
        '''
        if n==1:
            return 1
        if n<=0:
            return 0
        return self.f3(n-1) + self.f3(n-2)

    def f4(self, n:int):
        '''
        dynamic programming: memorization
        dynamic programing is process of optimizing recursive problems
        that have overlapping subproblems
        '''
        if n == 1:
            return 1
        if n<=0:
            return 0
        if n not in self.memo:
            self.memo[n] = self.f4(n-1) + self.f4(n-2)
        return self.memo[n]
