=========
TEMPYLATE
=========
This repo serves a few purposes:

1. Personal learning.
#. Template for future python projects.
#. A reference repo.
#. Showcase my personal process.

Included Functions
------------------
- TODO: Build and list the included (functional) modules.

Tests
-----
- TODO: Learn how tests work.

Post Clone
----------
When this repo is coloned into a new project, the things that need to be 
changed are:

- Create a virtual python environment within the "template" dir with the 
  command "``python3 -m venv venv``".
- Change "py_template" to the name of the new project.
- Delete files that include in their name "sample" as these are filler
  and don't provide any functionality.
- Work through each file in each directory and change the bylines or 
  docstrings.

Included in this repo are baseline modules that form the backbone of
most projects. These are likely to be required in your current project
and can be left alone.
NOTOUCH:

- TODO: Add files that can be left alone.

Repo Structure
--------------
- TODO: Update this structure.

Structure::

    tempylate/
    │
    ├── bin/
    │
    ├── docs/
    │   └── authorship.rst
    │
    ├── tempylate/
    │   ├── __init__.py
    │   ├── __main__.py
    │   ├── tempylate.py
    │   └── namepkg/
    │   │   ├── __init__.py
    │   │   └── namepkg.py
    │
    ├── data/
    │   ├── sample.csv
    │   └── sample.json
    │
    ├── tests/
    |
    ├── .gitignore
    ├── LICENSE
    └── README.md

This structure was inspired by the structure outlined in both 
`RealPython`_'s and `PyPA`_'s sample projects. Additionally many open
source projects were reviewed to get a sense of what formats are widely
used.

Samples/Boilerplate
-------------------

Package Docstring
~~~~~~~~~~~~~~~~~

Module Docstring
~~~~~~~~~~~~~~~~
Boilerplate module (Middle) level docstring. Fill in the ``[ ]`` 
sections.

    """[module name] does [summery]. This line must be <72 chars.

    (optional) .. warning: Depicated / Work In Progress

    [extended summery] This module has been built to solve [problem].
    It approaches this by [description]
    
    """#&

Additionally it is also expected that the following annotation dunders 
be included in each and every module:

- ``__author__ = "[name]"`` 
- ``__version__ = "X.Y.Z(.devN)"``

Git Usage
~~~~~~~~~
Git commits shall follow this format::

    (Manditory) Summarize changes made in <50 characters

    (Optional) Reasoning:
    - Explain why you made this change
    - Bullet each reason
    - Bullets must be <72 characters

    (Optional) Precisely explain what was done in this commit in more \
    depth than the summery line. Paragraphs need to be wrapped at 72  \
    characters.

    (Optional) Put here additional links and/or co-authors.

Heavily based on the commit format specified by `Jacob (dev.to)`_.

Appendix
--------
Useful code incantations:

- ``pip freeze | xargs pip uninstall -y`` 
  - Uninstall all modules from python environment.
- Hello again


References
----------
This resource was created by in order to expedite and unify python
project production. All references are included at the end of this 
document.


Blake Molyneux, 2020

.. _documentation publication: https://packaging.python.org/tutorials/creating-documentation/
.. _reStructuredText: https://docutils.sourceforge.io/docs/user/rst/quickref.html
.. _Module: https://numpydoc.readthedocs.io/en/latest/format.html#documenting-modules
.. _Numpy: https://numpydoc.readthedocs.io/en/latest/format.html
.. _here: https://numpydoc.readthedocs.io/en/latest/example.html#example
.. _Classes: https://numpydoc.readthedocs.io/en/latest/format.html#documenting-classes
.. _Constants: https://numpydoc.readthedocs.io/en/latest/format.html#documenting-constants
.. _Functions: https://numpydoc.readthedocs.io/en/latest/format.html#sections
.. _PEP 440: https://www.python.org/dev/peps/pep-0440/
.. _PyPI: https://pypi.org/
.. _detailed publication: https://packaging.python.org/guides/distributing-packages-using-setuptools/
.. _publication tutorial: https://packaging.python.org/tutorials/packaging-projects/
.. _RealPython: https://realpython.com/python-application-layouts/#application-with-internal-packages
.. _PyPA: https://github.com/pypa/sampleproject
.. _Jacob (dev.to): https://dev.to/jacobherrington/how-to-write-useful-commit-messages-my-commit-message-template-20n9
.. _PEP8: https://www.python.org/dev/peps/pep-0008/
