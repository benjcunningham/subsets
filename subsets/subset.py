import srt
import pydub


class Subset():

    def read_subs(self, path, **kwargs):

        with open(path, "r", **kwargs) as file:
            subs = list(srt.parse(file.read()))

        self.subs = subs

        return self


    def read_audio(self, path, **kwargs):

        self.audio = pydub.AudioSegment.from_file(path, **kwargs)

        return self


    def split_audio(self):

        msec = lambda time: time.total_seconds() * 1000
        stamp = lambda sub: (msec(sub.start), msec(sub.end))
        splice = lambda split: self.audio[split[0]:split[1]]

        splits = [stamp(sub) for sub in self.subs]
        self.splits = [splice(split) for split in splits]

        return self


    def __len__(self):

        return len(self.splits)


    def __getitem__(self, index):

        return self.splits[index]


    def __iter__(self):

        for split in self.splits:
            yield split
