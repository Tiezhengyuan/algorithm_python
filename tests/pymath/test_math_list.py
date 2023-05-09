from tests.helper import *
from pymath.math_list import MathList as c

@ddt
class TestCount(TestCase):

    @data(
        [[3,2,5], 5],
        [[5], 5],
    )
    @unpack
    def test_max(self, input, expect):
        res = c.max_1(input)
        assert res == expect
        res = c.max_2(input)
        assert res == expect
        res = c.max_3(input)
        assert res == expect

    @data(
        [[3,2,5], 30],
        [[5], 5],
    )
    @unpack
    def test_product(self, input, expect):
        res = c.product_1(input)
        assert res == expect
        res = c.product_2(input)
        assert res == expect
        res = c.product_3(input)
        assert res == expect
        res = c.product_4(input)
        assert res == expect
        res = c.product_5(input)
        assert res == expect