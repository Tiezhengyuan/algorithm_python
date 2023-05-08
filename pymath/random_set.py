'''
Random sets are random elements taking values as subsets of some space, 
serve as general mathematical models for set-valued observations 
and irregular geometrical patterns, and generate the traditional 
concept of ordinary random points/vectors.
http://www.scholarpedia.org/article/Random_sets
'''
import math
import random

class RandomSet:
    def __init__(self):
        self.data = []
    
    def insert(self, val:int)->bool:
        if val not in self.data:
            self.data.append(val)
            return True
        return False

    def remove(self, val:int)->bool:
        if val in self.data:
            self.data.remove(val)
            return True
        return False
    
    def get_random(self)->int:
        random_index = random.randint(0, len(self.data)-1)
        return self.data[random_index]

    def shuffle(self)->list:
        # deep copy
        input = self.data.copy()
        random.shuffle(input)
        return input