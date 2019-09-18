"""
This is a special file used by pytest. Pytest specifically looks for a file called
conftest.py and loads it before loading other test files. You can find more info here:
https://docs.pytest.org/en/latest/writing_plugins.html#plugin-discovery-order-at-tool-startup

Here, we need to use conftest.py to ensure that sys.path is correct when trying to import
stuff from 'src' (i.e. our actual code that we're trying to test). When running our scripts
like normal, 'src' will be added to sys.path (see 'src/README.md'), but when running pytest,
it won't. (Using 'python -m pytest' wouldn't help because that would add the repo's root dir to
sys.path, rather than 'src'.) 
This will lead to issues when trying to import our code because the import statements assume that 'src'
is in sys.path. So before pytest tries to import our tests, which will import our source files,
which will try to import other source files, and so on, we need to add 'src' to sys.path.

This all relies on the assumption that pytest was invoked WITH THE REPO AS THE WORKING DIRECTORY.
"""
import sys
import os

absolute_path_to_src = os.path.realpath("src") # Only works because we're assuming that the current working directory is the repo's root directory.
if not os.path.isdir(absolute_path_to_src):
    sys.exit("Pytest must be invoked with \"python -m pytest\" in the repo's root directory. Exiting now.")
sys.path.insert(0, absolute_path_to_src) # sys.path is just a Python list, so this is calling list.insert
