"""
This file contains generally-useful utility functions.
"""
from pathlib import Path
import os

def get_source_files():
    """
    Returns a list of strings that contains paths to all the source (.py or .ipynb) files
    in the project. This is useful for getting a list of source files to upload to Neptune.
    """
    # In order to do the globbing in a platform-independent manner, I'm using pathlib.

    # If you want files other than *.py to be counted as source files, you will need to alter the glob expression.
    list_of_concrete_paths_src = Path("src").glob("**/*.py") # See here for an example of how this works: https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob
    # notebooks and driver scripts can't be nested in folders so we don't have to use **
    list_of_concrete_paths_notebooks = Path("notebooks").glob("*.ipynb")
    list_of_concrete_paths_drivers = Path("drivers").glob("*.py")
    # The elements of the lists are path-like objects. To turn those into strings (in the style of the local platform), we use the os.fspath function.
    pathlist_src = [os.fspath(path) for path in list_of_concrete_paths_src]
    pathlist_notebooks = [os.fspath(path) for path in list_of_concrete_paths_notebooks]
    pathlist_drivers = [os.fspath(path) for path in list_of_concrete_paths_drivers]
    return pathlist_src + pathlist_notebooks + pathlist_drivers
