"""Test writers
"""
import unittest
import tempfile
from subsets import Subset, write


class TestWrite(unittest.TestCase):
    """Tests of write functions"""

    def setUp(self):

        args = {
            "subs": "tests/test_files/nge.srt",
            "audio": "tests/test_files/nge.aac"
        }

        self.sub = Subset(**args)
        self.tmp_dir = tempfile.gettempdir()


    def test_write_splits(self):
        """Write audio splits to disk"""

        paths = write.write_splits(self.sub, self.tmp_dir, "ogg")

        self.assertEqual(len(paths), len(self.sub))


if __name__ == "__main__":
    unittest.main()
