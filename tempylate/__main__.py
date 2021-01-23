"""
Manage a python project.

Module level interface to the tempylate package.

This module is a component of the `tempylate` project.
"""

__version__ = '0.0.1.dev0'

import pathlib
import logging
import argparse

log = logging.getLogger(__name__)
cwd = pathlib.Path(__file__).absolute().parent

DEBUG = false # True disables the main() function

# This is the function run when the tempylate module is invoked.
def main() -> None:
    print('Hello world')
    return None

# Run the main function
if not DEBUG:
    main()