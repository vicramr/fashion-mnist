# notebooks
This directory is where Jupyter notebooks should be located.

## Guidelines
Of course, there are some guidelines that must be followed in order to ensure that import paths and file paths all work correctly. The minimum requirements are that each notebook must run the following block before trying to do anything else:
```python
import sys
import os
assert "" in sys.path
os.chdir("..")
```
Here's what's going on. As far as I can tell, IPython inserts the empty string `""` into `sys.path` upon startup. This instructs Python to [search the current working directory](https://docs.python.org/3.6/library/sys.html#sys.path) for files to import. In addition, regardless of what your directory was when you ran `jupyter notebook` to start the Jupyter server, it appears that the notebook's working directory will be set to the directory that the notebook file itself. So what the above block does is change the directory from `notebooks` to the project root directory, which is what we want the working directory to be and which will also ensure that import statements are resolved correctly.

**I do not know whether any of the above is portable.** I wasn't able to find it in the Jupyter or IPython documentation, although I will keep looking. The line `assert "" in sys.path` is just there to ensure that in the event my assumptions don't hold, an exception will be thrown immediately.
