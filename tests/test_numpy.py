"""
This file contains tests that check any assumptions I'm making about how
numpy works. These are just sanity checks. Numpy is pretty complex so it's
good to check that it's actually doing what you want.
"""

import numpy as np

def test_neg_indexing():
    """
    Test that negative indexing works like I think it does.
    A rule of thumb I use is that the negative index can simply be replaced
    by the expression (size_of_corresponding_dimension + negative_index) and
    the behavior should be equivalent. For example, if 'arr' has shape (2,3,4)
    and we try to access 'arr[-1, -1:, -1]', that would be equivalent to
    accessing 'arr[1, 2:, 3]'.
    """
    arr1 = np.array(
        [1, 2, 3, 4, 5]
    )
    assert arr1[-2] == 4
    assert np.array_equal(arr1[:-1], np.array([1, 2, 3, 4]))
    assert np.array_equal(arr1[:-2], arr1[:3])
    arr2 = np.array(
        [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
    )
    # This next assert is just checking that I know how C-style array layout works
    assert np.array_equal(
        arr2.reshape(16, order="C"),
        np.arange(1, 17)
    )

    assert arr2[-3, -1] == 8

    assert np.array_equal(
        arr2[:-1, :-1],
        np.array(
            [[1, 2, 3],
             [5, 6, 7],
             [9, 10, 11]]
        )
    )
    
    assert np.array_equal(
        arr2[-1:, -1:],
        np.array([[16]])
    )

    assert np.array_equal(
        arr2[-3:-1, :],
        np.array(
            [[5, 6, 7, 8],
             [9, 10, 11, 12]]
        )
    )
