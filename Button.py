# -*- coding: utf-8 -*-
import pygame
 
class Button(object):

    FONT = {'font':'arial', 'size':20}
    COLOR = (165, 165, 165)
    BORDER_WIDTH = 2
    TEXT_COLOR = (0, 0, 0)
    BACKGROUND_COLOR = (255, 255, 255)

    def __init__(self, surface, pos, size, text = 'Text', \
                 textColor = TEXT_COLOR, color = COLOR, \
                 bgColor = BACKGROUND_COLOR):
        self.surface = surface
        self.pos = pos
        self.size = size
        self.textColor = textColor
        self.color = color
        self.bgColor = bgColor
        self.rect = pygame.Rect(self.pos.tuple(), self.size.tuple())
        self.font = pygame.font.SysFont(self.FONT['font'], self.FONT['size'])
        self._text =  self.font.render(text, True, self.textColor)
        self.textBox = self._text.get_rect()
        self.adjustTextPos()
        self.update()
        
    def adjustTextPos(self):
        self.textBox.center = self.rect.center
    
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text):
        self._text =  self.font.render(text, True, self.textColor)
        self.textBox = self._text.get_rect()
        self.adjustTextPos()
        self.update()
        
    def update(self):
        self.surface.fill(self.bgColor, self.rect)
        pygame.draw.rect(self.surface, self.color, self.rect , self.BORDER_WIDTH)
        self.surface.blit(self._text, self.textBox)
        pygame.display.update()

    def collidepoint(self, pos):
        return self.rect.collidepoint(pos)