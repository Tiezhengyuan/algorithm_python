from tests.helper import *
from process.hash import Hash as c


@ddt
class TestHash(TestCase):

    @data(
        [[3,2,3],3],
        [[2,2,1,1,1,2,2], 2],
    )
    @unpack
    def test_majority_element(self, nums, expect):
        res = c.majority_element(nums)
        assert res == expect