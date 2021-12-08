from math import sqrt

class Point:
    ''' Class representing a 2D point '''
    origin = (0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_distance_from_origin(self):
        return sqrt((self.x - Point.origin[0])**2 + (self.y - Point.origin[1])**2)


p = Point(1, 2)
print(f'p has x coordinate {p.x} and y coordinate {p.y}')
print(f'p is represented by the dictionary {p.__dict__}')
p.radius = 42
print(f'p is represented by the dictionary {p.__dict__}')