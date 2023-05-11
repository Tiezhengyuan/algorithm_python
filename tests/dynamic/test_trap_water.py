from tests.helper import *
from dynamic.trap_water import *

@ddt
class TestCount(TestCase):

    @data(
        [[0,1,0,2,1,0,1,3,2,1,2,1], 6],
        # [[3,2,0,0,0], 0],
        # [[0,3,6,4,7,2],2],
    )
    @unpack
    def test_(self, input, expect):
        res = trap_1(input)
        assert res == expect
        # res = trap_2(input)
        # assert res == expect