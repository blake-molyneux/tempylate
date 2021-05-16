"""
Task Management Tools

This module contains various tools which enable task management, through
the entire task management lifecycle.
"""

import pathlib
import logging

log = logging.getLogger(__name__)
cwd = pathlib.Path(__file__).absolute().parent