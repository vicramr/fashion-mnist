# drivers
This directory holds driver scripts.

## Important rules for driver scripts
1. All driver scripts MUST be located in `drivers`, NOT in a subdirectory of `drivers`.
2. All driver scripts MUST call `initialize.initialize()` before doing anything else. This function changes the directory to the repo's root directory, so all file paths should be written relative to that.
3. Because driver scripts call `initialize.initialize()`, they may be invoked from any directory.
