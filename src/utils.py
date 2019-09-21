"""
This file contains generally-useful utility functions.
"""
from pathlib import Path
import os

import numpy as np

from fashion_mnist_submodule.utils import mnist_reader

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

def load_raw_training_data():
    """
    This returns a 2-tuple of (X_train, y_train), with no preprocessing done.
    The results are regular numpy arrays.
    """
    path_to_data = os.path.join("fashion_mnist_submodule", "data", "fashion")
    X_train, y_train = mnist_reader.load_mnist(path_to_data, kind="train")
    assert X_train.shape == (60000, 784)
    assert X_train.dtype == np.dtype(np.uint8)
    assert np.amin(X_train) == 0
    assert np.amax(X_train) == 255

    assert y_train.shape == (60000,)
    assert y_train.dtype == np.dtype(np.uint8)
    assert np.amin(y_train) == 0
    assert np.amax(y_train) == 9

    return X_train, y_train

def load_raw_testing_data():
    path_to_data = os.path.join("fashion_mnist_submodule", "data", "fashion")
    X_test, y_test = mnist_reader.load_mnist(path_to_data, kind="t10k")
    assert X_test.shape == (10000, 784)
    assert X_test.dtype == np.dtype(np.uint8)
    assert np.amin(X_test) == 0
    assert np.amax(X_test) == 255

    assert y_test.shape == (10000,)
    assert y_test.dtype == np.dtype(np.uint8)
    assert np.amin(y_test) == 0
    assert np.amax(y_test) == 9

    return X_test, y_test    

def print_array_summary(arr):
    """
    Given a numpy or scipy array, prints a useful summary of that array.
    """
    print("Array shape:", arr.shape)
    print("Array dtype:", arr.dtype)
    print("Array object type:", arr.__class__.__name__)
