import pytest
from metademo.myabc import MyABC, myabstractmethod, AbstractClassInstantiationException

class Interface(MyABC):
    @myabstractmethod
    def f(self):
        pass

    def identity(self, x):
        return x

class ConcreteClassA(Interface):
    def f(self):
        return 42

class ConcreteClassB(Interface):
    def f(self):
        return 69

class InterfaceSubclass(Interface):
    pass

class ConcreteClassC(InterfaceSubclass):
    def f(self):
        return 37

class TestMyABC():
    @staticmethod
    def test_abstract_method_call():
        a = ConcreteClassA()
        b = ConcreteClassB()
        c = ConcreteClassC()

        assert a.f() == 42
        assert b.f() == 69
        assert c.f() == 37

    @staticmethod
    def test_abstract_instantiation_prevention():
        with pytest.raises(AbstractClassInstantiationException):
            i = Interface()
    
    @staticmethod
    def test_not_implemented_instantiation_prevention():
        with pytest.raises(AbstractClassInstantiationException):
            i = InterfaceSubclass()

    @staticmethod
    def test_nonabstract_base_method():
        a = ConcreteClassA()
        b = ConcreteClassB()

        assert a.identity(420) == 420
        assert b.identity(420) == 420