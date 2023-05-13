from tests.helper import *
from basic.iterate_list import IterateList as c

@ddt
class TestIterateList(TestCase):

    @data(
        [[1,2,2,4], [2,1], True],
        [[2,1], [1,2,2,4], True],
        [[1,2,2,4], [2,5], False],
        [[2,6], [1,2,2,4], False],
        [[1,2,2,4], [], True],
        [[], [2,1], True],
    )
    @unpack
    def test_is_subset(self, arr1, arr2, expect):
        res = c.is_subset(arr1, arr2)
        assert res == expect


    @data(
        [[1,2,2,4], [1,2], [1,2]],
        [[5,1], [4,1], [1,]],
        [[5,1], [4,2], []],
    )
    @unpack
    def test_get_intersection(self, arr1, arr2, expect):
        res = c.get_intersection_1(arr1,arr2)
        assert res == expect

    @data(
        [['a','b','c','d','c','e','f'], 'c'],
    )
    @unpack
    def test_detect_first_duplicate(self, arr, expect):
        res = c.detect_first_duplicate(arr)
        assert res == expect


    @data(
        ['minimum', 'n'],
    )
    @unpack
    def test_detect_first_unique(self, input, expect):
        res = c.detect_first_unique(input)
        assert res == expect

    @data(
        ['the quick brown box jumps over a lazy dog', 'f'],
    )
    @unpack
    def test_detect_missing_letters(self, input, expect):
        res = c.detect_missing_letters(input)
        assert res == expect