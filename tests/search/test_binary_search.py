from tests.helper import *
from search.binary_search import BinarySearch as c

@ddt
class TestBinarySearch(TestCase):

    @data(
        [[],1, -1],
        [[1,2,3],1, 0],
        [[1,2,3],2, 1],
        [[1,2,3],3, 2],
        [[1,2,3],5, -1],
        [[1,2,3,4],1, 0],
        [[1,2,3,4],2, 1],
        [[1,2,3,4],3, 2],
        [[1,2,3,4],4, 3],
        [[1,2,3,4],5, -1],
    )
    @unpack
    def test_while(self, input,target, expect):
        res = c.while_search(input,target)
        assert res == expect

    @data(
        [[],1, -1],
        [[1,2,3],1, 0],
        [[1,2,3],2, 1],
        [[1,2,3],3, 2],
        [[1,2,3],5, -1],
        [[1,2,3,4],1, 0],
        [[1,2,3,4],2, 1],
        [[1,2,3,4],3, 2],
        [[1,2,3,4],4, 3],
        [[1,2,3,4],5, -1],
    )
    @unpack
    def test_recursion(self, input,target, expect):
        res = c.recursion_search(input,target)
        assert res == expect
    
    @data(
        [
            [4,10,11,25,30,33,40,50,52,56,61,75,82,89,95],
            [50,25,75,10,33,56,89,4,11,30,40,52,61,82,95],
        ],
        [[],[]],
        [[5],[5]],
        [[1,5],[1,5]],
        [[1,2,5],[2,1,5]],
    )
    @unpack
    def test_binary_iter(self, input, expect):
        res = c.binary_iter(input)
        assert res == expect