from cgitb import text
import os
import pygame
from pygame.math import Vector2
from pygame import Rect


os.environ['SDL_VIDEO_CENTERED'] = '1'

class Unit():
    def __init__(self, state, position, tile):
        self.state = state
        self.position = position
        self.tile = tile

    def move(self, moveVector):
        raise NotImplementedError()

class Tank(Unit):
    def move(self, moveVector):
        newPos = self.position + moveVector

        if newPos.x < 0 or newPos.x >= self.state.worldSize.x \
        or newPos.y < 0 or newPos.y >= self.state.worldSize.y:
            return
        
        for unit in self.state.units:
            if newPos == unit.position:
                return

        self.position = newPos

class Tower(Unit):
    def move(self, moveVector):
        pass



class GameState():


    def __init__(self):
        self.worldSize = Vector2(16,10)
        self.units = [
            Tank(self,Vector2(5, 4), Vector2(1, 0)),
            Tower(self, Vector2(10, 3), Vector2(0, 1)),
            Tower(self, Vector2(10, 5), Vector2(0, 1))
        ]
        self.ground = [ 
            [ Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1)],
            [ Vector2(5,1), Vector2(5,1), Vector2(7,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(7,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(6,4), Vector2(7,2), Vector2(7,2)],
            [ Vector2(5,1), Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(6,1), Vector2(6,2), Vector2(5,1), Vector2(6,1), Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(6,1), Vector2(5,1)],
            [ Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(7,1)],
            [ Vector2(5,1), Vector2(7,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,5), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(8,5), Vector2(5,1), Vector2(5,1)],
            [ Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(7,1)],
            [ Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(7,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(7,1), Vector2(5,1)],
            [ Vector2(5,1), Vector2(5,1), Vector2(6,4), Vector2(7,2), Vector2(7,2), Vector2(8,4), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(5,1)],
            [ Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(7,1), Vector2(5,1), Vector2(5,1), Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(7,4), Vector2(7,2), Vector2(7,2)],
            [ Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1)]
        ]
                                                                                        # self.tankPos = Vector2(5,4)
                                                                                        # self.towersPos = [
                                                                                        #     Vector2(10, 3),
                                                                                        #     Vector2(10, 5)
                                                                                        # ]
                                                                                        # self.tower1Pos = Vector2(10, 3)
                                                                                        # self.tower2Pos = Vector2(10, 5)

    def worldWidth(self):
        return int(self.worldSize.x)

    def worldHeight(self):
        return int(self.worldSize.y)


    def update(self, moveTankCommand):
        for unit in self.units:
            unit.move(moveTankCommand)
                                                                                        # newTankPos = self.tankPos + moveTankCommand

        
                                                                                        # if newTankPos.x < 0 or newTankPos.x >= self.worldSize.x \
                                                                                        #     or newTankPos.y < 0 or newTankPos.y >= self.worldSize.y:
                                                                                        #     return
                                                                                        # for position in self.towersPos:
                                                                                        #     if newTankPos == position:
                                                                                        #         return
                                                                                        # self.tankPos == newTankPos
          
                                                                                        # if  newTankPos.x >= 0 and newTankPos.x < self.worldSize.x \
                                                                                        # and newTankPos.y >= 0 and newTankPos.y < self.worldSize.y \
                                                                                        # and newTankPos != self.tower1Pos and newTankPos != self.tower2Pos:
                                                                                        #     self.tankPos = newTankPos
                                                                                        # self.tankPos += moveTankCommand

                                                                                        # if self.tankPos.x < 0:
                                                                                        #     self.tankPos.x = 0
                                                                                        # elif self.tankPos.x >= self.worldSize.x:
                                                                                        #     self.tankPos.x = self.worldSize.x - 1

                                                                                        # if self.tankPos.y < 0:
                                                                                        #     self.tankPos.y = 0
                                                                                        # elif self.tankPos.y >= self.worldSize.y:
                                                                                        #     self.tankPos.y = self.worldSize.y - 1


class UserInterface():
    
    
    def __init__(self):
        pygame.init()
        
        self.gameState = GameState()
        
        self.cellSize = Vector2(64,64)
        self.unitsTexture = pygame.image.load('13_tank_tileset-1024x1024.png')

        windowSize = self.gameState.worldSize.elementwise() * self.cellSize
        self.window = pygame.display.set_mode((int(windowSize.x), int(windowSize.y)))        
        pygame.display.set_caption('This may end up being Tic Tac Toe... I dont know yet.')
        pygame.display.set_icon(pygame.image.load('01_image.png'))
        self.moveTankCommand = Vector2(0,0)
        
        self.clock = pygame.time.Clock()
        self.running = True 
                

    def processInput(self):
        self.moveTankCommand = Vector2(0,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d :
                    self.moveTankCommand.x += 1
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.moveTankCommand.x -= 1
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.moveTankCommand.y += 1
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.moveTankCommand.y -= 1
        
   
    def cellWidth(self):
        return int(self.cellSize.x)

    def cellHeight(self):
        return int(self.cellSize.y)


    def update(self):
        self.gameState.update(self.moveTankCommand)

    
    def renderGround(self, position, tile):
        spritePoint= position.elementwise() * self.cellSize

        texturePoint = tile.elementwise()*self.cellSize
        textureRect = Rect(int(texturePoint.x), int(texturePoint.y), self.cellWidth, self.cellHeight)
        self.window.blit(self.groundTexture,spritePoint,textureRect)


    def renderUnit(self, unit):
        spritePoint = unit.position.elementwise() * self.cellSize
    
        texturePoint = unit.tile.elementwise()*self.cellSize
        textureRect = Rect(int(texturePoint.x), int(texturePoint.y), self.cellWidth, self.cellHeight)
        self.window.blit(self.unitsTexture,spritePoint,textureRect)
    
        texturePoint = Vector2(0,6).elementwise()*self.cellSize
        textureRect = Rect(int(texturePoint.x), int(texturePoint.y), self.cellWidth, self.cellHeight)
        self.window.blit(self.unitsTexture,spritePoint,textureRect)
    
    def render(self):
        self.window.fill((0,0,0))
        
        for unit in self.gameState.units:
            self.renderUnit(unit)

        for y in range(int(self.gameState.worldSize.y)):
            for x in range(int(self.gameState.worldSize.x)):
                self.renderGround(Vector2(x,y),self.gameState.ground[y][x])
                                                                                                    # for position in self.gameState.towersPos:
                                                                                                    #     spritePoint = position.elementwise() * self.cellSize
                                                                                                    #     texturePoint = Vector2(0,1).elementwise() * self.cellSize
                                                                                                    #     textureRect = Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x), int(self.cellSize.y))
                                                                                                    #     self.window.blit(self.unitsTexture, spritePoint, textureRect)
                                                                                                    #     texturePoint = Vector2(0,6).elementwise()*self.cellSize
                                                                                                    #     textureRect = Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x),int(self.cellSize.y))
                                                                                                    #     self.window.blit(self.unitsTexture,spritePoint,textureRect)
                                                                                                    
                                                                                                    # spritePoint = self.gameState.tower2Pos.elementwise() * self.cellSize
                                                                                                    # texturePoint = Vector2(0,1).elementwise() * self.cellSize
                                                                                                    # textureRect = Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x), int(self.cellSize.y))
                                                                                                    # self.window.blit(self.unitsTexture, spritePoint, textureRect)
                                                                                                    # texturePoint = Vector2(0,6).elementwise()*self.cellSize
                                                                                                    # textureRect = Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x),int(self.cellSize.y))
                                                                                                    # self.window.blit(self.unitsTexture,spritePoint,textureRect)
        
                                                                                                    # spritePoint = self.gameState.tankPos.elementwise() * self.cellSize
                                                                                                    # texturePoint = Vector2(1,0).elementwise() * self.cellSize
                                                                                                    # textureRect = Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x), int(self.cellSize.y))
                                                                                                    # self.window.blit(self.unitsTexture,spritePoint,textureRect)
                                                                                                    # texturePoint = Vector2(0,6).elementwise() * self.cellSize
                                                                                                    # textureRect = Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x), int(self.cellSize.y))
                                                                                                    # self.window.blit(self.unitsTexture,spritePoint,textureRect)
        
        pygame.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)



game = UserInterface()
game.run()

