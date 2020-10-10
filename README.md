# py_template
This repo serves a few purposes:
1. Personal learning.
1. Template for future python projects.


## Post Clone
When this repo is coloned into a new project, the things that need to be changed are:

- Change "py_template" to the name of the new project.
- Delete files that include "DELETE ME" such as the "config.json" and "sample.csv" files.
- Work through each file in each directory and change the bylines/docstrings.

Included in this repo are baseline modules that form the backbone of most projects, and these don't need to be touched.
NOTOUCH:
- ...


## Pythonic Zen
There are a few important schemas to be uphold:

- Use type hints, for example:
```
def hello_world(name: str) -> str:
    return(f"{name} says 'Hello World'!")
```
- Use docstrings in the repo format [1](####package-docstrings):

## Documentation
There are many layers of documentation in this repo.
Docs fall into one of 3 tiers:

### High
High level docs (like this one) are front (consumer/user) facing. They are easily accessible by gui, web or other front ends.
These must take one of the following formats:
1. .md [(MarkDown)](https://guides.github.com/features/mastering-markdown/)
1. .pdf

### Middle
Middle level docs sit inside code files, usually at the top of the file, and provide the high-level description of the system.
These can take the form of package or module docstrings.
These must take one of the following formats:

#### Package Docstrings
Place these docstrings inside the `__init__.py` file at the top of the file. They should take the form:

TODO

#### Module Docstrings
Place these docstrings inside the "<package_name>.py" file, at the top of the file. They should take the [formal format spec](https://numpydoc.readthedocs.io/en/latest/format.html#id15).

### Low
Low level docs sit inside the "code" within a module. These are docstrings for:
- [Classes](https://numpydoc.readthedocs.io/en/latest/format.html#id9)
- [Constants](https://numpydoc.readthedocs.io/en/latest/format.html#id14)
- [Functions]()
All of these docs must follow the appropriate [formal format spec](https://numpydoc.readthedocs.io/en/latest/format.html) 

## Repo Structure
This template repo is based on the structure suggested by the [RealPython](https://realpython.com/python-application-layouts/#application-with-internal-packages) and [PyPA](https://github.com/pypa/sampleproject).

RealPython suggested structure:

```
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
```

## Git Usage

Git commits follow this format, courtesy of [Jacob, dev.to](https://dev.to/jacobherrington/how-to-write-useful-commit-messages-my-commit-message-template-20n9):



>Summarize the change in less than 50 characters
>
>Because:
>- Explain the reasons you made this change
>- Make a new bullet for each reason
>- Each line should be under 72 characters
>
>Explain exactly what was done in this commit with more depth than the
>50 character subject line. Remember to wrap at 72 characters!
>
>Include any additional notes, relevant links, or co-authors.

## References
This resource was created by in order to expidite and unify python project production.

Additionally please read the [references](docs/references.md) document for more information.


Blake Molyneux, 2020