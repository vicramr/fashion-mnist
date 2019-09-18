import sys
import os

def main():
    """
    This function changes the Python process's working directory to the
    project's root directory. This is required to ensure that we can
    use relative path names in the rest of the code to access files in
    the repo.

    In any driver script, you should ALWAYS call this function before doing
    anything else. If there are any failures, this function will call sys.exit() to 
    terminate the process with an exception.

    In order for this function to work correctly, Python MUST be invoked using
    a driver script in the 'src' directory, NOT in a subdirectory of 'src'.
    """
    arg0 = sys.argv[0]
    if not os.path.isfile(arg0):
        sys.exit("sys.argv[0] is not a path to a file: \"" + str(arg0) + "\". Exiting now.")
    absolute_path_to_file = os.path.realpath(arg0) # realpath follows symlinks, which is what we want in this case.
    absolute_path_to_src = os.path.dirname(absolute_path_to_file)
    (absolute_path_to_repo, src_dirname) = os.path.split(absolute_path_to_src)
    if src_dirname != "src":
        sys.exit("The driver script should be located in directory \"src\". It is instead in \"" + src_dirname + "\". Exiting now.")
    os.chdir(absolute_path_to_repo)
