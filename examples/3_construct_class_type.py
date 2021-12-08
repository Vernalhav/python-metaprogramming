# Standard Class definition
class BrazilianNumber:
    countryCode = 55

    def __init__(self, area_code, number):
        self.area_code = area_code
        self.number = number
    
    def __str__(self):
        return f'+ {BrazilianNumber.countryCode} ({self.area_code}) {self.number}'



# Defining a Class with the type constructor
def my_init(self, area_code, number):
    self.area_code = area_code
    self.number = number

def print_number(self):
    return f'+ {BrazilianNumber.countryCode} ({self.area_code}) {self.number}'

BrazilianNumber = type('BrazilianNumber', (), {
    'countryCode': 55,
    '__init__': my_init,
    '__str__': print_number
})

number = BrazilianNumber(16, 12341234)
print(f'The number is {number}')
print(f'The type of the instance is {type(number)}')
print(f'The type of the class is {type(BrazilianNumber)}')