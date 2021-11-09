class AbstractClassInstantiationException(Exception):
    pass


def myabstractmethod(f):
    f.__abstract = True
    return f


class MyABCMeta(type):
    @staticmethod
    def get_abstract_methods(namespace):
        abstract_methods = []

        for elem in namespace.values():
            if getattr(elem, '__abstract', False) is True:
                abstract_methods.append(elem)

        return abstract_methods


    def __call__(abcls, *args, **kwargs):
        if len(MyABCMeta.get_abstract_methods(abcls.__dict__)) > 0:
            raise AbstractClassInstantiationException(f'Cannot instantiate abstract class {abcls.__name__}') 

        return super().__call__(*args, **kwargs)


class MyABC(metaclass=MyABCMeta):
    pass