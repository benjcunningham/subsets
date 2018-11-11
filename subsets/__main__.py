"""Subsets
"""
import argparse
import os
import sys
from .subset import Subset
from .write import write_splits


def get_args():
    """Set CLI arguments

    Sets the command line interface arguments.
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("--subs", metavar="path to subtitles",
                        help="Subtitle to use.", required=True)

    parser.add_argument("--audio", metavar="path to audio",
                        help="Audio to use.", required=True)

    parser.add_argument("--path", metavar="path of output",
                        help="Where to write output.", required=True)

    parser.add_argument("--format", metavar="audio format",
                        help="Format of audio.", required=True)

    parser.add_argument("--prefix", metavar="output file prefix",
                        help="Prefix of output files.", required=False,
                        default="subtitle")

    parser.add_argument("--encoding", metavar="subtitle encoding",
                        help="Encoding of subtitle.", required=False)

    return parser


def create_kwargs(args):
    """Create kwarg dictionaries

    Creates keyword arg dictionaries.
    """

    kwargs = {
        "audio_kwargs": {
            "format": args.format},
        "subs_kwargs": {}}

    if hasattr(args, "encoding"):
        kwargs["subs_kwargs"]["encoding"] = args.encoding

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

    # Create the Subset object
    sub = create_subset(args)

    # Write the audio splits to disk
    paths = write_splits(sub, args.path, args.format, args.prefix)

    # Create a tabular view of the subtitle text
    table = sub.to_table()
    table["path"] = paths

    # Write the subtitle table to disk
    path = os.path.join(args.path, f"{args.prefix}.csv")
    table.to_csv(path, index=False)


if __name__ == "__main__":
    main()
