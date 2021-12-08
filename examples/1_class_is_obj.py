from pprint import pprint
from math import sqrt

class Point:
    ''' Class representing a 2D point '''
    origin = (0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_distance_from_origin(self):
        return sqrt((self.x - Point.origin[0])**2 + (self.y - Point.origin[1])**2)


pprint(Point.__dict__)