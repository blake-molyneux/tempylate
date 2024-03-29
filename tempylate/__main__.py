"""
Manage a python project.

Module level interface to the tempylate package.

This module is a component of the `tempylate` project.
"""

import pathlib
import logging
import argparse

from . import nominate

log = logging.getLogger(__name__)
cwd = pathlib.Path(__file__).absolute().parent

# Package level switches
DEBUG = False # True disables the main() function

# This is the function run when the tempylate module is invoked.
def main() -> None:
    # Does the user want to find pypi package names or just module names?
    mode = (input("Do you wish to check pypi package names? (Y/n)\n").lower() == 'y')
    while True:
        print("=======================\nWhat's the theme?")
        theme = input()
        if mode:
            number = int(input("How many names should be generated?\n"))
        else:
            number = 0
        name = nominate.Name(theme=theme, number=number, check_pypi=mode)
        name.gen_new_name()
        print("The results are: " + ", ".join(name.output))
        print("=======================\n")
    return None

# Run the main function
if __name__ == '__main__':
    log.debug(f"Running the package with debug mode: {DEBUG}")
    if not DEBUG:
        main()
    pass