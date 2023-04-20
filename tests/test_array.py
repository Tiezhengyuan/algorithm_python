
from tests.helper import *
from recursion.array import *

@ddt
class TestArray(TestCase):

    @data(
        [[1,[[]],2,[3,4,2],[[5,[],[7,[10,]]]],33], [1,2,3,4,5,7,10,33]]
    )
    @unpack
    def test_flat_array(self, input,expect):
        res = []
        flat_array(input, res)
        assert res == expect

    
    @data(
        [[1,2,3],[2,4,6]]
    )
    @unpack
    def test_double_array(self,input,expect):
        double_array(input)
        assert input == expect