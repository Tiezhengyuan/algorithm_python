from tests.helper import *
from process.two_points import TwoPoints as c


@ddt
class TestDeleteArray(TestCase):

    @data(
        [[1,3,5], 0, [1,3,5] ],
        [[1,3,5], 1, [3,1,5] ],
        [[1,3,5], 2, [5,1,3] ],
        [[1,3,5], -1, [5,1,3] ],
        [[1,3,5], -2, [3,1,5] ],
        [[1,3,5], -3, [1,3,5] ],
        [[1],0, [1]]
    )
    @unpack
    def test_move_forward(self, input, index, expect):
        c.move_forward(input, index)
        assert input == expect

    @data(
        [[1,3,5], 0, [3,5,1] ],
        [[1,3,5], 1, [1,5,3] ],
        [[1,3,5], 2, [1,3,5] ],
        [[1,3,5], -1, [1,3,5] ],
        [[1,3,5], -2, [1,5,3] ],
        [[1,3,5], -3, [3,5,1] ],
        [[1],0, [1]]
    )
    @unpack
    def test_move_backward(self, input, index, expect):
        c.move_backward(input, index)
        assert input == expect



    @data(
        [[0,1,2,2,3,0,4,2], 2, [0, 1, 0, 4, 3, '_', '_', '_'], 5],
        [[0,1,2,2,3,0,4,2], 1, [0, 2, 2, 2, 3, 0, 4, '_'], 7],
        [[0,1,2,2,3,0,4,2], 10, [0,1,2,2,3,0,4,2], 8],
    )
    @unpack
    def test_remove_element(self, nums, val, expect, expect_k):
        res = c.remove_element(nums, val)
        assert nums == expect
        assert res == expect_k
    

    @data(
        [[0,1,2,2,3,0,4,2], 2, [0, 1, 3, 0, 4, '_', '_', '_'], 5],
        [[0,1,2,2,3,0,4,2], 1, [0, 2, 2, 3, 0, 4, 2, '_'], 7],
        [[0,1,2,2,3,0,4,2], 10, [0,1,2,2,3,0,4,2], 8],
    )
    @unpack
    def test_remove_element_2(self, nums, val, expect, expect_k):
        res = c.remove_element_2(nums, val)
        assert nums == expect
        assert res == expect_k

    @data(
        [[1,1,2], [1,2,'_'], 2],
        [[0,0,1,1,1,2,2,3,3,4], [0,1,2,3,4,'_','_','_','_','_'], 5]
    )
    @unpack
    def test_remove_duplicates(self, nums, expect_arr, expect):
        res = c.remove_duplicates(nums)
        assert nums == expect_arr
        assert res == expect

    @data(
        [[1,1,1,2,2,3], [1,1,2,2,3,'_'], 5],
        [[0,0,1,1,1,1,2,3,3], [0,0,1,1,2,3,3,'_','_'], 7],
    )
    @unpack
    def test_remove_duplicates_2(self, nums, expect_arr, expect):
        res = c.remove_duplicates_2(nums, 2)
        assert nums == expect_arr
        assert res == expect

    @data(
        [[1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]],
        [[1,], 1, [], 0, [1]],
        [[0,], 0, [1], 1, [1]],
    )
    @unpack
    def test_merge_sorted(self, nums1, m, nums2, n, expect):
        c.merge_sorted(nums1, m, nums2, n)
        assert nums1 == expect

    @data(
        [[1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]],
        [[-1,-100,3,99], 2, [3,99,-1,-100]],
    )
    @unpack
    def test_rotate(self, nums, k, expect):
        c.rotate(nums, k)
        assert nums == expect