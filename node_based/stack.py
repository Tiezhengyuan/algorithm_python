'''
stack:
first in and last out, last in and first out
'''
from typing import Iterable

class Element:
    def __init__(self, val=None):
        self.val = val
        self.next = None
    
class Stack:

    def __init__(self):
        self.head = Element()
        self.length = 0

    def add(self, el:Element):
        if self.head.next:
            next_el = self.head.next
            el.next = next_el
        self.head.next = el
        self.length += 1

    def push(self, val=None):
        new_el = Element(val)
        self.add(new_el)
        return new_el

    def feed(self, input:Iterable):
        for el in input:
            self.push(el)

    def get(self):
        return self.head.next.val if self.head.next else None

    def pop(self)->Element:
        if self.head.next:
            first = self.head.next
            if first.next:
                second = first.next
                self.head.next = second
            else:
                self.head.next = None
            # print(first, getattr(first, 'val'))
            self.length -= 1
            return first
        return None

    def scan(self, curr:Element=None)->Element:
        if curr is None and self.head.next:
            curr = self.head.next
        if curr:
            yield curr
        if curr and getattr(curr, 'next'):
            yield from self.scan(curr.next)

    def is_empty(self)->bool:
        if self.head.next:
            return False
        return True

    def length(self)->int:
        return self.length
    
    def reverse(self):
        new_stack = Stack()
        while self.length > 0:
            el = self.pop()
            el.next = None
            # print(el, getattr(el, 'val'))
            new_stack.add(el)
        self.head = new_stack.head
        self.length = new_stack.length
            
    def to_list(self)->list:
        return [el.val for el in self.scan()]        
