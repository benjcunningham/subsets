import srt
import pydub

class SRT():

    def __init__(self, path):

        self.path = path
        self.subs = self.read(path)


    def read(self, path, encoding):

        with open(path, "r", encoding=encoding) as file:
            subs = list(srt.parse(file.read()))

        return subs


    def split_file(self, path, **kwargs):

        audio = pydub.AudioSegment.from_file(path, **kwargs)

        msec = lambda time: time.total_seconds() * 1000
        stamp = lambda sub: (msec(sub.start), msec(sub.end))

        splits = [stamp(sub) for sub in self.subs]

        splice = lambda split: audio[split[0]:split[1]]
        audios = [splice(split) for split in splits]

        return audios


    def __len__(self):

        return len(self.subs)


    def __getitem__(self, index):

        return self.subs[index]


    def __iter__(self):

        for sub in self.subs:
            yield sub
