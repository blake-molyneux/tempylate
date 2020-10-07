# Refferences
Many excellent resources have been utilised to the fullest in the construction of this repo. Bellow is a list of the most notable resources used, but by no means is it exhaustive.

## Pythonic Zen
There are a few important principals by which this repo is based:

- Use type hints, for example:
```
def hello_name(name: str) -> str:
    return(f"Hello {name}")
```
- Use docstrings, following the 

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


