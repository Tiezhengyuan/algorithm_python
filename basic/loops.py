'''
search linear from start to the end using iterator
This is most simple and straightforward approach
'''
from copy import deepcopy

class Loops:

    @staticmethod
    def for_loop(input:list):
        for i in range(len(input)):
            yield input[i]

    @staticmethod
    def for_loop2(input:list):
        for val in input:
            yield val

    @staticmethod
    def for_loop3(input:list):
        for i, val in enumerate(input):
            yield val

    @staticmethod
    def for_loop_backward(input:list):
        for i in range(-1, -len(input)-1, -1):
            yield input[i]

    @staticmethod
    def while_loop(input:list):
        i=0
        while i < len(input):
            yield input[i]
            i += 1

    @staticmethod
    def while_loop_backward(input:list):
        i=-1
        while i >= -len(input):
            yield input[i]
            i -= 1

    @staticmethod
    def while_pop_loop(input:list):
        input = deepcopy(input)
        while input:
            yield input.pop(0)

    @staticmethod
    def while_pop_loop_backward(input:list):
        input = deepcopy(input)
        while input:
            yield input.pop()

    def recursive_loop(self, input:list):
        if input:
            yield input[0]
            yield from self.recursive_loop(input[1:])

    def recursive_loop_backward(self, input:list):
        if input:
            yield input[-1]
            yield from self.recursive_loop_backward(input[:-1])
