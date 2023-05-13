from tests.helper import *
from basic.iterate_list2 import *

INPUT_1 = [[1,2,3],[4,5,6]]
INPUT_2 = [[1,2,3],[4,5,6],[7,8,9]]
INPUT_3 = [
    [0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,1,0,0,0,1,1,0,1,0],
    [0,1,0,1,1,0,1,1,1,1,1,1]
]

@ddt
class TestList2(TestCase):

    @data(
        [INPUT_1, [1,2,3,4,5,6]],
    )
    @unpack
    def test_by_row_forward(self, input, expect):
        res = by_row_forward(input)
        assert list(res) == expect

    @data(
        [INPUT_1, [6,5,4,3,2,1]],
    )
    @unpack
    def test_by_row_backward(self, input, expect):
        res = by_row_backward(input)
        assert list(res) == expect

    @data(
        [INPUT_1, [1,4,2,5,3,6]],
    )
    @unpack
    def test_by_col_top_left(self, input, expect):
        res = by_col_top_left(input)
        assert list(res) == expect

    @data(
        [INPUT_1, [1,2,3,6,5,4]],
        [INPUT_2, [1,2,3,6,5,4,7,8,9]],
    )
    @unpack
    def test_by_row_snake(self, input, expect):
        res = by_row_snake(input)
        assert list(res) == expect

    @data(
        [INPUT_1, [1,4,5,2,3,6]],
    )
    @unpack
    def test_by_col_snake(self, input, expect):
        res = by_col_snake(input)
        assert list(res) == expect

    @data(
        [INPUT_2, (1,1), [(1,1),], 8],
    )
    @unpack
    def test_traverse(self, input, start, visited, expect):
        res = traverse(input, start, visited)
        assert len(list(res)) == expect

    @data(
        [INPUT_3, (0,0), 16],
        [INPUT_3, (2,8), 0],
    )
    @unpack
    def test_traverse_binary(self, input, start, expect):
        res = traverse_binary(input, start)
        assert len(list(res)) == expect
