"""
Publish a completed project.

Now that you've completed your project, you will likely need to publish
some material. This module contains tools to help build, compile and
publish your work. Exactly what this does depends on what kind of project
is being run, but some examples are given below.

Python Project: Generate distribution archives, wheels and setup files
for a completed python project. Connect to PyPI and readthedocs to 
publish the build to the work in a single command.

Latex Project: Compile a latex document, inserting data, images, etc and
build the final document, usually to a PDF.

Web App: TBD

This module is a component of the `tempylate` project.
"""

__version__ = '0.0.1.dev0'

import pathlib
import logging

log = logging.getLogger(__name__)
cwd = pathlib.Path(__file__).absolute().parent


