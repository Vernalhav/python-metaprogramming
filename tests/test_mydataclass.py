from metademo.mydataclass import MyDataClass
import pytest


class TestMyDataClass():
    
    class Person(MyDataClass):
        name: str
        age: int

    class Empty(MyDataClass):
        pass

    @staticmethod
    def test_bad_instantiation():
        with pytest.raises(TypeError):
            p = TestMyDataClass.Person()

    @staticmethod
    def test_empty_insantiation():
        e = TestMyDataClass.Empty()

    @staticmethod
    def test_attributes():        
        p = TestMyDataClass.Person('William', 22)
        assert p.name == 'William'
        assert p.age == 22
    
    @staticmethod
    def test_multiple_instances():
        plato = TestMyDataClass.Person('Plato', 2442)
        aristotle = TestMyDataClass.Person('Aristotle', 2405)

        assert plato.name == 'Plato' and plato.age == 2442
        assert aristotle.name == 'Aristotle' and aristotle.age == 2405