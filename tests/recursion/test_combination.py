from tests.helper import *
from recursion.combination import *

@ddt
class TestCombination(TestCase):

    @data(
        # combinations=1 
        [1, [[1]]],
        # combinations=2 
        [2, [[1, 2], [2]]],
        # combinations=3 
        [3, [[1, 2, 3], [2, 3], [1, 3]]],
        # combinations=5 
        [4, [[1, 2, 3, 4], [2, 3, 4], [1, 3, 4], [1, 2, 4], [2, 4]]],
        # combinations=8
        [5, [[1, 2, 3, 4, 5], [2, 3, 4, 5], [1, 3, 4, 5], [1, 2, 4, 5], \
            [2, 4, 5], [1, 2, 3, 5], [2, 3, 5], [1, 3, 5]]],

    )
    @unpack
    def test_stair_2steps(self, input, expect):
        res = []
        stair_2steps(input, [], res)
        # print(res)
        assert res == expect

    @data(
        # combinations=1 
        [1, [[1]]],
        # combinations=2 
        [2, [[1, 2], [2]]],
        # combinations=4 
        [3, [[1, 2, 3], [2, 3], [1, 3], [3]]],
        # combinations=7
        [4, [[1, 2, 3, 4], [2, 3, 4], [1, 3, 4], [3, 4], \
            [1, 2, 4], [2, 4], [1, 4]]],
        # combinations=13
        [5, [[1, 2, 3, 4, 5], [2, 3, 4, 5], [1, 3, 4, 5], \
            [3, 4, 5], [1, 2, 4, 5], [2, 4, 5], [1, 4, 5], \
            [1, 2, 3, 5], [2, 3, 5], [1, 3, 5], [3, 5], \
            [1, 2, 5], [2, 5]]],

    )
    @unpack
    def test_stair_3steps(self, input, expect):
        res = []
        stair_3steps(input, [], res)
        # print(res)
        assert res == expect

    
    @data(
        # 3! = 3*2=6
        ['abc', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']],
        ['a', ['a']],
    )
    @unpack
    def test_anagram_char(self, input, expect):
        res = anagram_char(input, '')
        assert list(res) == expect

    @data(
        # 3!/(3-2)! = 6
        ['abc', 2, ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']],
        # 4!/(4-2)! = 4*3*2*1/(2*1)=12
        ['abcd', 2, ['ab', 'ac', 'ad', 'ba', 'bc', 'bd', \
            'ca', 'cb', 'cd', 'da', 'db', 'dc']],
    )
    @unpack
    def test_select_anagram_char(self, input, str_len, expect):
        res = select_anagram_char(input, '', str_len)
        assert list(res) == expect

    @data(
        ['abc', ['a', 'b', 'c', 'ab', 'ac', 'ba', 'bc', 'ca', \
            'cb', 'abc', 'acb', 'bac', 'bca', 'cab', 'cba']],
        ['a', ['a']],
    )
    @unpack
    def test_all_anagrams(self, input, expect):
        res = all_anagrams(input, '')
        assert list(res) == expect


    @data(
        ['abc', 2, ['ab', 'ac', 'bc']],
        ['a', 1, ['a']],
        # 6!/(3!*3!) = 20
        ['abcdef', 3, ['abc', 'abd', 'abe', 'abf', 'acd', 'ace', \
            'acf', 'ade', 'adf', 'aef', 'bcd', 'bce', 'bcf', \
            'bde', 'bdf', 'bef', 'cde', 'cdf', 'cef', 'def']],
    )
    @unpack
    def test_combination_char(self, input, str_len,expect):
        res = combination_char(input, '', str_len)
        assert list(res) == expect

    @data(
        [[-1,0,1,2,-1,-4], [[-1,0,1], [-1,-1,2]]],
        [[0,1,1], []],
    )
    @unpack
    def test_threeSum(self, input, expect):
        res = threeSum(input)
        assert res == expect