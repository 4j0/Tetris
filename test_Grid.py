# -*- coding: utf-8 -*-
import unittest
from Grid import *
from Size import Size
from Pos import Pos
from Tetrimino import Piece
import pygame

class TestGrid(Grid):
    
    PIECE_COLOR = (255, 0, 0)
    
    A = (
           (0,0,0,0,0,0,0,0,0,0),
           (1,0,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,1),
           (1,1,0,0,0,0,0,0,1,1),
           (1,1,0,0,0,0,0,0,1,0),
           (1,1,1,0,0,0,0,0,1,1),
           (1,1,1,0,0,0,0,0,1,1),
           (1,1,1,0,0,0,0,0,1,1),
           (1,1,1,1,1,1,0,0,1,1),
           (1,1,1,1,1,1,1,1,1,1),
           (1,1,1,1,1,1,1,1,1,1),
           (1,1,1,1,1,1,1,1,1,1),
           (1,1,1,1,1,1,1,1,1,1),
       )
    
    B = (
           (0,0,0,0,0,0,0,0,0,0),
           (1,0,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,1),
           (1,1,0,0,0,0,0,0,1,1),
           (1,1,0,0,0,0,0,0,1,0),
           (1,1,1,0,0,0,0,0,1,1),
           (1,1,1,0,0,0,0,0,1,1),
           (1,1,1,0,0,0,0,0,1,1),
           (1,1,1,1,1,1,0,0,1,1),
           (1,1,1,1,1,1,0,1,1,1),
           (1,1,1,1,1,1,0,1,1,1),
           (1,1,1,1,1,1,0,1,1,1),
           (0,0,0,0,0,0,0,0,0,0),
       )
    
    C = (
           (0,0,0,0,0,0,0,0,0,0),
           (0,0,0,0,0,0,0,0,0,0),
           (1,0,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,1),
           (1,1,0,0,0,0,0,0,1,1),
           (1,1,0,0,0,0,0,0,1,0),
           (1,1,1,0,0,0,0,0,1,1),
           (1,1,1,0,0,0,0,0,1,1),
           (1,1,1,0,0,0,0,0,1,1),
           (1,1,1,1,1,1,0,0,1,1),
           (1,1,1,1,1,1,0,1,1,1),
           (1,1,1,1,1,1,0,1,1,1),
           (1,1,1,1,1,1,0,1,1,1),
       )

    D = (
           (0,0,0,0,0,0,0,0,0,0),
           (1,0,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,0),
           (1,1,0,0,0,0,0,0,0,1),
           (1,1,0,0,0,0,0,0,1,1),
           (1,1,0,0,0,0,0,0,1,0),
           (1,1,1,0,0,0,0,0,1,1),
           (1,1,1,0,0,0,0,0,1,1),
           (1,1,1,0,0,0,0,0,1,1),
           (1,1,1,1,1,1,0,0,1,1),
           (1,1,1,1,1,1,0,1,1,1),
           (1,1,1,1,1,1,0,1,1,1),
           (1,1,1,1,1,1,0,1,1,1),
           (1,1,1,1,1,1,1,1,1,1),
       )

    def __init__(self, pos, surface, template, rowNum = Grid.ROWNUM, colNum = Grid.COLNUM, \
                squareSize = Grid.SQUARE_SIZE, \
                 color = Grid.COLOR, backGroundColor = Grid.BACKGROUND_COLOR):
        self.pos = pos
        self.squareSize = squareSize
        self.template = template
        self.colNum = colNum
        self.rowNum = rowNum
        self.color = color
        self.size = self.calSize(rowNum, colNum, squareSize)
        self.backGroundColor = backGroundColor
        self.surface = surface
        self.grid = self.init_grid()
        self.border = pygame.Rect(self.pos.tuple(), self.size.tuple())
        self.initTestPieces()
        
    def initTestPieces(self):
        for i, row in enumerate(self.template):
            for j, ele in enumerate(row):
                if ele:
                    rect = self.grid[i][j].inflate(-2, -2) 
                    self.grid[i][j].piece = Piece(Pos(rect.x, rect.y), self.PIECE_COLOR, self)
        


class Test(unittest.TestCase):

    def test_getFilledRows(self):
        grid = TestGrid(Pos(0, 0), None, TestGrid.A)
        filledRows = grid.getFilledRows()
        self.assertEqual(len(filledRows), 4)
        self.assertEqual(filledRows[3], grid.grid[19])
        self.assertEqual(filledRows[2], grid.grid[18])
        self.assertEqual(filledRows[1], grid.grid[17])
        self.assertEqual(filledRows[0], grid.grid[16])
        
    def test_emptyRows(self):
        grid = TestGrid(Pos(0, 0), None, TestGrid.A)
        rows = grid.grid[-2:]
        for row in rows:
            for square in row:
                self.assertIsNotNone(square.piece)
        grid.emptyRows(rows)
        for row in rows:
            for square in row:
                self.assertIsNone(square.piece)

    def test_convertRowsToCols(self):
        grid = TestGrid(Pos(0, 0), None, TestGrid.A)
        row = []
        row.append(grid.grid[19])
        row = grid.convertRowsToCols(row)
        self.assertEqual(row, grid.grid[19])
        rows = grid.grid[-2:]
        _rows = grid.grid[-2:]
        cols = grid.convertRowsToCols(rows)
        self.assertEqual(len(cols), 10)
        for col in cols:
            self.assertEqual(len(col), 2)
        self.assertEquals(cols[9], [rows[0][9], rows[1][9]])
        #确保convert过程中未修改rows
        self.assertEqual(rows, _rows)
    
    def test_dropPieces(self):
        grid = TestGrid(Pos(0, 0), None, TestGrid.B)
        _grid = TestGrid(Pos(0, 0), None, TestGrid.C)
        rows = grid.grid[:19]
        grid.dropPieces(rows)
        for i, row in enumerate(_grid):
            for j, square in enumerate(row):
                if square.piece:
                    self.assertEqual(square.piece, grid.grid[i][j].piece)
                else:
                    self.assertEqual(None, grid.grid[i][j].piece)
        
    def test_clearRows(self):
        grid = TestGrid(Pos(0, 0), None, TestGrid.D)
        _grid = TestGrid(Pos(0, 0), None, TestGrid.C)
        row = grid.getFilledRows()
        grid.clearRows(row)
        for i, row in enumerate(_grid):
            for j, square in enumerate(row):
                if square.piece:
                    self.assertEqual(square.piece, grid.grid[i][j].piece)
                else:
                    self.assertEqual(None, grid.grid[i][j].piece)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()