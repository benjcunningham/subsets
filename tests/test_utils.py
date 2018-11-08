import unittest
import datetime
import srt
from subsets import utils

class TestUtils(unittest.TestCase):

    def setUp(self):

        path = "tests/test_files/test_sub.srt"
        with open(path, "r") as file:
            self.subs = list(srt.parse(file.read()))


    def test_msec(self):
        """Convert to milliseconds"""

        expect = 2.5e5
        time = datetime.timedelta(milliseconds=expect)
        result = utils.msec(time)

        self.assertEqual(result, expect)


    def test_bound(self):
        """Get time bounds of subtitle"""

        expect = (137440, 140375)
        result = utils.bound(self.subs[0])

        self.assertEqual(result, expect)


if __name__ == "__main__":
    unittest.main()
