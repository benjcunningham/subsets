"""Subsets
"""

import argparse
import sys
from .subset import Subset


def get_args():
    """Set CLI arguments

    Sets the command line interface arguments.
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("--subs", metavar="path to subtitles",
                        help="Subtitle to use.")

    parser.add_argument("--audio", metavar="path to audio",
                        help="Audio to use.")

    parser.add_argument("--format", metavar="audio format",
                        help="Format of audio.", required=False)

    parser.add_argument("--encoding", metavar="subtitle encoding",
                        help="Encoding of subtitle.", required=False)

    return parser


def create_kwargs(args):
    """Create kwarg dictionaries

    Creates keyword arg dictionaries.
    """

    kwargs = {"subs_kwargs": {}, "audio_kwargs": {}}

    if hasattr(args, "encoding"):
        kwargs["subs_kwargs"]["encoding"] = args.encoding

    if hasattr(args, "format"):
        kwargs["audio_kwargs"]["format"] = args.format

    return kwargs


def create_subset(args):
    """Create a Subset object

    Creates a Subset object based on the CLI args.
    """

    kwargs = create_kwargs(args)
    sub = Subset(args.subs, args.audio, **kwargs)

    return sub


def main():
    """Create and write a Subset to disk

    Parses CLI arguments to create a Subset object. Writes the resulting
    subtitles and audio to disk.
    """

    parser = get_args()
    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)

    sub = create_subset(args)

    # TODO: Write subs to CSV, audio splits to file


if __name__ == "__main__":
    main()
