"""
Create file and folder structures for a project.

.. warning:: 
    Work In Progress. This function is in active development.

This module forms the backbone of the file and folder management. This
module is not designed to be run directly.

This module is a component of the **tempylate** project.
"""

__author__ = "Blake Molyneux"
__email__ = "blake.molyneux@hotmail.com"
__docformat__ = "restructuredtext"
__license__ = "MIT"
__version__ = "0.0.1.dev0"

import os
import jinja2
import pathlib

def main():
    jenv = jinja2.Environment(
        loader=jinja2.PackageLoader('fylr', 'templates'),
        autoescape=True)
    
    template = jenv.get_template('module.py')
    print(template.render(
        module_comment='Hello World!'))
    pass

def mk_folder(path : pathlib.Path() = pathlib.Path('')):
    """
    Create a directory.
    
    Given a supplied directory attempt to create it. If the directory
    already exists, then handle the error.

    Parameters
    ----------
    path : pathlib.Path
        The full directory path to be created.

    Returns
    -------
    bool
        True if the directory was created successfully.
    """

    pass

def mk_file(path : pathlib.Path() = pathlib.Path('')):
    """
    Create a file.

    Given a supplied file directory and name, create the directory
    structure if it doesn't already exist. Then create the empty file
    with the given file name.

    Parameters
    ----------
    path : pathlib.Path
        Path to the directory in which to create the file.
    name : str
        Name of the file to be created. Include in this name a file
        extenstion if that is desired.

    Returns
    -------
    bool
        True if the file and directories were created successfully.
    """

    pass

if __name__ == "__main__":
    main()
