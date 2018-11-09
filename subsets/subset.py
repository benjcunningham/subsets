import srt
import pydub
from subsets.utils import bound, msec


class Subset():

    def read_subs(self, path, **kwargs):
        """Read subtitle file

        Reads a subtitle file into the object as a Subtitle object. This
        is just a thin wrapper for srt.parse. Pass additional kwargs
        like the file encoding to properly handle opening the file.
        """

        with open(path, "r", **kwargs) as file:
            subs = list(srt.parse(file.read()))

        self.subs = subs

        return self


    def read_audio(self, path, **kwargs):
        """Read audio file

        Reads an audio file into the object. This is just a thin wrapper
        for pydub.AudioSegment.from_file, and by passing kwargs any file
        type handled by ffmpeg can be loaded.
        """

        self.audio = pydub.AudioSegment.from_file(path, **kwargs)

        return self


    def split_audio(self):
        """Split audio on subtitle bounds

        Splits the object's audio into separate objects corresponding to
        the timestamps of every subtitle.
        """

        bounds = [bound(sub) for sub in self.subs]
        self.splits = [self._split(bound) for bound in bounds]

        return self


    def _split(self, bound):
        """Split audio

        Split the object's audio given a tuple of bounds (i.e., start
        and end timestamps).
        """

        start, end = bound

        return self.audio[start:end]


    def __len__(self):

        return len(self.splits)


    def __getitem__(self, index):

        return self.splits[index]


    def __iter__(self):

        for split in self.splits:
            yield split
