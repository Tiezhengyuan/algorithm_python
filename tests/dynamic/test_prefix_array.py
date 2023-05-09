from tests.helper import *
from dynamic.prefix_array import PrefixArray as c

@ddt
class TestCount(TestCase):

    @data(
        [[1,2,3,4], [24,12,8,6]],
    )
    @unpack
    def test_product_except_self(self, input, expect):
        res = c.product_except_self_1(input)
        assert res == expect
        res = c.product_except_self_2(input)
        assert res == expect
        res = c.product_except_self_3(input)
        assert res == expect
        res = c.product_except_self_4(input)
        assert res == expect
