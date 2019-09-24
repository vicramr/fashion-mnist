[![Travis Status](https://travis-ci.com/vicramr/fashion-mnist.svg?branch=master)](https://travis-ci.com/vicramr/fashion-mnist)
[![AppVeyor Status](https://ci.appveyor.com/api/projects/status/0xav4pxp0s6p2uvf/branch/master?svg=true)](https://ci.appveyor.com/project/vicramr/fashion-mnist/branch/master)

# fashion-mnist
This is a project using my [kaggle-template](https://github.com/vicramr/kaggle-template) project template.

The setup scripts are currently only written to work on Unix-based systems, which means that they should work correctly on Linux and macOS but not Windows. However, apart from those, everything is written to work cross-platform, including on Windows. Most of the setup is pretty straightforward to do on Windows, except perhaps setting the environment variables.

This project has Zalando's official [Fashion MNIST repository](https://github.com/zalandoresearch/fashion-mnist) as a submodule. This contains the actual dataset.

## Setup
In order to use this repo you will need to first install Anaconda or Miniconda.

There are 2 setup scripts required to fully set up a new environment. First run `setup1.sh`, then **source** `setup2.sh`. That means doing something like the following:
```bash
./setup1.sh
source setup2.sh
```
You should be using Bash as your shell, at least when sourcing `setup2.sh`. It may also work in other shells but I can't guarantee that it will.

`setup2.sh` requires you to have the Neptune API key handy so you can enter it. Don't worry, it won't be echoed! (See comments in `setup2.sh` for security concerns.) `setup2.sh` also activates the Conda environment so you won't have to do `conda activate fashionmnist` yourself. You should only have to run `setup1.sh` once per machine, but you'll need to source `setup2.sh` every time you start a new terminal session.

To get the Neptune API token, you'll need to create an account at neptune.ml. I recommend creating it using your Github account.

## Import Guidelines
Here I'm gonna lay out the ground rules for how to do Python imports in this project. My overall goal is to ensure that everything just works, with minimal configuration, in a consistent manner, and without any weird cases. Unfortunately, because of how the Python import system works, there will have to be tradeoffs. The cleanest way to ensure correctness is for me to lay out some rules that the entire codebase must follow:
1. All import statements should be written relative to the project root directory (that's the directory containing this README file). For example, if you want to import `src/utils.py` in some file `foo.py`, then - no matter where in the project directory `foo.py` is located - you should do `import src.utils` or `from src import utils`, rather than trying to do `import utils`.
2. All driver scripts must be located in `drivers`. Not outside of `drivers`, and not in a subdirectory of `drivers`. Here, "driver script" refers to any Python file that will be directly run as a script by the end user with `python path/to/drivers/filename.py`.
3. All driver scripts must run the following block before doing anything else (including importing anything):
```python
import initialize
initialize.initialize()
```

4. Jupyter notebooks are a little different. Imports in a notebook should still be written relative to the project root, but `initialize.initialize()` won't work correctly so there are some alternative rules. See `notebooks/README.md` for more information.

In addition, paths to files themselves should be written relative to the project root. `initialize.initialize()` will change the working directory to be the project root, ensuring that the paths will always be correct.

## Run Tests
We're using pytest for our tests. To run tests, invoke pytest while your working directory is this repo's root directory. I recommend invoking pytest via the command `python -m pytest tests`; you can optionally pass any arguments you want to pytest. For more information on writing or running tests, see `tests/README.md`.
