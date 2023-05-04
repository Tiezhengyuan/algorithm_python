
from tests.helper import *
from sort.sort_array import SortArray

INPUT_1 = [4,2,7,1,3]
RESULT_1 = [1,2,3,4,7]

INPUT_2 = [4,2,7,1,2,3]
RESULT_2 = [1,2,2,3,4,7]


@ddt
class TestSortArray(TestCase):

    @data(
        [INPUT_1, RESULT_1],
        [INPUT_2, RESULT_2],
        [[], []],
    )
    @unpack
    def test_bubble_sort(self, input, expect):
        res = SortArray.bubble_sort(input)
        assert res == expect

    @data(
        [INPUT_1, RESULT_1],
        [INPUT_2, RESULT_2],
        [[], []],
    )
    @unpack
    def test_selection_sort(self, input, expect):
        res = SortArray.selection_sort(input)
        assert res == expect

    @data(
        [INPUT_1, RESULT_1],
        [INPUT_2, RESULT_2],
        [[], []],
    )
    @unpack
    def test_insertion_sort(self, input, expect):
        res = SortArray.insertion_sort(input)
        assert res == expect