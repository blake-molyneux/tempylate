"""
Publish a completed python project.

Generate distribution archives, wheels and setup files for a completed
python project. Connect to PyPI, readthedocs etc to publish the build.

This module is a component of the `tempylate` project.
"""

__version__ = "0.0.1.dev0"

import pathlib
import logging

log = logging.getLogger(__name__)
cwd = pathlib.Path(__file__).absolute().parent
