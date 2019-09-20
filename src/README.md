# src
This directory is where files containing the business logic should be located. Driver scripts should be in `drivers` and tests should be in `tests`, but driver scripts should mostly just be calling functions which are located in `src`.

## Code guidelines
1. Write import statements relative to the project root directory. This follows from the requirement that all driver scripts call `initialize.initialize()`.
2. Write file paths relative to the repo's root directory. This follows from the requirement that all driver scripts call `initialize.initialize()`.
3. In order to keep file paths platform-independent, use `os.path` functions like `os.path.join`. For example, rather than writing `"drivers/initialize.py"`, write `os.path.join("drivers", "initialize.py")`.
4. You may create subdirectories within `src` for code. Files in `src` may be arbitrarily nested.
