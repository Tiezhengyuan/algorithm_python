
from typing import Iterable

class IterateDict:

    @staticmethod
    def by_key_1(input:dict)->Iterable:
        for k in input:
            yield k

    @staticmethod
    def by_key_2(input:dict)->Iterable:
        for k in input.keys():
            yield k

    @staticmethod
    def by_key_3(input:dict)->Iterable:
        for k in list(input):
            yield k

    @staticmethod
    def by_value(input:dict)->Iterable:
        for v in input.values():
            yield v

    @staticmethod
    def by_pair(input:dict)->Iterable:
        for k,v in input.items():
            yield k,v

    @staticmethod
    def by_ascending_key(input:dict)->Iterable:
        # Note: list(input).sort() is wrong
        # .sort() return None
        for k in sorted(input.keys()):
            yield k

    @staticmethod
    def by_descending_key(input:dict)->Iterable:
        for k in sorted(input.keys(), reverse=True):
            yield k
    
    @staticmethod
    def by_descending_value(input:dict)->Iterable:
        # lambda function specify sorting rule
        for pair in sorted(input.items(), key=lambda x: x[1], reverse=True):
            yield pair[1]