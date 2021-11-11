
class AbstractClassInstantiationException(Exception):
    pass


def myabstractmethod(f):
    f.__abstract = True
    return f


class MyABCMeta(type):
    def __is_abstract(abcls, attribute: str):
        return hasattr(getattr(abcls, attribute), '__abstract')

    def __has_abstract_methods(abcls):
        abcls_attributes = dir(abcls)
        return any(map(abcls.__is_abstract, abcls_attributes))

    def __call__(abcls, *args, **kwargs):
        if MyABCMeta.__has_abstract_methods(abcls):
            raise AbstractClassInstantiationException(f'Cannot instantiate abstract class {abcls.__name__}') 

        return super().__call__(*args, **kwargs)


class MyABC(metaclass=MyABCMeta):
    pass