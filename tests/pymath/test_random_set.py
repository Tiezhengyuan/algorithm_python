from tests.helper import *
from pymath.random_set import RandomSet

@ddt
class TestRandomSet(TestCase):

    def test_(self):
        obj = RandomSet()
        res = obj.insert(1)
        assert res == True
        res = obj.remove(2)
        assert res == False
        res = obj.insert(2)
        assert res == True
        res = obj.remove(1)
        assert res == True
        res = obj.insert(2)
        assert res == False

        res = obj.get_random()
        assert res == 2

        res = obj.shuffle()
        assert res == [2]
