#!/bin/bash
set -e  # This is a Bash builtin command that exits the script if a command errors

# Next we'll cd into the directory containing this script. This is useful because it means
# we can use relative paths to things like 'environment.yml' but this script may be called from
# anywhere. Of course, this also requires that the script is not moved, but I think that's
# fair to require.
# This snippet is from a stackoverflow answer: https://stackoverflow.com/a/246128
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"  # The -P option to cd makes it not follow symlinks.
# The above snippet assigned the absolute path to the parent directory of this file to DIR. Now we can actually cd.
cd "$DIR"

echo "[setup.sh] Now setting up conda environment."
conda env create -f environment.yml

echo "[setup.sh] Now downloading dataset from Kaggle to directory 'data'."
# We need to make sure we're using the conda environmnt in order for 'kaggle' commands to work
conda activate myenv || source activate myenv
echo "[setup.sh] There may have been an error message just now, but it appears that we have been able to recover from it. Proceeding to download data."
kaggle competitions download {Competition Name} -p data  # TODO Replace placeholder
