"""Subset object
"""
import srt
import pydub
import pandas as pd
from subsets.utils import bound


class Subset():
    """Subset object

    Handles reading subtitles and audio into a unified object. Also
    provides methods for splitting audio based on the timestamps of the
    loaded subtitles.
    """

    def __init__(self, subs, audio,
                 subs_kwargs=None,
                 audio_kwargs=None):

        self.subs = None
        self.audio = None
        self.splits = None

        subs_kwargs = subs_kwargs or {}
        audio_kwargs = audio_kwargs or {}

        self.read_subs(subs, **subs_kwargs)
        self.read_audio(audio, **audio_kwargs)
        self.split_audio()


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
        self.splits = [self._split(bnd) for bnd in bounds]

        return self


    def to_table(self):
        """Convert subs to tabular format

        Converts the object's subtitles to a data frame.
        """

        subs_dict = [sub.__dict__ for sub in self.subs]
        table = pd.DataFrame.from_dict(subs_dict)

        return table


    def _split(self, bounds):
        """Split audio

        Split the object's audio given a tuple of bounds (i.e., start
        and end timestamps).
        """

        start, end = bounds

        return self.audio[start:end]


    def __len__(self):

        return len(self.splits)


    def __getitem__(self, index):

        return self.splits[index]


    def __iter__(self):

        for split in self.splits:
            yield split
