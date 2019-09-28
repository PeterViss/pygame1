
def handle_collision(my_circle_object, my_rectangle_object):
    # bx by px py rad
    bx = my_circle_object.get_x()
    by = my_circle_object.get_y()
    px = my_rectangle_object.get_x()
    py = my_rectangle_object.get_y()
    # right side
    right_diff = bx - px
    # left side
    left_diff = px - bx
    # ball is above the paddle
    up_diff = py - by
    # ball is lower than the paddle
    down_diff = by - py
    # ball is on the left side of the paddle
    thick = my_rectangle_object.get_height()/2
    length = my_rectangle_object.get_width()/2
    rad = my_circle_object.get_radius()
    # side of paddle
    corner_size = ((rad * rad)/2) ** 0.5

    if up_diff > 0 and up_diff < (rad + thick):
        if right_diff > 0:
            if right_diff < (length + corner_size):
                my_circle_object.bounce_y()
            elif right_diff < (length + rad):
                my_circle_object.bounce_x()
        if left_diff > 0:
            if left_diff < (length + corner_size):
                my_circle_object.bounce_y()
            elif left_diff < (length + rad):
                my_circle_object.bounce_x()

    if down_diff > 0 and down_diff < (rad + thick):
        if right_diff > 0:
            if right_diff < (length + corner_size):
                my_circle_object.bounce_y()
            elif right_diff < (length + rad):
                my_circle_object.bounce_x()
        if left_diff > 0:
            if left_diff < (length + corner_size):
                my_circle_object.bounce_y()
            elif left_diff < (length + rad):
                my_circle_object.bounce_x()
