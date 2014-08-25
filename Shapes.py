# -*- coding: utf-8 -*-

class Shape(object):

    def __init__(self):
        self.shapeIndex = 0
        self.shapeNum = len(self.SHAPES)
    
    @staticmethod    
    def new(shapeName):
        return eval(shapeName + '()')

    def __iter__(self):
        return self.SHAPES[self.shapeIndex].__iter__()
    
    def rotate(self):
        shape = Shape.new(self.__class__.__name__)
        shape.shapeIndex = self.shapeIndex
        shape.rotate_ip()
        return shape

    def rotate_ip(self):
        if self.shapeNum > 1:
            if self.shapeIndex == self.shapeNum - 1:
                self.shapeIndex = 0
            else:
                self.shapeIndex += 1

class O(Shape):

    COLOR = (255, 255, 0)

    SHAPES = (
              (
                (0, 0, 0, 0),
                (0, 1, 1, 0),
                (0, 1, 1, 0),
                (0, 0, 0, 0),
                ),
              )

class I(Shape):

    COLOR = (38, 38, 38)

    SHAPES = (
               (
                (0, 0, 0, 0),
                (1, 1, 1, 1),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                ),
               (
                (0, 1, 0, 0),
                (0, 1, 0, 0),
                (0, 1, 0, 0),
                (0, 1, 0, 0),
                )
              )

class Z(Shape):

    COLOR = (228, 0, 0)

    SHAPES = (
               (
                (0, 0, 0, 0),
                (1, 1, 0, 0),
                (0, 1, 1, 0),
                (0, 0, 0, 0),
                ),
               (
                (0, 0, 1, 0),
                (0, 1, 1, 0),
                (0, 1, 0, 0),
                (0, 0, 0, 0),
                )
               )

class S(Shape):

    COLOR = (0, 204, 0)

    SHAPES = (
               (
                (0, 0, 0, 0),
                (0, 1, 1, 0),
                (1, 1, 0, 0),
                (0, 0, 0, 0),
                ),
               (
                (1, 0, 0, 0),
                (1, 1, 0, 0),
                (0, 1, 0, 0),
                (0, 0, 0, 0),  
                )
               )

class L(Shape):

    COLOR = (255, 102, 0)

    SHAPES = (
               (
                (0, 0, 0, 0),
                (0, 0, 1, 0),
                (1, 1, 1, 0),
                (0, 0, 0, 0),
                ),
               (
                (1, 1, 0, 0),
                (0, 1, 0, 0),
                (0, 1, 0, 0),
                (0, 0, 0, 0),
                ),
               (
                (0, 0, 0, 0),
                (1, 1, 1, 0),
                (1, 0, 0, 0),
                (0, 0, 0, 0),
                ),
               (
                (0, 1, 0, 0),
                (0, 1, 0, 0),
                (0, 1, 1, 0),
                (0, 0, 0, 0),
                )
               )

class J(Shape):

    COLOR = (0, 0, 255)

    SHAPES = (
               (
                (0, 0, 0, 0),
                (1, 0, 0, 0),
                (1, 1, 1, 0),
                (0, 0, 0, 0),
                ),
               (
                (0, 1, 1, 0),
                (0, 1, 0, 0),
                (0, 1, 0, 0),
                (0, 0, 0, 0),
                ),
               (
                (0, 0, 0, 0),
                (1, 1, 1, 0),
                (0, 0, 1, 0),
                (0, 0, 0, 0),
                ),
               (
                (0, 1, 0, 0),
                (0, 1, 0, 0),
                (1, 1, 0, 0),
                (0, 0, 0, 0),
                )
               )

class T(Shape):

    COLOR = (204, 51, 153)

    SHAPES = (
               (
                (0, 0, 0, 0),
                (1, 1, 1, 0),
                (0, 1, 0, 0),
                (0, 0, 0, 0),
                ),
               (
                (0, 1, 0, 0),
                (1, 1, 0, 0),
                (0, 1, 0, 0),
                (0, 0, 0, 0),
                ),
               (
                (0, 1, 0, 0),
                (1, 1, 1, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                ),
               (
                (0, 1, 0, 0),
                (0, 1, 1, 0),
                (0, 1, 0, 0),
                (0, 0, 0, 0),
                )
               )
