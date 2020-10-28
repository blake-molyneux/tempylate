"""
Constructs a new python project.

.. warning:: 
    Work In Progress. This module is in active development.

Based on user input this module constructs a new directory structure
including all files and folders required to start development of a new 
python project. It has been built to overcome the ongoing obsticle of
starting a new python project. It takes too long to setup boilerplate 
files, folders, etc when the majority of the projects undertaken use a
fundamentally homeomorphic, specified structure.

This module is a component of the **tempylate** project.
"""


__author__ = "Blake Molyneux"
__email__ = "blake.molyneux@hotmail.com"
__docformat__ = "restructuredtext"
__license__ = "MIT"
__version__ = "0.0.1.dev0"

import os
import pathlib
import time
import json

from namepkg import Name

def main():
    test_name = Name(name='sailor')
    test_name.check()
    print(test_name.available)

    return None

def rename():
    """
    Rename a package.
    """
    raise NotImplementedError("I've not implemented rename yet.")
    pass

# If called directly, run main()
if __name__ == "__main__":

    main()

    pass