"""Test MKV classes
"""
import unittest
import os
import tempfile
from subsets.mkv import MKV, MKVStream


class TestMKV(unittest.TestCase):
    """Tests of MKV objects"""

    def setUp(self):

        self.path = "tests/test_files/nge.mkv"
        self.mkv = MKV(self.path)


    def test_stream_type(self):
        """Streams are accessible as iterable list"""

        self.assertIsInstance(self.mkv.streams, list)


    def test_stream_length(self):
        """Correct number of streams are found"""

        self.assertEqual(len(self.mkv.streams), 3)


    def test_stream_element_type(self):
        """Individual streams are MKVStream objects"""

        for stream in self.mkv.streams:
            self.assertIsInstance(stream, MKVStream)


    def test_iterator(self):
        """Iterating object yields MKVStreams"""

        for stream in self.mkv:
            self.assertIsInstance(stream, MKVStream)


class TestMKVStream(unittest.TestCase):
    """Test of MKVStream objects"""

    def setUp(self):

        self.path = "tests/test_files/nge.mkv"
        self.mkv = MKV(self.path)
        self.tmp_dir = tempfile.gettempdir()


    def test_writing(self):
        """Stream can be written with ffmpeg"""

        for stream in self.mkv:

            codec = stream.codec_type

            if codec == "audio":
                ext = "ogg"
            elif codec == "video":
                ext = "mp4"
            elif codec == "subtitle":
                ext = "ssa"

            fname = "{}.{}".format(stream.index, ext)
            tmp = os.path.join(self.tmp_dir, fname)

            stream.write(tmp)

            self.assertTrue(os.path.isfile(tmp))
