"""
This file contains tests that involve running Jupyter notebooks.
"""

import os

import pytest
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

class PushPop:
    """
    This class is a context manager which implements pushd/popd semantics.
    Upon entry, this will save the current working directory and change
    the working directory to the one specified in the constructor.
    Upon exit, the working directory will be changed back to the old one.

    Note: __enter__ doesn't return anything so you can't use the 'with __ as __:'
    syntax. Just use 'with __:'.
    """
    def __init__(self, newdir):
        """
        newdir must be a path-like object: https://docs.python.org/3.6/glossary.html#term-path-like-object
        """
        self.newdir = newdir

    def __enter__(self):
        self.olddir = os.getcwd()
        os.chdir(self.newdir)
    
    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.olddir)
        return False
        # We return False to signal that we didn't handle an exception, if any. See here:
        # https://docs.python.org/3.6/reference/datamodel.html#object.__exit__

def _notebook_run(path):
    """
    This function runs a notebook, uses nbformat to collect the output, and
    if there's any exception in the notebook, a CellExecutionError exception
    will be raised.

    path is the path to the .ipynb file you want to test.
    There is no return value.

    This function is modifed from the following blog post:
    https://blog.thedataincubator.com/2016/06/testing-jupyter-notebooks/
    However, this pull request for the nbconvert docs mentions potential encoding
    issues when writing a notebook to a file: https://github.com/jupyter/nbconvert/pull/921/
    I could not find a command-line option to specify the encoding with which the notebook 
    would be written out, so instead I followed the instructions here to sidestep the
    whole issue and do it all in memory rather than invoking the nbconvert CLI:
    https://nbconvert.readthedocs.io/en/latest/execute_api.html

    TODO right now, we've specifically passing the execution path so the tests don't fail.
    Might want to also assert that some situations DO cause failures.
    """

    with open(path, encoding="utf-8") as f:  # The notebooks should be UTF-8 when committed to git, so this is a safe assumption.
        nb = nbformat.read(f, as_version=4) # https://nbformat.readthedocs.io/en/latest/api.html#nbformat.read
        ep = ExecutePreprocessor(timeout=60) # The docs also specified kernel, but I think the default should be fine.
        execpath = os.path.dirname(path) # Execute the notebook in the notebook's parent dir
        ep.preprocess(nb, {"metadata": {"path": execpath}}) # This runs the notebook. If any cells throw an exception we'll get a CellExecutionError.
        # NOTE
        # I looked at the source for ExecutePreprocessor.preprocess; it's in directory 'nbconvert/preprocessors/execute.py'.
        # The "path" entry of the metadata dict will be the kernel's execution path.
        # This is explicitly grabbed out of the dict by the ExecutePreprocessor.setup_preprocessor context manager
        # (which is also in execute.py) and is passed as the 'cwd' argument to ExecutePreprocessor.start_new_kernel,
        # which is in turn forwarded to KernelManager.start_kernel. If I don't give the "path" metadata entry then
        # None will be passed to cwd. I wasn't quite willing to go further but my impression is that "path" is used
        # to set the working directory for the notebook's kernel. However, I do not know what the default action
        # would be; in particular, I don't know whether running a Jupyter notebook like normal would have semantics
        # similar to passing None to start_kernel, or whether Jupyter will always explicitly pass in the notebook's
        # parent directory.
        # For future reference, KernelManager is defined in 'jupyter_client/manager.py'.

@pytest.mark.parametrize(
    "dir,path_to_notebook", 
    [(".", os.path.join("notebooks", "test_paths.ipynb")), 
     ("..", os.path.join("fashion-mnist", "notebooks", "test_paths.ipynb")), 
     ("notebooks", "test_paths.ipynb"), 
     ("src", os.path.join("..", "notebooks", "test_paths.ipynb"))]
)
def test_paths(dir, path_to_notebook):
    """
    dir: before executing the notebook, the working directory will be changed to this.

    path_to_notebook: this is the path to 'notebooks/test_paths.ipynb' after changing the
    working directory to dir.
    """
    with PushPop(dir):
        assert os.path.isfile(path_to_notebook)
        _notebook_run(path_to_notebook)

def test_PushPop():
    """
    This test checks that PushPop indeed sets/resets the directory correctly.
    """
    olddir = os.getcwd()
    with PushPop("."):
        assert os.path.samefile(os.getcwd(), olddir)
    assert os.path.samefile(os.getcwd(), olddir)

    with PushPop(".."):
        assert os.path.samefile(
            os.getcwd(),
            os.path.join(olddir, "..")
        )
    assert os.path.samefile(os.getcwd(), olddir)

    with PushPop("notebooks"):
        assert os.path.samefile(
            os.getcwd(),
            os.path.join(olddir, "notebooks")
        )
    assert os.path.samefile(os.getcwd(), olddir)

    try:
        with PushPop("src"):
            assert os.path.samefile(
                os.getcwd(),
                os.path.join(olddir, "src")
            )
            raise RuntimeError
        assert False # control should not reach here
    except RuntimeError:
        assert os.path.samefile(os.getcwd(), olddir)
    assert os.path.samefile(os.getcwd(), olddir)
