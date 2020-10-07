# Refferences

This template repo is based on the structure suggested by the [RealPython](https://realpython.com/python-application-layouts/#application-with-internal-packages) and [PyPA](https://github.com/pypa/sampleproject).

RealPython suggested structure:

`
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
`
