"""Write utilities
"""
import os


def write_splits(sub, path, fmt, prefix="subtitle", **kwargs):
    """Write Subset splits to disk

    Writes splits in a Subset object to disk.
    """

    files = [f"{prefix}_{sub.index}.{fmt}" for sub in sub.subs]
    paths = [os.path.join(path, file) for file in files]

    for audio, file in zip(sub.splits, paths):
        audio.export(file, fmt, **kwargs)

    return paths
