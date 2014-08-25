class Size(object):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def tuple(self):
        return (self.width, self.height)