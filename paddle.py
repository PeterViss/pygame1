import pygame
import rectangle_object


class Paddle(rectangle_object.rectangle_object):
    def __init__(self, x, y, w, h):
        super(Paddle, self).__init__(x, y, w, h)
