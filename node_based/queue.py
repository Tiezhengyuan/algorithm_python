'''
queue
1. data is inserted at the end
2. data is deleted or read on at the front
'''

class Element:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.end = None
        self.length = 0
    
    def insert(self, val):
        '''
        insert at the end
        '''
        new_el = Element(val)
        end_el = self.end
        end_el.next = new_el
        self.end = new_el
        self.length += 1
        if self.length == 1:
            self.front = new_el

    def get(self):
        '''
        get at the front
        '''
        return self.front.val

    def delete(self):
        '''
        delete at the front
        '''
        if self.length > 0:
            front_el = self.front
            if self.length > 1:
                next_el = front_el.next
                self.front = next_el
            else:
                self.front, self.end = None, None
            self.length -= 1
            return front_el.val
        return None

    def scan(delf):
        '''
        scan from the front
        '''
        curr_el = self.front
        while curr_el:
            yield curr_el
            curr_el = getattr(curr_el, 'next') 

