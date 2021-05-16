"""
Constructs a new python project.

Based on user input this module constructs a new directory structure
including all files and folders required to start development of a new 
python project. It has been built to overcome the ongoing obstacle of
starting a new python project. It takes too long to setup boilerplate 
files, folders, etc when the majority of the projects undertaken use a
fundamentally homeomorphous, specified structure.

This module is a component of the `tempylate` project.
"""

__version__ = '0.0.1.dev0'

import pathlib
import logging
import logging.config

import tempylate.utils
import tempylate.nominate

log = logging.getLogger(__name__)
cwd = pathlib.Path(__file__).absolute().parent

# Configure the logging system
tempylate.utils.logging_config()

def rename():
    """
    Rename a package.
    """

    raise NotImplementedError('rename() not implemented yet')
    
    pass
