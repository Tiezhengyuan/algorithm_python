from tests.helper import *
from process.dict_count import *


@ddt
class TestHash(TestCase):

    @data(
        [[3,2,3],3],
        [[2,2,1,1,1,2,2], 2],
    )
    @unpack
    def test_majority_element(self, nums, expect):
        res = majority_element(nums)
        assert res == expect

    @data(
        ['III', 3],
        ['LVIII', 58],
        ["MCMXCIV", 1994],
    )
    @unpack
    def test_roman_to_int(self, input, expect):
        res = roman_to_int(input)
        assert res == expect

