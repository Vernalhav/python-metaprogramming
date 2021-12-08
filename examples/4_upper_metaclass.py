from pprint import pprint

# Metaclass that will make all class attributes and methods be uppercase
class ToUpper(type):
    def __new__(cls, name, bases, namespace):
        new_namespace = {}
        for attr, value in namespace.items():
            if attr.startswith('__'):
                new_namespace[attr] = value
            else:
                new_namespace[attr.upper()] = value

        return super().__new__(cls, name, bases, new_namespace)


class BrazilianNumber(metaclass=ToUpper):
    countryCode = 55
    areaCodes = {
        'São Paulo': 11,
        'Rio de Janeiro': 21,
        'São Carlos': 16,
    }

    def __init__(self, area_code, number):
        self.area_code = area_code
        self.number = number
    
    def __str__(self):
        return f'+ {BrazilianNumber.COUNTRYCODE} ({self.area_code}) {self.number}'

    def is_number_from_area(self, area):
        return BrazilianNumber.AREACODES[area] == self.area_code

number = BrazilianNumber(16, 12341234)
print(f'number\'s dict representation is\n{number.__dict__}', end='\n\n')
print(f'BrazilianNumber\'s dict representation is')
pprint(BrazilianNumber.__dict__)