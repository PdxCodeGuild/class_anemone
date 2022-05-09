import math
# import random
class Point:
    def  __helper_function(self):
        print("I am just trying to help...")

    def __init__(self, x, y): # this is the initializer
        self.__x = x # these are member variables
        self.__y = y

    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)
    def scale(self,v):
        self.x*=v
        self.y*=v

p1 = Point(int(input("point 1, x: ")),int(input("point 1, y: "))) # call the initializer, instantiate the class
p2 = Point(int(input("point 2, x: ")),int(input("point 2, y: ")))
print(p1.x) # 5
print(p1.y) # 2
print(type(p1)) # Point
print(round(p1.distance(p2),2))

print(p2.scale(2))

