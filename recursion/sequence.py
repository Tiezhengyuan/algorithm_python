

def factorial(n:int):
    '''
    n!=n*n-1*n-2...*1
    '''
    if n==1:
        return n
    return n * factorial(n-1)

def fibonacci(n:int):
    '''
    f(n) = f(n-1) + f(n-2)
    '''
    if n==2 or n==1:
        return 1
    if n<=0:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)

def get_sequence(low:int, high:int):
    if low <= high:
        yield low
        yield from get_sequence(low + 2, high)

def get_sum(low:int, high:int):
    if low == high:
        return low
    return low + get_sum(low + 1, high)

def triangle_numbers(n:int):
    '''
    sequence: 1,3,6,10,15,21
    f(n) = n + f(n-1)
    '''
    if n <= 0:
        return 0
    return triangle_numbers(n-1) + n
