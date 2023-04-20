
from tests.helper import *
from recursion.files import *

@ddt
class TestDNA(TestCase):

    def test_find_dir(self):
        input = os.path.dirname(os.path.dirname(__file__))
        output = []
        find_dir(input, output)
        # print(output)

    def test_find_files(self):
        input = os.path.dirname(os.path.dirname(__file__))
        output = []
        find_files(input, output)
        print(output)