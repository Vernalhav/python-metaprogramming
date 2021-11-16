from typing import Dict, List
import sys


class MyDataClassMeta(type):
    def __new__(cls, name, bases, namespace):
        attributes = namespace.get('__annotations__', {})

        init_method = MyDataClassMeta.__get_init_method(attributes)
        exec(init_method, sys.modules[namespace['__module__']].__dict__, namespace)

        return super().__new__(cls, name, bases, namespace)


    @staticmethod
    def __get_function_string(name, args: List[str], body: List[str]) -> str:        
        signature = ', '.join(args)
        body_content = '\n\t'.join(body) or 'pass'
        return f'def {name}({signature}):\n\t{body_content}'


    @staticmethod
    def __get_init_method(attributes: Dict[str, type]) -> str:
        init_params = ['self'] + list(attributes.keys())
        body = [ f'self.{arg} = {arg}' for arg in attributes ]
        return MyDataClassMeta.__get_function_string('__init__', init_params, body)


class MyDataClass(metaclass=MyDataClassMeta):
    pass