from tests.helper import *
from recursion.expand import *

@ddt
class TestExpand(TestCase):

    @data(
        # start from c
        [['a','b','c','d'], 2,  [['c'], ['b', 'c', 'd'], ['a', 'b', 'c', 'd']]],
        ['a',0, ['a']],
    )
    @unpack
    def test_double_expand(self, input, start, expect):
        obj = double_expand(input, start, start+1)
        res = []
        for a,b in obj:
            res.append(input[a:b])
        assert res == expect

    @data(
        # start from c
        [['a','b','c','d'], 2, [['c'], ['b', 'c'], ['a', 'b', 'c'], \
            ['a', 'b', 'c', 'd'], ['b', 'c', 'd'], ['a', 'b', 'c', 'd'], \
            ['a', 'b', 'c', 'd'], ['c', 'd'], ['b', 'c', 'd'], \
            ['a', 'b', 'c', 'd'], ['b', 'c', 'd'], ['a', 'b', 'c', 'd']]],
        ['a',0, ['a']],
    )
    @unpack
    def test_wild_expand(self, input, start, expect):
        obj = wild_expand(input, start, start+1)
        res = []
        for a,b in obj:
            res.append(input[a:b])
        assert res == expect


    def test_condition_wild_expand(self):
        # default condition
        input = 'eabcb'
        obj = condition_wild_expand(input, 2, 3, condition_default)
        res = []
        for a,b in obj:
            res.append(input[a:b])
        assert res ==  ['b', 'ab', 'eab', 'eabc', 'eabcb', 'abc', 'eabc', \
            'eabcb', 'abcb', 'eabcb', 'eabcb', 'eabc', 'eabcb', 'bc', \
            'abc', 'eabc', 'eabcb', 'abcb', 'eabcb', 'eabcb', 'bcb', \
            'abcb', 'eabcb', 'abcb', 'eabcb', 'abc', 'eabc', 'eabcb', \
            'abcb', 'eabcb', 'eabcb']

        # all unique
        obj = condition_wild_expand(input, 1, 2, condition_unique)
        res = []
        for a,b in obj:
            res.append(input[a:b])
        print(res)
        assert res == ['a', 'ea', 'eab', 'eabc', 'ab', 'eab', \
            'eabc', 'abc', 'eabc', 'eabc', 'eab', 'eabc']
