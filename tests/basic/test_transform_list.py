
from tests.helper import *
from basic.transform_list import *

INPUT_1 = [[1,2,3],[4,5,6]]

INPUT_3 = [0,1,0,2,1,0,1,3,2,1,2,1]
RESULT_3 = [
    [0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,1,0,0,0,1,1,0,1,0],
    [0,1,0,1,1,0,1,1,1,1,1,1]
]


@ddt
class TestTransform(TestCase):

    @data(
        [[1,2,3], [3,2,1]],
    )
    @unpack
    def test_reverse(self, input, expect):
        res = reverse_1(list(input))
        assert res == expect
        res = reverse_2(list(input))
        assert res == expect
        res = reverse_3(list(input))
        assert res == expect

    @data(
        [[1,2,3,4], 2, [[1,2,],[3,4]]],
    )
    @unpack
    def test_to_list2_by_row(self, input, ncol, expect):
        res = to_list2_by_row(list(input), ncol)
        assert res == expect

    @data(
        [[1,2,3,4], 2, [[1,3,],[2,4]]],
    )
    @unpack
    def test_to_list2_by_col(self, input, ncol, expect):
        res = to_list2_by_col(list(input), ncol)
        assert res == expect

    @data(
        [INPUT_1, [[1,4],[2,5],[3,6]]],
    )
    @unpack
    def test_transpose_list2(self, input, expect):
        res = transpose_list2(input)
        assert res == expect
    
    def test_turn_list2(self):
        input = [
            [1,2,3],
            [4,5,6],
        ]
        res = turn_list2(input)
        assert res == [[4,1],[5,2],[6,3]]
        res = turn_list2(res)
        assert res == [[6,5,4],[3,2,1]]
        res = turn_list2(res)
        assert res == [[3,6],[2,5],[1,4]]
        res = turn_list2(res)
        assert res == input

    @data(
        # 1x3 -> 4x3
        [[0,4,2], [[0,1,0],[0,1,0],[0,1,1],[0,1,1]]],
    )
    @unpack
    def test_linear_hyperspace(self, input, expect):
        res = linear_hyperspace(input)
        assert res == expect