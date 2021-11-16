from typing import List

import pytest
from metademo.mydataclass import MyDataClass


class Person(MyDataClass):
    name: str
    age: int

    def greet(self):
        return f'Hello, {self.name}!'


class Empty(MyDataClass):
    pass


class NotPrimitiveType(MyDataClass):
    people: List[Person]
    empty: Empty


class TestMyDataClass():
    @staticmethod
    def test_bad_instantiation():
        with pytest.raises(TypeError):
            p = Person()

    @staticmethod
    def test_empty_insantiation():
        e = Empty()

    @staticmethod
    def test_attributes():        
        p = Person('William', 22)
        assert p.name == 'William'
        assert p.age == 22
    
    @staticmethod
    def test_method():
        p = Person('William', 22)
        assert p.greet() == 'Hello, William!'

    @staticmethod
    def test_multiple_instances():
        plato = Person('Plato', 2442)
        aristotle = Person('Aristotle', 2405)
        assert plato.name == 'Plato' and plato.age == 2442
        assert aristotle.name == 'Aristotle' and aristotle.age == 2405

    @staticmethod
    def test_not_primitive_type():
        not_primitive = NotPrimitiveType([Person('Tijolo', 21), Person('Baracus', 23), Person('Jão', 21)], Empty())
        assert not_primitive.people[2].name == 'Jão'