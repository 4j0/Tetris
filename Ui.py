# -*- coding: utf-8 -*-
import pygame
from Button import Button
from Tetrimino import Tetrimino
from Size import Size
from Pos import Pos

class UiConfig(object):

    mainScreen = {'SIZE':Size(520, 540), 'CAPTION':'Tetris', 'BACKGROUND_COLOR':(255, 255, 255)}
    grid = {'POS':Pos(20, 20), 'SIZE':Size(200, 400)}
    tetriminoBox = {'POS':Pos(300, 30), 'SIZE':Size(200, 100), 'BORDER_COLOR':(165, 165, 165), 'BORDER_WIDTH':2}
    infoBox = {'POS':Pos(300, 160), 'SIZE':Size(200, 100), 'BORDER_COLOR':(165, 165, 165), 'BORDER_WIDTH':2}
    New = {'POS':Pos(340, 300), 'SIZE':Size(120, 40)}
    Pause = {'POS':Pos(340, 380), 'SIZE':Size(120, 40)}
    Exit = {'POS':Pos(340, 460), 'SIZE':Size(120, 40)}

class TetriminoBox(object):
    
    def __init__(self, Pos, Size, Surface):
        self.pos = Pos
        self._tetrimino = None
        self.surface = Surface
        self.rect = pygame.Rect(Pos.tuple(), Size.tuple())
        pygame.draw.rect(self.surface, UiConfig.tetriminoBox['BORDER_COLOR'], \
                         self.rect, UiConfig.tetriminoBox['BORDER_WIDTH'])
        
    @property
    def tetrimino(self):
        return self._tetrimino
    
    @tetrimino.setter
    def tetrimino(self, tetrimino):
        if self._tetrimino:
            self._tetrimino.clear()
        pos = Pos(self.pos.x + 50, self.pos.y)
        self._tetrimino = Tetrimino(tetrimino.shape, tetrimino.color, \
                                    surface = tetrimino.surface, pos = pos, \
                                   grid = tetrimino.grid)
        self._tetrimino.draw()

class InfoBox(object):
    
    FONT = {'font':'arial', 'size':20}
    BACKGROUND_COLOR = (255, 255, 255)
    TEXT_COLOR = (0, 0, 0)
    TEXT_POS = {'LevelText':Pos(350, 175), 'ScoreText':Pos(350, 219),
                'Level':Pos(380, 200), 'Score':Pos(380, 242)}
    
    def __init__(self, Pos, Size, Surface):
        self.surface = Surface
        self.rect = pygame.Rect(Pos.tuple(), Size.tuple())
        pygame.draw.rect(self.surface, UiConfig.infoBox['BORDER_COLOR'], \
                         self.rect, UiConfig.infoBox['BORDER_WIDTH'])
        self.font = pygame.font.SysFont(self.FONT['font'], self.FONT['size'])
        self.drawText('Level:', self.TEXT_POS['LevelText'])
        self.levelText = self.drawText('0', self.TEXT_POS['Level'])
        self.drawText('Score:', self.TEXT_POS['ScoreText'])
        self.scoreText = self.drawText('0', self.TEXT_POS['Score'])
        self._level = 0
        self._score = 0
        
    def drawText(self, text, pos):
        _text = self.font.render(text, True, self.TEXT_COLOR)
        # get_rect()
        # get the rectangular area of the Surface
        # get_rect(**kwargs) -> Rect
        # Returns a new rectangle covering the entire surface. This rectangle will always 
        # start at 0, 0 with a width. and height the same size as the image.
        # 
        # You can pass keyword argument values to this function. These named values will 
        # be applied to the attributes of the Rect before it is returned. An example 
        # would be ‘mysurf.get_rect(center=(100,100))’ to create a rectangle for the 
        # Surface centered at a given position.
        textBox = _text.get_rect(center = pos.tuple())
        self.surface.blit(_text, textBox)
        return _text
    
    def clearText(self, text, pos):
        textBox = text.get_rect(center = pos.tuple())
        self.surface.fill(self.BACKGROUND_COLOR, textBox)
        pygame.display.update(textBox)
    
    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, level):
        self._level = level
        self.clearText(self.levelText, self.TEXT_POS['Level'])
        self.levelText = self.drawText(str(self._level), self.TEXT_POS['Level'])
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score
        self.clearText(self.scoreText, self.TEXT_POS['Score'])
        self.scoreText = self.drawText(str(self._score), self.TEXT_POS['Score'])

class Ui(object):
    
    def __init__(self, Surface):
        self.mainScreen = Surface
        pygame.display.set_caption(UiConfig.mainScreen['CAPTION'])
        self.mainScreen.fill(UiConfig.mainScreen['BACKGROUND_COLOR'])
        
        self.tetriminoBox = TetriminoBox(UiConfig.tetriminoBox['POS'], \
                                     UiConfig.tetriminoBox['SIZE'], \
                                     self.mainScreen)
        self.infoBox = InfoBox(UiConfig.infoBox['POS'], \
                                   UiConfig.infoBox['SIZE'], \
                                   self.mainScreen)
        self.New = Button(self.mainScreen, UiConfig.New['POS'], \
                            UiConfig.New['SIZE'], text='New Game')
        self.Pause = Button(self.mainScreen, UiConfig.Pause['POS'], \
                            UiConfig.Pause['SIZE'], text='Pause')
        self.Exit = Button(self.mainScreen, UiConfig.Exit['POS'], \
                           UiConfig.Exit['SIZE'], text='Exit')
        