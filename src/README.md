# src
This directory is where all source code should be located, with the exception of testing code; that's in the `tests` directory.

## Important rules for driver scripts
1. All driver scripts MUST be located in `src`, NOT in a subdirectory of `src`.
2. All driver scripts MUST call `main.main()` as one of the first steps in their execution, and definitely before referencing any files. This function changes the directory to the repo's root directory, so all file paths should be written relative to that.
3. Because driver scripts call `main.main()`, they may be invoked from any directory.

## Code guidelines
1. Write import statements relative to the `src` directory. This follows from the requirement that all driver scripts be located in `src`; this means that upon startup, one of the first things that Python will do is add `/absolute/path/to/{Repo Name}/src` to `sys.path`. (The path may not be guaranteed to be absolute, but in my experience it's been absolute.)
2. Write file paths relative to the repo's root directory. This follows from the requirement that all driver scripts call `main.main()`.
3. In order to keep file paths platform-independent, use `os.path` functions like `os.path.join`. For example, rather than writing `"src/main.py"`, write `os.path.join("src", "main.py")`.
4. You may create subdirectories within `src` for code. As long as the driver scripts are located in `src` itself, the rest of the source code may be arbitrarily nested.
