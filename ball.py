import pygame


class Ball:
    def __init__(self, x, y, dx, dy, rad):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.bounced_y = False

    def get_x(self):
        return int(self.x)

    def get_y(self):
        return int(self.y)

    def get_radius(self):
        return int(self.rad)

    def move(self, width, height):
        self.bounced_y = False
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        # if ball is off the left screen or off the right screen, return it to the screen & invert dx
        # (this will require two different if statements)
        if self.x < 0:
            self.x = 0
            self.dx = -self.dx
        if self.x > width:
            self.x = width
            self.dx = -self.dx

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.get_x(),
                                           self.get_y()), self.get_radius())

    def bounce_y(self):
        self.bounced_y = True
        self.dy = -self.dy

    def bounce_x(self):
        self.dx = -self.dx

    def accelerate(self, gravity):
        if self.bounced_y == False:
            self.dy = self.dy + gravity
