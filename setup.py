"""Subsets setup
"""
from setuptools import setup, find_packages


LONG_DESC = open("README.md").read()

setup(
    name="subsets",
    author="Ben Cunningham",
    author_email="benjamescunningham@gmail.com",
    description="Create speech-to-text datasets from subtitles",
    long_description=LONG_DESC,
    license="MIT",
    url="https://github.com/benjcunningham/subsets",
    test_suite="tests",
    install_requires=["srt",
                      "pydub"],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "subsets=subsets.__main__:main"
        ]
    },
)
