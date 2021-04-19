"""
Task Management Tools

This module contains various tools which enable task management, through
the entire task management lifecycle.
"""

__version__ = '0.0.1.dev0'

import pathlib
import logging

log = logging.getLogger(__name__)
cwd = pathlib.Path(__file__).absolute().parent