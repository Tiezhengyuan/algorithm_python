
from tests.helper import *
from recursion.sequence import *

@ddt
class TestDNA(TestCase):

    @data(
        [5, 120]
    )
    @unpack
    def test_factorial(self, input,expect):
        res = factorial(input)
        assert res == expect


    @data(
        [0, 0],
        [1, 1],
        [2, 1],
        [3, 2],
        [5, 5],
        [10, 55],
    )
    @unpack
    def test_fibonacci(self, input,expect):
        res = fibonacci(input)
        assert res == expect


    @data(
        [0, 10, [0,2,4,6,8,10]],
    )
    @unpack
    def test_get_sequence(self, low, high, expect):
        res = get_sequence(low, high)
        assert list(res) == expect

    @data(
        [0, 10, 55]
    )
    @unpack
    def test_get_sum(self, low, high,expect):
        res = get_sum(low, high)
        assert res == expect

    @data(
        [1, 1],
        [7, 28],
    )
    @unpack
    def test_triangle_numbers(self, input, expect):
        res = triangle_numbers(input)
        assert res == expect