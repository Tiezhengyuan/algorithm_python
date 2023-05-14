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

    @data(
        # vertical first walk
        [3,3,(0,0), 'north_south', (1,0)],
        [3,3,(2,0), 'north_south', (1,1)],
        [3,3,(1,1), 'west_north', (0,2)],
        [3,3,(0,2), 'west_north', (1,2)],
        [3,3,(1,2), 'north_south', (2,2)],
        [3,3,(2,2), 'north_south', None],
        # horizontal first walk
        [3,3,(0,0), 'west_east', (0,1)],
        [3,3,(0,2), 'west_east', (1,1)],
        [3,3,(1,1), 'north_west', (2,0)],
        [3,3,(2,2), 'west_east', None],
    )
    @unpack
    def test_zigzag_step(self, nrow, ncol, start, walk, expect):
        res, _ = zigzag_step(nrow, ncol, start, walk)
        assert res == expect

    @data(
        [INPUT_2, True, [1,4,7,5,3,6,9]],
        [INPUT_2, False, [1,2,3,5,7,8,9]],
    )
    @unpack
    def test_zigzag_walk(self, input, vertical_first, expect):
        path = zigzag_walk(input, vertical_first)
        res = [input[x][y] for x,y in path]
        assert res == expect

    def test_zigzag_iteration(self):
        iter = zigzag_iteration(3,0,0,'north_south')
        res = next(iter)
        assert res == (1,0,'north_south')
        res = next(iter)
        assert res == (2,0,'north_south')
        res = next(iter)
        assert res == (1, 1, 'west_north')
        res = next(iter)
        assert res == (0, 2, 'west_north')
        res = next(iter)
        assert res == (1, 2, 'north_south')
        res = next(iter)
        assert res == (2, 2, 'north_south')
        res = next(iter)
        assert res == (1, 3, 'west_north')
        