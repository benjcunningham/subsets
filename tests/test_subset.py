import unittest
import pydub
import srt
from subsets import Subset


class TestSubset(unittest.TestCase):

    def setUp(self):

        self.path = {
            "subs": "tests/test_files/test_sub.srt",
            "audio": "tests/test_files/gallop.ogg"
        }


    def test_read_subs(self):
        """Read subtitle file into object"""

        sub = Subset()
        sub.read_subs(self.path["subs"])

        self.assertIn("subs", dir(sub))
        self.assertIsInstance(sub.subs, list)
        self.assertIsInstance(sub.subs[0], srt.Subtitle)


    def test_read_audio(self):
        """Read audio file into object"""

        sub = Subset()
        sub.read_audio(self.path["audio"])

        self.assertIn("audio", dir(sub))
        self.assertIsInstance(sub.audio, pydub.AudioSegment)


    def test_split(self):
        """Split audio based on integer bounds"""

        sub = Subset()
        sub.read_audio(self.path["audio"])

        bound = (0, 100)
        split = sub._split(bound)

        self.assertIsInstance(split, pydub.AudioSegment)
        self.assertEqual(len(split), 100)


    def test_split_audio(self):
        """Split audio based on subtitles"""

        sub = Subset()
        sub.read_subs(self.path["subs"])
        sub.read_audio(self.path["audio"])
        sub.split_audio()

        self.assertIn("splits", dir(sub))
        self.assertIsInstance(sub.splits, list)
        self.assertEqual(len(sub.splits), len(sub.subs))
        self.assertIsInstance(sub.splits[0], pydub.AudioSegment)


if __name__ == "__main__":
    unittest.main()
