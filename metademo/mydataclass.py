
class MyDataClassMeta(type):
    def __new__(cls, name, bases, namespace):

        attributes = namespace.get('__annotations__', {})

        indent = '\n\t'
        init_signature = f"self{''.join(f', {attr}: {attr_type.__name__}' for attr, attr_type in attributes.items())}"
        init_body = f"{indent}{indent.join(f'self.{attr} = {attr}' for attr in attributes) or 'pass'}"

        init_method = f'''
def __init__({init_signature}):
{init_body}
'''

        exec(init_method, globals(), namespace)

        return super().__new__(cls, name, bases, namespace)


class MyDataClass(metaclass=MyDataClassMeta):
    pass


class A(MyDataClass):
    size: int
    color: str

    def test(x: int) -> str:
        pass