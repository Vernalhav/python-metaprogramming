import pprint
from typing import Dict, List, Tuple, get_type_hints
import inspect
import sys

class MyDataClassMeta(type):
    def __new__(cls, name, bases, namespace):
        attributes = namespace.get('__annotations__', {})
        init_method = MyDataClassMeta.__get_init_method(attributes, namespace.get('__module__'))
        print(f'\n========================\n{init_method}\n===================\n\n\n')
        exec(init_method, sys.modules[namespace.get('__module__')].__dict__, namespace)

        return super().__new__(cls, name, bases, namespace)

    @staticmethod
    def __annotate_in_module(base_module: str):
        def __annotate_parameter(param: Tuple[str, type]) -> List[str]:
            param_name, param_type = param
            return f'{param_name}' + (f': {inspect.formatannotation(param_type, base_module)}' if param_type is not None else '')
        return __annotate_parameter

    @staticmethod
    def __get_function_string(name, args: Dict[str, type], body: List[str], base_module: str=None) -> str:
        annotator_function = MyDataClassMeta.__annotate_in_module(base_module)
        annotated_params = map(annotator_function, args.items())
        signature = ', '.join(annotated_params)

        body_content = '\n\t'.join(body) or 'pass'
        return f'def {name}({signature}):\n\t{body_content}'

    def __get_init_method(attributes: Dict[str, type], base_module: str=None) -> str:
        body = [ f'self.{arg} = {arg}' for arg in attributes ]
        init_params = { 'self': None, **attributes }
        return MyDataClassMeta.__get_function_string('__init__', init_params, body, base_module)


class MyDataClass(metaclass=MyDataClassMeta):
    pass