"""Write utilities
"""
import os


def write_splits(sub, path, format, prefix="subtitle", **kwargs):
    """Write Subset splits to disk

    Writes splits in a Subset object to disk.
    """

    files = [f"{prefix}_{audio.index}.{format}" for audio in sub.audio]
    paths = [os.join.path(path, file) for file in files]

    for audio, path in enumerate(subs.splits, paths):
        audio.export(path, format=format, **kwargs)

    return paths
