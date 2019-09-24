"""
This file contains miscellaneous tests.
"""
import os

def test_trivial():
    """
    This is a trivial test that I'm using to check whether pytest can find the test
    files correctly.
    """
    assert True

from src import utils

def test_get_source_files():
    """
    Should probably be removed or altered, but this does help test that pytest is
    importing correctly.
    """
    list_of_files = utils.get_source_files()
    assert os.path.join("drivers", "experiment1.py") in list_of_files
    assert os.path.join("src", "utils.py") in list_of_files
    assert os.path.join("drivers", "initialize.py") in list_of_files
    assert os.path.join("notebooks", "EDA.ipynb") in list_of_files

    files_minus_notebooks = utils.get_source_files(False)
    assert os.path.join("notebooks", "EDA.ipynb") not in files_minus_notebooks
    assert os.path.join("drivers", "experiment1.py") in files_minus_notebooks
    assert os.path.join("src", "utils.py") in files_minus_notebooks
    assert os.path.join("drivers", "initialize.py") in files_minus_notebooks
