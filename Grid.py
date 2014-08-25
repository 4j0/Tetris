# -*- coding: utf-8 -*-
import pygame
from Size import Size
from Pos import Pos

class Grid(object):
    
    ROWNUM = 20
    COLNUM = 10
    SQUARE_SIZE = Size(25, 25)
    COLOR = (165, 165, 165)
    BACKGROUND_COLOR = (255, 255, 255)

    def __init__(self, pos, surface, rowNum = ROWNUM, colNum = COLNUM, \
                squareSize = SQUARE_SIZE, \
                 color = COLOR, backGroundColor = BACKGROUND_COLOR):
        self.pos = pos
        self.squareSize = squareSize
        self.colNum = colNum
        self.rowNum = rowNum
        self.color = color
        self.size = self.calSize(rowNum, colNum, squareSize)
        self.backGroundColor = backGroundColor
        self.surface = surface
        self.grid = self.init_grid()
        self.border = pygame.Rect(self.pos.tuple(), self.size.tuple())
        self.outerBorder = pygame.Rect(self.border.inflate(2, 2))
        self.draw()
    
    def __iter__(self):
        return self.grid.__iter__()
    
    def __len__(self):
        return len(self.grid)
    
    def __getitem__(self, index):
        return self.grid[index]
    
    def calSize(self, rowNum, colNum, squareSize):
        width =  colNum * squareSize.width
        height = rowNum * squareSize.height
        return Size(width, height)

    def init_grid(self):
        grid = []
        for i in range(self.rowNum):
            y = self.pos.y + (self.squareSize.height * i)
            grid.append(Row(Pos(self.pos.x, y), self))
        return grid
# 
    def receive(self, piece):
        row = (piece.y - self.pos.y + 1) / self.squareSize.height
        col = (piece.x - self.pos.x + 1) / self.squareSize.width
        self.grid[row][col].piece = piece
    
    def getFilledRows(self):
        filledRows = []
        for row in self:
            if row.isFilled():
                filledRows.append(row)
        return filledRows

    def mapFn(self, *rows):
        return list(rows)

    def convertRowsToCols(self, rows):
        if len(rows) == 1:
            return rows[0]
        return map(self.mapFn, *rows)

    def clearRows(self, rows):
        self.emptyRows(rows)
        cols = self.convertRowsToCols(rows)
        self.clearCols(cols)
        sliceIndex = self.index(rows[-1])
        rows = self.grid[:sliceIndex]
        self.dropPieces(rows)
        self.updateRows(self.grid[:sliceIndex + 1])
    
    def index(self, row):
        return self.grid.index(row)
    
    def emptyRows(self, rows):
        for row in rows:
            row.empty()
   
    def empty(self):
        for row in self:
            row.empty()
    
    def clearCols(self,cols):
        for col in cols:
            self.clearCol(col)
            pygame.time.delay(25)

    def clearCol(self, col):
        #判断是Square还是col,pygame.Rect对象是可迭代的，如果不加判断会迭代Rect.
        if isinstance(col, Square):
            rect = col.inflate(-2, -2)
            self.surface.fill(self.backGroundColor, rect)
            pygame.display.update(col)
        else:
            for square in col:
                rect = square.inflate(-2, -2)
                self.surface.fill(self.backGroundColor, rect)
            pygame.display.update(col)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.outerBorder, 1)
        pygame.display.update(self.outerBorder)
        for row in self:
            row.draw()
            
    def dropPieces(self, rows):
        for row in reversed(rows):
            if not row.isEmpty():
                row.dropPieces()
            
    def clear(self):
        for row in self:
            row.clear()

    def update(self):
        self.clear()
        self.draw()
        
    def updateRows(self, rows):
        for row in rows:
            row.clear()
        #把clear和draw分开来是因为视觉上这样会比较好一点
        for row in rows:
            row.draw()

    @property
    def pieces(self):
        pieces = []
        for row in self.grid:
            if row.pieces:
                pieces.extend(row.pieces)
        return pieces
    
    @property
    def bottom(self):
        return self.border.bottom

    def contains(self, piece):
        return self.border.contains(piece)
    
class Row(list):
    
    def __init__(self, pos, grid):
        self._pos = pos
        self.grid = grid
        self.colNum = grid.colNum
        self.surface = grid.surface
        self.backGroundColor = grid.backGroundColor
        self.squareSize = grid.squareSize
        squares = [Square(Pos(0, 0), self.backGroundColor, self.squareSize) \
         for i in range(self.colNum)]
        list.__init__(self, squares)
        self.pos = self._pos
        
    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        self._pos = pos
        for i, square in enumerate(self):
            square.pos = Pos(self._pos.x + (i * self.squareSize.width), self._pos.y)
     
    def isFilled(self):
        for square in self:
            if square.piece == None:
                return False
        return True
    
    @property
    def pieces(self):
        pieces = []
        for square in self:
            if square.piece:
                pieces.append(square.piece)
        return pieces
    
    @pieces.setter
    def pieces(self, pieces):
        for piece in pieces:
            i = (piece.x - 1 - piece.grid.pos.x) / self.squareSize.width
            self[i].piece = piece
    
    def clear(self):
        for square in self:
            rect = square.inflate(-2, -2)
            self.surface.fill(self.backGroundColor, rect)
        pygame.display.update(self)
    
    def draw(self):
        for square in self:
            pygame.draw.rect(self.surface, self.grid.color, square, 1)
            if square.piece:
                self.surface.fill(square.piece.color, square.piece)
        pygame.display.update(self)
    
    def dropPieces(self):
        nextRow = self.nextRow()
        if nextRow and nextRow.isEmpty():
            self.downPieces()
            nextRow.pieces = self.pieces
            self.empty()
            nextRow.dropPieces()
    
    def downPieces(self):
        self.setPiecesY(self.pos.y + 1 + self.squareSize.height)
    
    def setPiecesY(self, y):
        for piece in self.pieces:
            piece.y = y
    
    def nextRow(self):
        i = self.grid.index(self) + 1
        if i < len(self.grid):
            return self.grid[i]
        return None
        
    def isEmpty(self):
        for square in self:
            if square.piece:
                return False
        return True
        
    def empty(self):
        for square in self:
            square.piece = None

class Square(pygame.Rect):
    
    def __init__(self, pos, color, size):
        self._pos = pos
        self.color = color
        self.piece = None
        pygame.Rect.__init__(self, self._pos.tuple(), size.tuple())
        
    @property
    def pos(self):
        return self._pos
    
    @pos.setter
    def pos(self, pos):
        self._pos = pos
        self.x = self._pos.x
        self.y = self._pos.y
        if self.piece:
            self.piece.x = self._pos.x + 1
            self.piece.y = self._pos.y + 1