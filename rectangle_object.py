import pygame


class rectangle_object:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_x(self):
        return int(self.x)

    def get_y(self):
        return int(self.y)

    # get width
    def get_width(self):
        return int(self.w)

    # get height
    def get_height(self):
        return int(self.h)

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, (self.get_x() - (self.get_width()/2),
                                         self.get_y() - (self.get_height()/2),
                                         self.get_width(), self.get_height()))

    def move_to(self, x, y, width, height):
        self.x = x
        self.y = y
        if self.x < 0:
            self.x = 0
        if self.x > width:
            self.x = width
        if self.y < 400:
            self.y = 400
        if self.y > height:
            self.y = height
