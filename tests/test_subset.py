"""Test Subset class
"""
import unittest
import pydub
import srt
import pandas as pd
from subsets import Subset


class TestSubset(unittest.TestCase):
    """Tests of Subset objects"""

    def setUp(self):

        self.args = {
            "subs": "tests/test_files/nge.srt",
            "audio": "tests/test_files/nge.aac"
        }


    def test_read_subs(self):
        """Read subtitle file into object"""

        sub = Subset(**self.args)
        sub.read_subs(self.args["subs"])

        self.assertTrue(hasattr(sub, "subs"))
        self.assertIsInstance(sub.subs, list)
        self.assertIsInstance(sub.subs[0], srt.Subtitle)


    def test_read_audio(self):
        """Read audio file into object"""

        sub = Subset(**self.args)
        sub.read_audio(self.args["audio"])

        self.assertTrue(hasattr(sub, "audio"))
        self.assertIsInstance(sub.audio, pydub.AudioSegment)


    def test_split(self):
        """Split audio based on integer bounds"""

        sub = Subset(**self.args)

        bound = (0, 100)
        split = sub._split(bound)

        self.assertIsInstance(split, pydub.AudioSegment)
        self.assertEqual(len(split), 100)


    def test_split_audio(self):
        """Split audio based on subtitles"""

        sub = Subset(**self.args)
        sub.split_audio()

        self.assertTrue(hasattr(sub, "splits"))
        self.assertIsInstance(sub.splits, list)
        self.assertIsInstance(sub.splits[0], pydub.AudioSegment)
        self.assertEqual(len(sub.splits), len(sub.subs))


    def test_init(self):
        """Initialize object with subs and audio"""

        sub = Subset(**self.args)

        self.assertTrue(hasattr(sub, "subs"))
        self.assertTrue(hasattr(sub, "audio"))
        self.assertTrue(hasattr(sub, "splits"))
        self.assertIsInstance(sub.subs, list)
        self.assertIsInstance(sub.subs[0], srt.Subtitle)
        self.assertIsInstance(sub.audio, pydub.AudioSegment)
        self.assertIsInstance(sub.splits, list)
        self.assertIsInstance(sub.splits[0], pydub.AudioSegment)


    def test_init_kwargs(self):
        """Initialize object with kwargs"""

        subs_kwargs = {"encoding": "utf-8"}
        audio_kwargs = {"format": "aac"}
        sub = Subset(**self.args,
                     subs_kwargs=subs_kwargs,
                     audio_kwargs=audio_kwargs)

        self.assertTrue(hasattr(sub, "subs"))
        self.assertTrue(hasattr(sub, "audio"))
        self.assertTrue(hasattr(sub, "splits"))
        self.assertIsInstance(sub.subs, list)
        self.assertIsInstance(sub.subs[0], srt.Subtitle)
        self.assertIsInstance(sub.audio, pydub.AudioSegment)
        self.assertIsInstance(sub.splits, list)
        self.assertIsInstance(sub.splits[0], pydub.AudioSegment)


    def test_to_table(self):
        """Convert subs to data frame"""

        sub = Subset(**self.args)
        table = sub.to_table()

        self.assertIsInstance(table, pd.DataFrame)
        self.assertEqual(table.shape, (3, 5))


if __name__ == "__main__":
    unittest.main()
