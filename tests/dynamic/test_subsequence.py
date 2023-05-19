
from tests.helper import *
from dynamic.subsequence import *

@ddt
class TestSubsequence(TestCase):

    @data(
        ["abc", "ahbgdc", True],
        ["axc", "ahbgdc", False]
    )
    @unpack
    def test_isSubsequence(self, s, t, expect):
        res = isSubsequence(s, t)
        assert res == expect