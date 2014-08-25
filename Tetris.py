# -*- coding: utf-8 -*-
import pygame, random
from pygame.locals import *
from Tetrimino import Grid, Tetrimino, Shape
from Ui import Ui, UiConfig

class Game(object):

    FPS = 60
    SHAPES = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
    FALL_EVENT = USEREVENT + 1
    MAX_LEVEL = 9
    MAX_SPEED = 10
    LEFT_BUTTON = 1
    LEVEL_UP = 10
    SPEED = {0 : 1000, 1 : 900, 2 : 800, 3 : 700, 4 : 600, 5 : 500, \
             6 : 400, 7 : 300, 8 : 200, 9 : 100, 10: 75}
    
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.state = 'notRunning'
        self.mainScreen = pygame.display.set_mode(UiConfig.mainScreen['SIZE'].tuple())
        self.gameOverImage = pygame.image.load('game-over.png').convert_alpha()
        self.gameUi = Ui(self.mainScreen)
        self.grid = Grid(UiConfig.grid['POS'], self.mainScreen)
        self.clock = pygame.time.Clock()
        pygame.mixer.music.load("sound.ogg")
        #control how held keys are repeated
        pygame.key.set_repeat(100, 100)
        self.handleEvent()
    
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, speed):
        self._speed = speed
        pygame.time.set_timer(self.FALL_EVENT, self._speed)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score
        self.gameUi.infoBox.score = score
        
    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, level):
        self._level = level
        self.gameUi.infoBox.level = level

    def levelUp(self):
        self.level += 1
        self.lines = 0

    def handleEvent(self):
        while 1:
            #限制FPS为60帧
            self.clock.tick(60)
            for event in pygame.event.get():
                self.eventHandler(event)
    
    def randomShape(self):
        return Shape.new(random.choice(self.SHAPES))
    
    def randomTetrimino(self):
        shape = self.randomShape()
        return Tetrimino(shape, shape.COLOR, surface = self.mainScreen, \
                         grid = self.grid)

    def newGame(self):
        self.grid = Grid(UiConfig.grid['POS'], self.mainScreen)
        self.grid.update()
        self.level = 0
        self.score = 0
        self.lines = 0
        self.tetrimino = self.randomTetrimino()
        self.tetrimino.draw()
        self.nextTetrimino = self.randomTetrimino()
        self.gameUi.tetriminoBox.tetrimino = self.nextTetrimino
        #The first event will not appear until the amount of time has passed.
        self.speed = self.SPEED[self.level]
        self.gameUi.Pause.text = 'Pause'
        self.state = 'running'
        pygame.mixer.music.play(-1)
    
    def gameOver(self):
        pygame.time.set_timer(self.FALL_EVENT, 0)
        self.state = 'gameOver'
        pygame.mixer.music.stop()
        self.mainScreen.blit(self.gameOverImage, (25, 100))
        pygame.display.update()
    
    def pause(self):
        pygame.time.set_timer(self.FALL_EVENT, 0)
        self.gameUi.Pause.text = 'Resume'
        self.state = 'paused'
        pygame.mixer.music.pause()
    
    def resume(self):
        pygame.time.set_timer(self.FALL_EVENT, self.SPEED[self.level])
        self.gameUi.Pause.text = 'Pause'
        self.state = 'running'
        pygame.mixer.music.unpause()

    def eventHandler(self, event):
        if event.type == pygame.QUIT:
            exit()
        if self.state == 'running':
            if event.type == self.FALL_EVENT:
                self.fallEventHandler(event)
            elif event.type == KEYDOWN or KEYUP:
                self.keyBoardEventHandler(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouseEventHandler(event)

    def mouseEventHandler(self, event):
        #如果按下的是左键
        if event.button == self.LEFT_BUTTON:
            mousePos = pygame.mouse.get_pos()
            if self.gameUi.New.collidepoint(mousePos):
                self.newGame()
            elif self.gameUi.Pause.collidepoint(mousePos):
                if self.state == 'running':
                    self.pause()
                elif self.state == 'paused':
                    self.resume()
            elif self.gameUi.Exit.collidepoint(mousePos):
                exit()
    
    def keyBoardEventHandler(self, event):
        if self.state != 'gameOver':
            if event.type == KEYDOWN:
                self.keydownEventHandler(event)
            elif event.type == KEYUP:
                self.keyupEventHandler(event)
    
    def keyupEventHandler(self, event):
        if event.key == K_DOWN:
            self.speed = self.SPEED[self.level]
    
    def keydownEventHandler(self, event):
        if event.key == pygame.K_LEFT:
            self.tetrimino.moveLeft()
        elif event.key == K_RIGHT:
            self.tetrimino.moveRight()
        elif event.key == K_UP:
            self.tetrimino.rotate()
        elif event.key == K_DOWN:
            if self.speed != self.SPEED[self.MAX_SPEED]:
                self.speed = self.SPEED[self.MAX_SPEED]
    
    def fallEventHandler(self, event):
        if self.tetrimino.bottom + 1 == self.grid.bottom or \
        self.tetrimino.on(self.grid.pieces):
            self.tetrimino.stop()
            filledRows = self.grid.getFilledRows()
            if filledRows:
                #如果不停止下落事件的话会造成消行后新的方块快速下落
                pygame.time.set_timer(self.FALL_EVENT, 0)
                n = len(filledRows)
                self.lines += n
                if self.lines >= self.LEVEL_UP and self.level < self.MAX_LEVEL:
                    self.levelUp()
                self.grid.clearRows(filledRows)
                self.score += (n * 2 - 1)
            if self.nextTetrimino.overlap(self.grid.pieces):
                self.gameOver()
                return
            self.tetrimino = self.nextTetrimino
            self.tetrimino.draw()
            self.nextTetrimino = self.randomTetrimino()
            self.gameUi.tetriminoBox.tetrimino = self.nextTetrimino
            pygame.time.set_timer(self.FALL_EVENT, self.SPEED[self.level])
        else:
            self.tetrimino.moveDown()

if __name__ == '__main__':
    game = Game()