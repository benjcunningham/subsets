"""MKV object
"""
import json
from subprocess import run, PIPE, DEVNULL


class MKV():
    """MKV object

    Handles reading streams of data from an MKV file.
    """

    def __init__(self, path):

        self.path = path

        kinds = ["a", "v", "s"]
        streams = [self.extract_metadata(kind) for kind in kinds]

        self.streams = sum(streams, [])


    def extract_metadata(self, kind):
        """Extract MKV stream metadata

        Extracts all the metadata for streams of a particular kind in
        the input file (i.e., audio, video, or subtitle streams).
        """

        cmd = ["ffprobe", "-show_streams", "-select_streams", kind,
               "-print_format", "json", self.path]

        resp = run(cmd, stdout=PIPE, stderr=DEVNULL)
        data = [stream for stream in json.loads(resp.stdout)["streams"]]
        streams = [MKVStream(self.path, stream) for stream in data]

        return streams


    def __iter__(self):

        for stream in self.streams:
            yield stream


class MKVStream():
    """MKVStream object

    Wraps metadata describing a single stream in an MKV file.
    """

    def __init__(self, path, data):

        self.path = path
        self.data = data


    def write(self, path):
        """Write stream to disk

        Uses ffmpeg to write a copy of a stream to disk as a standalone
        file.
        """

        stream = "0:{}".format(self.data["index"])

        cmd = ["ffmpeg", "-i", self.path, "-map", stream, "-c", "copy",
               path]

        run(cmd, stdout=PIPE, stderr=DEVNULL)

        return path


    def __getattr__(self, name):

        return self.data[name]
