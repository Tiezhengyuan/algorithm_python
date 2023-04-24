from tests.helper import *
from node_based.stack import *

@ddt
class TestStack(TestCase):

    
    @data(
        [None, None, None],
        ['a', 'a', None],
    )
    @unpack
    def test_element(self, val, expect_val, expect_next):
        res = Element(val)
        assert res.val == expect_val
        assert res.next == expect_next


    def test_CRUD(self):
        c = Stack()
        assert c.head.val == None
        assert c.head.next == None

        el_a = c.push('a')
        assert el_a.val == 'a'
        assert c.get() == 'a'

        el_b = c.push('b')
        assert el_b.val == 'b'
        assert el_b.next == el_a
        assert c.get() == 'b'

        el_none = c.push()
        assert el_none.val == None
        assert el_none.next == el_b
        assert c.get() == None

        res = c.pop()
        assert res.val == None
        assert c.get() == 'b'
        res = c.pop()
        assert c.get() == 'a'
        res = c.pop()
        assert c.get() == None

    def test_scan(self):
        c = Stack()
        res = [el.val for el in c.scan()]
        assert res == []

        c.push('a')
        c.push('b')
        res = [el.val for el in c.scan()]
        assert res == ['b','a']

    def test_empty(self):
        c = Stack()
        assert c.is_empty() == True
        c.push()
        assert c.is_empty() == False

    def test_length(self):
        c = Stack()
        assert c.length == 0
        c.push('a')
        assert c.length == 1
        c.push('b')
        assert c.length == 2
        c.pop()
        assert c.length == 1
    
    def test_reverse(self):
        c = Stack()
        c.reverse()
        res = [el.val for el in c.scan()]
        assert res == []

        c.push('a')
        c.push('b')
        res = [el.val for el in c.scan()]
        assert res == ['b', 'a']
        c.reverse()
        res = [el.val for el in c.scan()]
        assert res == ['a', 'b']

    def test_feed(self):
        c = Stack()
        res = c.to_list()
        assert res == []

        #reverse string
        c.feed('abc')
        res = c.to_list()
        assert res == ['c', 'b', 'a']
