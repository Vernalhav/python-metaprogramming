from metademo.myabc import AbstractClassInstantiationException, MyABC, myabstractmethod
from typing import List, Dict

class DataReader(MyABC):
  @myabstractmethod
  def read_input(self, data_path: str) -> List[Dict]:
    pass
    
class CSVReader(DataReader):
  def read_input(self, data_path: str) -> List[Dict]:
    print(f'Reading csv file {data_path}...')

class DatabaseReader(DataReader):
  def read_input(self, data_path: str) -> List[Dict]:
    print(f'Reading data from table {data_path}...')

csv_reader = CSVReader()
csv_reader.read_input('data.csv')

db_reader = DatabaseReader()
db_reader.read_input('Users')

try:
    abstract_reader = DataReader()
except AbstractClassInstantiationException as error:
    print(error)