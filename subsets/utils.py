"""Utility functions
"""


def msec(time):
    """Convert to milliseconds

    Convert a timedelta object to milliseconds.
    """

    return time.total_seconds() * 1000


def bound(sub):
    """Time bound a subtitle

    Given a Subtitle object, return a tuple containing its start and end
    times.
    """

    return (msec(sub.start), msec(sub.end))
