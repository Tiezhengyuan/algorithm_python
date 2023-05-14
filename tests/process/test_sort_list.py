
from tests.helper import *
from process.sort_list import *

INPUT_1 = [4,2,7,1,3]
RESULT_1 = [1,2,3,4,7]

INPUT_2 = [4,2,7,1,2,3]
RESULT_2 = [1,2,2,3,4,7]

INPUT_3 = [[4,2,1],[1,0,0]]

@ddt
class TestSortArray(TestCase):

    @data(
        [INPUT_1, RESULT_1],
        [INPUT_2, RESULT_2],
        [[], []],
    )
    @unpack
    def test_bubble_sort(self, input, expect):
        res = bubble_sort(input)
        assert res == expect

    @data(
        [INPUT_1, RESULT_1],
        [INPUT_2, RESULT_2],
        [[], []],
    )
    @unpack
    def test_selection_sort(self, input, expect):
        res = selection_sort(input)
        assert res == expect

    @data(
        [INPUT_1, RESULT_1],
        [INPUT_2, RESULT_2],
        [[], []],
    )
    @unpack
    def test_insertion_sort(self, input, expect):
        res = insertion_sort(input)
        assert res == expect

    @data(
        [deepcopy(INPUT_3), [[0,0,1],[1,2,4]]],
    )
    @unpack
    def test_sort_list2(self, input, expect):
        sort_list2(input)
        assert input == expect