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

    return parser


def create_subset(args):
    """Create a Subset object

    Creates a Subset object based on the CLI args.
    """

    sub = Subset()

    sub.read_subs(args.subs)
    sub.read_audio(args.audio)
    sub.split_audio()

    return sub


def main():

    parser = get_args()
    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)

    sub = create_subset(args)

    # TODO: Write subs to CSV, audio splits to file


if __name__ == "__main__":
    main()
