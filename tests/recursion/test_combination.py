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