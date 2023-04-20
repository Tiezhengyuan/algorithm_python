
from tests.helper import *
from recursion.memorization import *

@ddt
class TestMemorization(TestCase):

    @data(
        [[5,2], 7],
        [[5,200,2], 7],
        [[5,94,2], 99],
    )
    @unpack
    def test_add_unitl_100(self, input,expect):
        res = add_unitl_100(input)
        assert res == expect


    @data(
        [5, 3],
        [100, 21],
    )
    @unpack
    def test_golomb(self, input,expect):
        res = golomb(input)
        assert res == expect