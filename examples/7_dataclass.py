from typing import List
from metademo.mydataclass import MyDataClass

class Person(MyDataClass):
    name: str
    age: int
    favorite_games: List[str]

    def greet(self):
        print(f'Hello, {self.name}! Your favorite games are {", ".join(self.favorite_games)}')


victor = Person('Victor', 21, ['Outer Wilds', 'Hollow Knight', 'Dark Souls'])
victor.greet()

jao = Person('Jão', 21, ['Dofus', 'Hades', 'Legends of Runeterra'])
jao.greet()