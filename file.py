import pygame
import random
import time
import ball
import paddle
import pingpongphysics

WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
circle_palette = [BLUE, GREEN, RED]
TEXTCOLOR = (0,   0,  0)
(width, height) = (400, 600)
background_color = WHITE


def main():
    # initialize pygame and create window
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("TUFF")

    # set game to running
    game_over = False

    myball = ball.Ball(width//2, 300, 4, 0, 20)
    mypaddle = paddle.Paddle(170, 300, 70, 20)
    gravity = 1.0

    while not game_over:
        time.sleep(0.01667)
        # print(ball_y, dy)
        # +0 +1 +2 +3 +4 +5 -4 -3 -2 -1 0

        # update positions
        pos = pygame.mouse.get_pos()
        mypaddle.move_to(pos[0], pos[1], width, height)
        myball.move(width, height)

        # check for collisions and create/destroy objects
        pingpongphysics.handle_collision(myball, mypaddle)

        # process the events (which might change position/physics)
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                # pos = pygame.mouse.get_pos()
                # pick = random.choice(circle_palette)
                # pygame.draw.circle(screen, pick, pos, random.randint(10, 50))
                # when mouse button is released, bounce the ll.ll so it goes the other way
                myball.bounce_y()

            if event.type == pygame.QUIT:
                game_over = True

        # apply physics
        myball.accelerate(gravity)

        # clear the screen
        screen.fill(background_color)

        # draw things
        myball.draw(screen, BLUE)
        mypaddle.draw(screen, GREEN)

        # update the display
        pygame.display.update()


if __name__ == '__main__':
    main()
