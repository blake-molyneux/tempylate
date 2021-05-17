"""
Manage a python project.

Module level interface to the tempylate package.

This module is a component of the `tempylate` project.
"""

import pathlib
import logging
import argparse

log = logging.getLogger(__name__)
cwd = pathlib.Path(__file__).absolute().parent

# Package level switches
DEBUG = False # True disables the main() function

# This is the function run when the tempylate module is invoked.
def main() -> None:
    print(__name__)
    return None

# Run the main function
if __name__ == '__main__':
    log.debug(f"Running the package with debug mode: {DEBUG}")
    log.warning("AAAAAAAaaaaAAAAA")
    if not DEBUG:
        main()
    pass