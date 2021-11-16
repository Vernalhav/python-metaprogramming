# Python Metaprogramming
This repo contains two examples of metaclass usecases in Python: abstract base classes and dataclasses. I tried to replicate as closely as possible the features of the `ABC` and `dataclasses` standard Python modules while still remaining as simple as possible for educational purposes.

# Installation
The base package has no dependencies and can be installed by running
```bash
pip install .
```
in the directory containing `setup.py`. It can then be imported with the `metademo` module.

# Automated testing
If you wish to run the automated tests, then the `pytest` module is required. The tests can be executed by running
```bash
pytest
```
in the root or `/tests` directory.

# Project structure
```bash
├── metademo
│   ├── __init__.py
│   ├── myabc.py          # Abstract base class implementation
│   └── mydataclass.py    # Dataclass implementation
├── setup.py
└── tests                 # Automated tests
    ├── test_myabc.py
    └── test_mydataclass.py
```

# Usage example
## Abstract Base Class
```python
from metademo.myabc import MyABC, myabstractmethod
from typing import List, Dict

class DataReader(MyABC):
  @myabstractmethod
  def read_input(data_path: str) -> List[Dict]:
    pass
    
class CSVReader(DataReader):
  def read_input(data_path: str) -> List[Dict]:
    print(f'Reading csv file {data_path}...')

class DatabaseReader(DataReader):
  def read_input(data_path: str) -> List[Dict]:
    print(f'Reading data from table {data_path}...')

csv_reader = CSVReader()
db_reader = DatabaseReader()
abstract_reader = DataReader()    # Throws exception because there are unimplemented abstract methods
```
## Dataclasses
```python
from metademo.mydataclass import MyDataClass

class Person(MyDataClass):
    name: str
    age: int

    def greet(self):
        return f'Hello, {self.name}!'

victor = Person('Victor', 21)   # Automatically generated init method
victor.greet()                  # Hello, Victor!
```

# TODO
## General
- Add CI automated testing and linting with Github Actions
- Rename `metademo/` directoru to `src/`

## Abstract Base Class
- Throw error if abstract and concrete type annotation signature do not match

## Dataclass
- Add `repr` method
- Add type hints to `__init__` params (check branch `feat/type-annotations` for current attempts at this featrue)
- Add default values to `__init__` parameters
