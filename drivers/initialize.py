import sys
import os

def initialize():
    """
    This function does 2 things.
    
    First, it changes the Python process's working directory to the
    project's root directory. This is required to ensure that we can
    use relative path names in the rest of the code to access files in
    the repo.
    Second, it inserts the path to the project's root directory at the
    beginning of sys.path. This is required to ensure that absolute import
    statements (i.e. plain old import statements) may be written in the
    same way in all the code (that is, relative to the project root) without
    anything breaking.

    In any driver script, you should ALWAYS call this function before doing
    anything else. If there are any failures, this function will call sys.exit() to 
    terminate the process with an exception.

    In order for this function to work correctly, Python MUST be invoked using
    a driver script in the 'drivers' directory, NOT in a subdirectory of 'drivers'.

    Note: when a driver script imports this file, it will have to do so with
    an import that's relative to 'drivers' rather than the project root. This is
    unfortunate but unavoidable; the path to 'drivers' is the only one that starts
    off in sys.path, which is the reason that the driver needs to call initialize()
    in the first place! So there's a bit of a chicken-and-egg problem. The
    upshot is that there's a bit of ugliness in the code, in the sense that
    'import initialize' is relative to 'drivers' but every other import in the project
    is relative to the project root dir. Still, I think this is the minimally
    ugly way to do it.
    """
    arg0 = sys.argv[0]
    if not os.path.isfile(arg0):
        sys.exit("sys.argv[0] is not a path to a file: \"" + str(arg0) + "\". Exiting now.")
    absolute_path_to_file = os.path.realpath(arg0) # realpath follows symlinks, which is what we want in this case.
    absolute_path_to_drivers = os.path.dirname(absolute_path_to_file)
    (absolute_path_to_repo, drivers_dirname) = os.path.split(absolute_path_to_drivers)
    if drivers_dirname != "drivers":
        sys.exit("The driver script should be located in directory \"drivers\". It is instead in \"" + drivers_dirname + "\". Exiting now.")
    os.chdir(absolute_path_to_repo)
    sys.path.insert(0, absolute_path_to_repo)
