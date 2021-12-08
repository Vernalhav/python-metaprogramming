class BrazilianNumber:
    countryCode = 55

    def __init__(self, area_code, number):
        self.area_code = area_code
        self.number = number
    
    def __str__(self):
        return f'+ {BrazilianNumber.countryCode} ({self.area_code}) {self.number}'


number = BrazilianNumber(11, 55551234)
print(f'The number is {number}')
print(f'The type of the instance is {type(number)}')
print(f'The type of the class is {type(BrazilianNumber)}')
print(f'The type of string is {type(str)}')