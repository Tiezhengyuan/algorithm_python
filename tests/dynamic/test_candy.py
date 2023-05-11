from tests.helper import *
from dynamic.candy import *

@ddt
class TestCandy(TestCase):

    @data(
        # candy: 2,1,2
        [[1,0,2], 5],
        # candy: 1,2,1
        [[1,2,2],4],
        # candy: 1,3,2,1
        [[1,5,2,1], 7],
    )
    @unpack
    def test_candy(self, ratings, expect):
        res = greedy(ratings)
        assert res == expect
        res = traverse(ratings)
        assert res == expect
        res = search_peak(ratings)
        # assert res == expect

    @data(
        [[1,], True],
        [[1,2], True],
        [[1,2,1], True],
        [[1,3,2], True],
        [[2,1], False],
        [[1,1], False],
        [[1,2,3,3], False],
        [[1,2,3,1,2,1], False],
    )
    @unpack
    def test_is_peak(self, ratings, expect):
        res = is_peak(ratings)
        assert res == expect

    @data(
        [[1,0,2], [[1], [0, 2]]],
        [[1,2,2], [[1, 2], [2]]],
        [[1,5,2,1], [[1, 5, 2, 1]]],
    )
    @unpack
    def test_detect_peak(self, ratings, expect):
        res = detect_peak(ratings)