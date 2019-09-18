# kaggle-template
This is a project template tailored towards data science projects, specifically Kaggle competitions, using the Neptune.ml experiment management system. There are scripts to help set up a working Conda environment and get the Kaggle and Neptune APIs working.

The setup scripts are currently only written to work on Unix-based systems, which means that they should work correctly on Linux and macOS but not Windows. However, apart from those, everything is written to work cross-platform, including on Windows. Most of the setup is pretty straightforward to do on Windows, except perhaps setting the environment variables.

## Using This Template
**WARNING: BEFORE USING THIS TEMPLATE, YOU MUST MAKE SOME CHANGES.** Specifically, you must make the following replacements:
* In `src/constants.py`, replace the placeholders strings with your information. The placeholders are on lines marked with `# TODO Replace this`.
* In `setup1.sh`, replace `{Competition Name}` with the actual name of the competition you want to compete in.
* In `setup2.sh`, replace `{Kaggle Username}` with your Kaggle username.
In order to make these replacements, you must have made a Kaggle account and a Neptune account.

In addition, `environment.yml` will currently create a Conda environment named `myenv`. If you want to change the name, you'll have to do so in `environment.yml` and also in `setup1.sh` and `setup2.sh`.

## Setup
In order to use this repo you will need to first install Anaconda or Miniconda.

There are 2 setup scripts required to fully set up a new environment. First run `setup1.sh`, then **source** `setup2.sh`. That means doing something like the following:
```bash
./setup1.sh
source setup2.sh
```
You should be using Bash as your shell, at least when sourcing `setup2.sh`. It may also work in other shells but I can't guarantee that it will.

`setup2.sh` requires you to have the Kaggle and Neptune API keys handy so you can enter them. Don't worry, they won't be echoed! (See comments in `setup2.sh` for security concerns.) `setup2.sh` also activates the Conda environment so you won't have to do `conda activate myenv` yourself.

To get the Neptune API token, you'll need to create an account at neptune.ml. I recommend creating it using your Github account.

## Run Tests
We're using pytest for our tests. To run tests, invoke pytest while your working directory is this repo's root directory. I recommend invoking pytest via the command `pytest tests`; you can optionally pass any arguments you want to pytest. For more information on writing or running tests, see `tests/README.md`.
