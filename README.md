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

`setup2.sh` requires you to have the Neptune API key handy so you can enter it. Don't worry, it won't be echoed! (See comments in `setup2.sh` for security concerns.) `setup2.sh` also activates the Conda environment so you won't have to do `conda activate fashionmnist` yourself.

To get the Neptune API token, you'll need to create an account at neptune.ml. I recommend creating it using your Github account.

## Run Tests
We're using pytest for our tests. To run tests, invoke pytest while your working directory is this repo's root directory. I recommend invoking pytest via the command `pytest tests`; you can optionally pass any arguments you want to pytest. For more information on writing or running tests, see `tests/README.md`.
