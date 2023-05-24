from tests.helper import *
from search.slide_window import *

@ddt
class TestSlideWindow(TestCase):

    @data(
        ['ATCGAG', 3, ['ATC','TCG','CGA','GAG']],
    )
    @unpack
    def test_fixed_window(self, input, length,expect):
        obj = k_mers(input, length, 0)
        res = [i[1] for i in obj]
        assert res == expect

    @data(
        ['gotxxotgxdogt','got', [0]],
    )
    @unpack
    def test_countAnagram(self, input, target, expect):
        res = countAnagram(input, target)
        assert res == expect

    @data(
        [[3, 4, 2, 5, 1],3,[2, 5, 1]],
        [[1,2,3,4],3,[1,2,3]],
    )
    @unpack
    def test_min_sum(self, input, k, expect):
        res = min_sum(input,k)
        assert res == expect

    @data(
        [[2,6,7], [(0, 2), (1, 2), (2, 2), (1, 1), (0, 1), (1, 1), (0, 0), (1, 1)]],
    )
    @unpack
    def test_two_points_shrink(self, input, expect):
        res = two_points_shrink(input, 0, len(input)-1)
        # print(list(res))
        assert list(res) == expect

    @data(
        [[2,3,1,2,4,3],7, 2],
        [[1,4,4],4,1],
        [[1,1,1,1,1,1,1,1],11,0],
    )
    @unpack
    def test_minSubArrayLen(self, input, target, expect):
        res = minSubArrayLen(input, target)
        assert res == expect

    # @data(
    #     ["abcabcbb", 0,1, ['abc']],
    #     ["abcabcbb", 5,6, ['abc']],
    #     ['wwww', 1,2, ['w']],
    #     ['wwww', 3,4, ['w']],
    #     ['wwwcw', 4,5, ['cw']],
    #     ['wwwcw', 3,4, ['wc']],
    #     ['w', 0,1, ['w']],
    #     ['wwcwba',3,4, ['cwba']],
    #     ['wwwwba',3,4, ['wba']],
    #     ['waw', 1,2, ['wa', 'aw']],
    # )
    # @unpack
    # def test_LongestNoneRepeat(self, input, start, end,expect):
    #     output = []
    #     LongestNoneRepeat(input, start, end, output)
    #     res = [input[i[0]:i[1]] for i in output]
    #     assert res == expect


    # @skip
    # @data(
    #     ["abcabcbb", 3],
    #     ["bbbbb", 1],
    #     ["pwwkew", 3],
    # )
    # @unpack
    # def test_lengthOfLongestSubstring(self, input, expect):
    #     res = lengthOfLongestSubstring(input)
    #     assert res == expect

    @data(
        ["barfoothefoobarman", ["foo","bar"], [0,9]],
        ["wordgoodgoodgoodbestword", ["word","good","best","word"], []],
        ["barfoofoobarthefoobarman", ["bar","foo","the"], [6,9,12]],
    )
    @unpack
    def test_findSubstring(self, input, words, expect):
        res = findSubstring(input, words)
        assert res == expect

    @data(
        ["ADOBECODEBANC", "ABC", 0, ["ADOBEC"]],
        ["ADOBECODEBANC", "ABC", 12, ["BANC"]],
    )
    @unpack
    def test_condition_wild_expand(self, s, t, start, expect):
        obj = condition_wild_expand(s, start, start+1, t)
        res = [s[start:end] for start,end in obj]
        # print(res)
        assert res == expect

    @data(
        ["ADOBECODEBANC", "ABC", "BANC"],
        ['a','a', 'a'],
        ['a','aa', ''],
    )
    @unpack
    def test_minWindowSubstring(self, input, target,expect):
        res = minWindowSubstring(input,target)
        assert res == expect