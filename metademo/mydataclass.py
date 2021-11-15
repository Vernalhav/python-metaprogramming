
class MyDataClassMeta(type):
    pass


class MyDataClass(metaclass=MyDataClassMeta):
    pass