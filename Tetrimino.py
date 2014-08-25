# -*- coding: utf-8 -*-
import pygame
from Size import Size
from Pos import Pos
from Grid import Grid
from Shapes import Shape

class Piece(pygame.Rect):
    
    SIZE = Size(Grid.SQUARE_SIZE.width -2, Grid.SQUARE_SIZE.height -2)
    
    def __init__(self, pos, color, grid, size = SIZE):
        pygame.Rect.__init__(self, pos.tuple(), size.tuple())
        self.color = color
        self.grid = grid
    
    def on(self, pieces):
        for piece in pieces:
            if self.x == piece.x and (self.y + self.grid.squareSize.height) == \
            piece.y:
                return True
        return False
    
    def overlap(self, pieces):
        #If no collisions are found an index of -1 is returned.
        if self.collidelist(pieces) == -1:
            return False
        return True
        
class Tetrimino(object):
    
    START_POS = Pos(95, -5)
    
    def __init__(self, shape, color, surface, pos = START_POS, pieceSize = Piece.SIZE, \
                 grid = None):
        self.pos = pos
        self.pieceSize = pieceSize
        self.shape = shape
        self.color = color
        self.surface = surface
        self.grid = grid
        self.pieces = self.ShapeToPieces(self.shape)
    
    def __iter__(self):
        return self.pieces.__iter__()
    #待重构
    def ShapeToPieces(self, shape):
        pieces = []
        for rowIndex, row in enumerate(shape):
            for colIndex, col in enumerate(row):
                if col:
                    x = (self.pos.x + 1) + (self.grid.squareSize.width * colIndex)
                    y = (self.pos.y + 1) + (self.grid.squareSize.height * rowIndex)
                    pos = Pos(x, y)
                    pieces.append(Piece(pos, self.color, self.grid))
        return pieces
    
    def draw(self):
        for piece in self:
            self.surface.fill(piece.color, piece)
        pygame.display.update(self.pieces)
        
    def clear(self):
        for piece in self:
            self.surface.fill(self.grid.backGroundColor, piece)
        pygame.display.update(self.pieces)
        
    def move(self, pos):
        return Tetrimino(self.shape, self.color, pos = pos, \
                         surface = self.surface, grid = self.grid)

    def move_ip(self, pos):
        self.pos = pos
        self.clear()
        #待重构
        self.pieces = self.ShapeToPieces(self.shape)
        self.draw()

    def rotate(self):
        shape = self.shape.rotate()
        tetrimino = Tetrimino(shape, shape.COLOR, pos = self.pos, \
                         surface = self.surface, grid = self.grid)
        if tetrimino.isInValidPos():
            self.rotate_ip()

    def rotate_ip(self):
        self.clear()
        self.shape.rotate_ip()
        self.pieces = self.ShapeToPieces(self.shape)
        self.draw()
        
    def isInValidPos(self):
        return self.inside(self.grid) and not self.overlap(self.grid.pieces)

    def moveLeft(self):
        pos = Pos(self.pos.x - self.grid.squareSize.width, self.pos.y)
        tetrimino = self.move(pos)
        if tetrimino.isInValidPos():
            self.move_ip(pos)

    def moveRight(self):
        pos = Pos(self.pos.x + self.grid.squareSize.width, self.pos.y)
        tetrimino = self.move(pos)
        if tetrimino.isInValidPos():
            self.move_ip(pos)
    
    def moveDown(self):
        pos = Pos(self.pos.x, self.pos.y + self.grid.squareSize.width)
        self.move_ip(pos)
        
    @property
    def bottom(self):
        bottom = 0
        for piece in self:
            if piece.bottom > bottom:
                bottom = piece.bottom
        return bottom
    
    def inside(self, grid):
        for piece in self:
            if not grid.contains(piece):
                return False
        return True

    def on(self, pieces):
        for piece in self:
            if piece.on(pieces):
                return True
        return False

    def overlap(self, pieces):
        for piece in self:
            if piece.overlap(pieces):
                return True
        return False
            
    def stop(self):
        for piece in self:
            self.grid.receive(piece)