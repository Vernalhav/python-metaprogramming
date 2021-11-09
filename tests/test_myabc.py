import pytest
from myabc import MyABC, myabstractmethod, AbstractClassInstantiationException


class TestMyABC():

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

    @staticmethod
    def test_abstract_method_call():
        a = TestMyABC.ConcreteClassA()
        b = TestMyABC.ConcreteClassB()

        assert a.f() == 42
        assert b.f() == 69

    @staticmethod
    def test_abstract_instantiation_prevention():
        with pytest.raises(AbstractClassInstantiationException):
            i = TestMyABC.Interface()
    
    @staticmethod
    def test_not_implemented_instantiation_prevention():
        with pytest.raises(AbstractClassInstantiationException):
            i = TestMyABC.InterfaceSubclass()

    @staticmethod
    def test_nonabstract_base_method():
        a = TestMyABC.ConcreteClassA()
        b = TestMyABC.ConcreteClassB()

        assert a.identity(420) == 420
        assert b.identity(420) == 420