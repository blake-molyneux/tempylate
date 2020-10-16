"""Run this setup file to build the project.

.. warning::
    Work In Progress.

Examples
--------
To build the file:
    $ 

"""

import setuptools

with open("README.rst", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="tempylate",
    version="0.0.1.dev0",
    author="Blake Molyneux",
    author_email="blake.molyneux@hotmail.com",
    description="A package to expedite the package authorship process.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/blake-molyneux/tempylate",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)