"""
Create file and folder structures for a project.

This module forms the backbone of the file and folder management. This
module is not designed to be run directly.

This module is a component of the `tempylate` project.
"""

import pathlib
import logging

import jinja2

log = logging.getLogger(__name__)
cwd = pathlib.Path(__file__).absolute().parent

env = jinja2.Environment(
    loader=jinja2.PackageLoader(__name__, 'templates'),
    autoescape=True,
    )

def load(path: pathlib.Path) -> str:
    """
    Load a template from a file on disk.

    Parameters
    ----------
    path : pathlib.Path
        The path to the template file to be loaded.

    Returns
    -------
    str
        The string output from the rendered template.
    """

    result = ''

    template = env.get_template('module.py')

    result = template.render(
        test='random stuff here'
    )

    return result

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

    raise NotImplementedError('mk_folder() not implemented')

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
        extension if that is desired.

    Returns
    -------
    bool
        True if the file and directories were created successfully.
    """

    raise NotImplementedError('mk_file() not implemented')

    pass
