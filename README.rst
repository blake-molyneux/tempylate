=========
TEMPYLATE
=========
This repo serves a few purposes:

1. Personal learning.
#. Template for future python projects.
#. A reference repo.
#. Showcase my personal process.

Pythonic Zen
------------
There are a few important schemas to be uphold:

- Use type hints::

    def hello_world(name: str) -> str:
        return(f"{name} says 'Hello World'!")

- Follow the Documentation_ guidelines.
- Write `Tests`_ for each and every function.


Documentation
-------------
There are many layers of documentation in this repo. In all cases documentation
must be composed in `reStructuredText`_.
Docs fall into one of 3 tiers:

High
~~~~
High level docs (like this one) are front (consumer/user) facing. They are 
easily accessible by gui, web or other front ends.These must take the file type
``.rst`` and be composed in `reStructuredText`_.

Middle
~~~~~~
Middle level docs sit inside code files, usually at the top of the file, and 
provide the high-level description of the system. These can take the form of 
package or module docstrings. These must take one of the following formats:

Package Docstrings
++++++++++++++++++
Place these docstrings inside the `__init__.py` file at the top of the file. 
They should take the form:

- TODO: Figure out how these comments should be formatted.

Module Docstrings
+++++++++++++++++
Place these docstrings inside the "<package_name>.py" file, at the top of the 
file. They should conform to the `Module`_ format spec.

Low
~~~
Low level docs sit inside the "code" within a module. All documentation in this
section follows the guidelines set by the `Numpy`_ standard. An example module
is provided by Numpy `here`_. A breakdown of the types of docstring included 
in the `Low`_ level are:

- `Classes`_ 
- `Constants`_ 
- `Functions`_ 

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
- Delete files that include "DELETE ME". (e.g. .json" and "sample.csv")
- Work through each file in each directory and change the bylines/docstrings.

Included in this repo are baseline modules that form the backbone of most 
projects. These are likely to be required in your current project and can be
left alone.
NOTOUCH:
- ...

Publication
-----------
The steps to publish this (or any other) repo to `PyPI`_ are covered in the 
`publication tutorial`_.

Version
~~~~~~~
The versioning standard of this project shall conform with `PEP 440`_'s 
"canonical format". More specifically the project shall use a "simple" three
tier ``major.minor.micro`` schema. No preceeding "v". For example::

    0.0.1
    0.0.8
    0.1.1
    2.0.1
    ...


Repo Structure
--------------
- TODO: Update this structure.

Structure::

    helloworld/
    │
    ├── bin/
    │
    ├── docs/
    │   ├── hello.md
    │   └── world.md
    │
    ├── helloworld/
    │   ├── __init__.py
    │   ├── runner.py
    │   ├── hello/
    │   │   ├── __init__.py
    │   │   ├── hello.py
    │   │   └── helpers.py
    │   │
    │   └── world/
    │       ├── __init__.py
    │       ├── helpers.py
    │       └── world.py
    │
    ├── data/
    │   ├── input.csv
    │   └── output.xlsx
    │
    ├── tests/
    │   ├── hello
    │   │   ├── helpers_tests.py
    │   │   └── hello_tests.py
    │   │
    │   └── world/
    │       ├── helpers_tests.py
    │       └── world_tests.py
    │
    ├── .gitignore
    ├── LICENSE
    └── README.md

This is based heavily on the structure outlined in both `RealPython`_'s
and `PyPA`_'s sample projects.

Git Usage
---------
Git commits shall follow this format::

    (Manditory) Summarize changes made in <50 characters

    (Optional) Reasoning:
    - Explain why you made this change
    - Bullet each reason
    - Bullets must be <72 characters

    (Optional) Precisely explain what was done in this commit in more depth \
    than the summery line. Paragraphs need to be wrapped at 72 characters.

    (Optional) Put here additional links and/or co-authors.

Heavily based on the commit format created by `Jacob (dev.to)`_.

References
----------
This resource was created by in order to expedite and unify python project 
production. All references are included throughout this document.



Blake Molyneux, 2020

.. _reStructuredText: https://docutils.sourceforge.io/docs/user/rst/quickref.html
.. _Module: https://numpydoc.readthedocs.io/en/latest/format.html#id15
.. _Numpy: https://numpydoc.readthedocs.io/en/latest/format.html
.. _here: https://numpydoc.readthedocs.io/en/latest/example.html#example
.. _Classes: https://numpydoc.readthedocs.io/en/latest/format.html#id9
.. _Constants: https://numpydoc.readthedocs.io/en/latest/format.html#id14
.. _Functions: 
.. _PEP 440: https://www.python.org/dev/peps/pep-0440/
.. _PyPI: https://pypi.org/
.. _publication tutorial: https://packaging.python.org/tutorials/packaging-projects/
.. _RealPython: https://realpython.com/python-application-layouts/#application-with-internal-packages
.. _PyPA: https://github.com/pypa/sampleproject
.. _Jacob (dev.to): https://dev.to/jacobherrington/how-to-write-useful-commit-messages-my-commit-message-template-20n9
