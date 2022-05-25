import pygame
from lab16tile import Tile

class Level:
    def __init__(self,level_data,surface):
        self.dispalysurface= surface
        self.setup(level_data)
        


    def setup(self, layout):
        self.tiles = pygame.sprite.Group()
        for row in layout:
            