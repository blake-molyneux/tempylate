=======================
Developer Documentation
=======================
There be dragons here.

Pythonic Zen
------------
There are a few important schemas to be uphold:

1. `PEP8`_ will be your savior.
#. Use type hints::

    def hello_world(name: str) -> str:
        return(f"{name} says 'Hello World'!")

#. Follow the Documentation_ guidelines.
#. Write Tests_ for each and every function.
#. All files shall be written in UTF8 encoding.
#. Use double quotes for long language/sentences otherwise single quotes
   is preferred.

Design Decisions
----------------
1. Inclusion of ``tests``.

   1. The decision was made to include the tests in this package. The
      tempylate package isn't going to top the charts of PyPI Stats so
      including a few extra KBs of tests seems to have little down side.
   #. I am willing to reconsider this decision.

#. This is an automated one.

Tests
-----
Write tests for every function. No matter how unimportant it may seem.
Use the inbuilt unittest package for this.

Publication
-----------
There are several steps to the publication process. These are:

1. Formalise all documentation.
#. Configure setup.py file.
#. Build project into distro.
#. Upload build to the Test PyPI platform. Confirm functionality.
#. Upload revised build to PyPI.
#. Upload docs to Read The Docs.

For detailed instructions on how to complete these steps please see the
`detailed publication`_ page of python packaging.

PyPI Pub
~~~~~~~~
The steps to publish this (or any other) repo to `PyPI`_ are covered in
the `publication tutorial`_.

Read The Docs
~~~~~~~~~~~~~
To publish documentation to Read The Docs follow the guide to 
`documentation publication`_

Version
~~~~~~~
The versioning standard of this project shall conform with `PEP 440`_'s 
"canonical format". More specifically the project shall use a "simple"
three tier "``major.minor.micro``" (``X.Y.Z``) schema. No prefix "v". 
Dev versions are to use the ``.devN`` suffix. For example::

    0.0.1
    0.1.1
    2.0.1
    ...
    2.1.0.dev1

Post Clone
----------
When this repo is cloned into a new project, the things that need to be 
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

Documentation
-------------
There are many layers of documentation in this repo. In all cases 
documentation must be composed in `reStructuredText`_. The main
inspiration for the structure of the documentation is the `Numpy`_
formal documentation specification.
Docs fall into one of 3 tiers:

High
~~~~
High level docs (like this one) are front (consumer/user) facing. They
are easily accessible by gui, web or other front ends.These must take 
the file type ``.rst`` and be composed in `reStructuredText`_.

Middle
~~~~~~
Middle level docs sit inside code files, usually at the top of the file,
and provide the high-level description of the system. These can take the
form of package or module docstrings. These must take one of the 
following formats:

Package Docstrings
++++++++++++++++++
Place these docstrings inside the `__init__.py` file at the top of the
file. They should take the form:

- TODO: Figure out how these comments should be formatted.

Module Docstrings
+++++++++++++++++
Place these docstrings inside the "<package_name>.py" file, at the top
of the file. They should conform to the `Module`_ format spec.

Low
~~~
Low level docs sit inside the "code" within a module. All documentation
in this section follows the guidelines set by the `Numpy`_ standard. An
example module is provided by `Numpy`_. A breakdown of the types of
docstring included in the Low_ level are:

- `Classes`_ 
- `Constants`_ 
- `Functions`_

Samples/Boilerplate
-------------------

Package Docstring
~~~~~~~~~~~~~~~~~

Module Docstring
~~~~~~~~~~~~~~~~
Boilerplate module (Middle) level docstring. Fill in the ``[ ]`` 
sections.

    """[module name] does [summery]. This line must be <72 chars.

    (optional) .. warning: Deprecated / Work In Progress

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

    (Mandatory) Summarize changes made in <50 characters

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

- ``pip freeze | xargs pip uninstall -y`` => Uninstall all modules from
  the current python environment.

References
----------
This resource was created by in order to expedite and unify python
project production. All references are included at the end of this 
document.


Blake Molyneux, 2020

.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _PEP 440: https://www.python.org/dev/peps/pep-0440/

.. _reStructuredText: https://docutils.sourceforge.io/docs/user/rst/quickref.html
.. _PyPI: https://pypi.org/
.. _detailed publication: https://packaging.python.org/guides/distributing-packages-using-setuptools/
.. _publication tutorial: https://packaging.python.org/tutorials/packaging-projects/
.. _documentation publication: https://packaging.python.org/tutorials/creating-documentation/

.. _Numpy: https://numpydoc.readthedocs.io/en/latest/format.html
.. _Module: https://numpydoc.readthedocs.io/en/latest/format.html#documenting-modules
.. _Classes: https://numpydoc.readthedocs.io/en/latest/format.html#documenting-classes
.. _Constants: https://numpydoc.readthedocs.io/en/latest/format.html#documenting-constants
.. _Functions: https://numpydoc.readthedocs.io/en/latest/format.html#sections

.. _RealPython: https://realpython.com/python-application-layouts/#application-with-internal-packages
.. _PyPA: https://github.com/pypa/sampleproject
.. _Jacob (dev.to): https://dev.to/jacobherrington/how-to-write-useful-commit-messages-my-commit-message-template-20n9

