"""
This file contains generally-useful utility functions.
"""
from pathlib import Path
import os

def get_src_files():
    """
    Returns a list of strings that contains paths to all the source (.py) files
    in the 'src' directory and its subdirectories. This is useful for getting a
    list of source files to upload to Neptune.
    """
    # In order to do the globbing in a platform-independent manner, I'm using pathlib.

    # If you want files other than *.py to be counted as source files, you will need to alter the glob expression.
    list_of_concrete_paths = Path("src").glob("**/*.py") # See here for an example of how this works: https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob
    # The elements of the list are path-like objects. To turn those into strings (in the style of the local platform), we use the os.fspath function.
    return [os.fspath(path) for path in list_of_concrete_paths]

