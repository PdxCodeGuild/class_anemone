import math
from re import A
# import random
class Point:
    def  __helper_function(self):
        print("I am just trying to help...")

    def __init__(self, x, y): # this is the initializer
        self.x = x # these are member variables
        self.y = y

    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)
    def scale(self,v):
        self.x*=v
        self.y*=v

# p1 = Point(int(input("point 1, x: ")),int(input("point 1, y: "))) # call the initializer, instantiate the class
# p2 = Point(int(input("point 2, x: ")),int(input("point 2, y: ")))
# print(p1.x) # 5
# print(p1.y) # 2
# print(type(p1)) # Point
# print(round(p1.distance(p2),2))

# print(p2.scale(2))

class Dictlist:
    # def __init__(self)
    pass



# ==============================================================================

"""inheritance"""
# have something that pulls from a super class
# and have things be inherited form it
# 

class Animal:
    def __init__(self, name, food):
        self.name = name
        self.fav_food = food

class Squirrel(Animal):
    def __init__(self, name, food):
        super().__init__(name, food)
        self.animal = "squirrel"
        self.legs = 4

class Anteater(Animal):
    def __init__(self, name, food):
        super().__init__(name, food)
        self.animal = "anteater"
        self.legs = 4

class Snake(Animal):
    def __init__(self, name, food):
        super().__init__(name, food)
        self.animal = "snake"  
        self.legs = 0

s = Squirrel("Clarence", "nuts") # (name, food)
print(f"\nanimal: {s.animal}\nname: {s.name}\nfood: {s.fav_food}\nlegs: {s.legs}")           
shell = []
a = Anteater("Jimmy", "ants")
shell +=s,a
print(f"\nanimal: {a.animal}\nname: {a.name}\nfood: {a.fav_food}\nlegs: {a.legs}")  
print(repr(Animal))

"""dunder methods, class methods"""