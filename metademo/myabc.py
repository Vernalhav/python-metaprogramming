class AbstractClassInstantiationException(Exception):
    pass


def myabstractmethod(f):
    f.__abstract = True
    return f


class MyABCMeta(type):
    def __is_abstract(abcls, attribute: str) -> bool:
        return hasattr(getattr(abcls, attribute), '__abstract')

    def __has_abstract_methods(abcls) -> bool:
        abcls_attributes = dir(abcls)
        return any(map(abcls.__is_abstract, abcls_attributes))

    def __call__(abcls, *args, **kwargs):
        if abcls.__has_abstract_methods():
            error = f'Cannot instantiate abstract class {abcls.__name__}'
            raise AbstractClassInstantiationException(error) 

        return super(MyABCMeta, abcls).__call__(*args, **kwargs)


class MyABC(metaclass=MyABCMeta):
    pass