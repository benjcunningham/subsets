"""Test writers
"""
import unittest
import tempfile
from subsets import write


class TestWrite(unittest.TestCase):
    """Tests of write functions"""

    def setUp(self):

        args = {
            "subs": "tests/test_files/test_sub.srt",
            "audio": "tests/test_files/gallop.ogg"
        }

        self.sub = Subset(**args)
        self.tmp_dir = tempfile.gettempdir()


    def test_write_splits(self):
        """Write audio splits to disk"""

        paths = write_splits(self.sub, self.tmp_dir, "ogg")

        self.assertEqual(len(paths), len(self.sub))


if __name__ == "__main__":
    unittest.main()
