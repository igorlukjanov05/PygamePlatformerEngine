import pygame
import time
import ppe.events


class GameObject(object):
    def __init__(self, current=None, topleft=None):
        self.__topleft = topleft
        self.current = current

        self.__gravity = None

        self.__x_speed = None
        self.__y_speed = None

        self.__max_positive_x_speed = None
        self.__max_negative_x_speed = None

        self.__max_positive_y_speed = None
        self.__max_negative_y_speed = None

        self.__x_positive_acceleration = None
        self.__x_negative_acceleration = None

        self.__x_positive_deceleration = None
        self.__x_negative_deceleration = None

        self.__jump_power = None

        self.__on_ground = None

        self.__move_left_keys = None
        self.__move_right_keys = None

        self.__animation = None
        self.__animation_time_per_frame = None
        self.__last_animation_time = None

    def init_animation(self):
        self.__animation_time_per_frame = 0.05
        self.__last_animation_time = time.time()

    def animate(self):
        if self.__animation is not None \
                and self.__last_animation_time is not None \
                and self.__animation_time_per_frame is not None:
            if time.time() - self.__last_animation_time >= self.__animation_time_per_frame:
                self.__last_animation_time = time.time()
                self.__animation()

    def animator(self, time_per_frame=0.05):
        def wrapper(func):
            self.__animation = func
            self.__animation_time_per_frame = time_per_frame
        return wrapper

    def move_left(self, keys=(pygame.K_LEFT, pygame.K_a)):
        self.__move_left_keys = keys

    def move_right(self, keys=(pygame.K_RIGHT, pygame.K_d)):
        self.__move_right_keys = keys

    def fall(self):
        if not self.__on_ground:
            self.__y_speed += self.__gravity
            if self.__y_speed > self.__max_positive_y_speed:
                self.__y_speed = self.__max_positive_y_speed

    def change_x_speed(self):
        move_left = False
        move_right = False
        if type(self.__move_left_keys) is int:
            move_left = True if ppe.events.pressed_keys[self.__move_left_keys] else move_left
        elif self.__move_left_keys is not None:
            for lk in self.__move_left_keys:
                move_left = True if ppe.events.pressed_keys[lk] else move_left

        if type(self.__move_right_keys) is int:
            move_right = True if ppe.events.pressed_keys[self.__move_right_keys] else move_right
        elif self.__move_right_keys is not None:
            for rk in self.__move_right_keys:
                move_right = True if ppe.events.pressed_keys[rk] else move_right

        if move_right and not move_left:
            self.__x_speed += self.__x_positive_acceleration
            if self.__x_speed > self.__max_positive_x_speed:
                self.__x_speed = self.__max_positive_x_speed
        elif move_left and not move_right:
            self.__x_speed -= self.__x_negative_acceleration
            if self.__x_speed < -self.__max_negative_x_speed:
                self.__x_speed = -self.__max_negative_x_speed
        elif not move_right and not move_left:
            if self.__x_speed > 0:
                self.__x_speed -= self.__x_positive_deceleration
                if self.__x_speed < 0:
                    self.__x_speed = 0
            elif self.__x_speed < 0:
                self.__x_speed += self.__x_negative_deceleration
                if self.__x_speed > 0:
                    self.__x_speed = 0

    def main_speed(self, events):
        self.__on_ground = False
        self.fall()
        self.change_x_speed()
        self.animate()

    def main_pos(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def init_physics(self, gravity=0.1, x_speed=0,
                     y_speed=0, max_positive_x_speed=5,
                     max_negative_x_speed=5, max_positive_y_speed=10,
                     max_negative_y_speed=10, x_positive_acceleration=0.4,
                     x_negative_acceleration=0.4, x_positive_deceleration=0.3,
                     x_negative_deceleration=0.3, jump_power=8):
        self.__gravity = gravity
        self.__x_speed = x_speed
        self.__y_speed = y_speed
        self.__max_positive_x_speed = max_positive_x_speed
        self.__max_negative_x_speed = max_negative_x_speed
        self.__max_positive_y_speed = max_positive_y_speed
        self.__max_negative_y_speed = max_negative_y_speed
        self.__x_positive_acceleration = x_positive_acceleration
        self.__x_negative_acceleration = x_negative_acceleration
        self.__x_positive_deceleration = x_positive_deceleration
        self.__x_negative_deceleration = x_negative_deceleration
        self.__jump_power = jump_power

    @property
    def last_animation_time(self):
        return self.__last_animation_time

    @last_animation_time.setter
    def last_animation_time(self, value):
        self.__last_animation_time = value

    @property
    def animation_time_per_frame(self):
        return self.__animation_time_per_frame

    @animation_time_per_frame.setter
    def animation_time_per_frame(self, value):
        self.__animation_time_per_frame = value

    @property
    def on_ground(self):
        return self.__on_ground

    @on_ground.setter
    def on_ground(self, value):
        self.__on_ground = value

    @property
    def gravity(self):
        return self.__gravity

    @gravity.setter
    def gravity(self, value):
        self.__gravity = value

    @property
    def x_speed(self):
        return self.__x_speed

    @x_speed.setter
    def x_speed(self, value):
        self.__x_speed = value

    @property
    def y_speed(self):
        return self.__y_speed

    @y_speed.setter
    def y_speed(self, value):
        self.__y_speed = value

    @property
    def max_positive_x_speed(self):
        return self.__max_positive_x_speed

    @max_positive_x_speed.setter
    def max_positive_x_speed(self, value):
        self.__max_positive_x_speed = value

    @property
    def max_negative_x_speed(self):
        return self.__max_negative_x_speed

    @max_negative_x_speed.setter
    def max_negative_x_speed(self, value):
        self.__max_negative_x_speed = value

    @property
    def max_positive_y_speed(self):
        return self.__max_positive_y_speed

    @max_positive_y_speed.setter
    def max_positive_y_speed(self, value):
        self.__max_positive_y_speed = value

    @property
    def max_negative_y_speed(self):
        return self.__max_negative_y_speed

    @max_negative_y_speed.setter
    def max_negative_y_speed(self, value):
        self.__max_negative_y_speed = value

    @property
    def x_positive_acceleration(self):
        return self.__x_positive_acceleration

    @x_positive_acceleration.setter
    def x_positive_acceleration(self, value):
        self.__x_positive_acceleration = value

    @property
    def x_negative_acceleration(self):
        return self.__x_negative_acceleration

    @x_negative_acceleration.setter
    def x_negative_acceleration(self, value):
        self.__x_negative_acceleration = value

    @property
    def x_positive_deceleration(self):
        return self.__x_positive_deceleration

    @x_positive_deceleration.setter
    def x_positive_deceleration(self, value):
        self.__x_positive_deceleration = value

    @property
    def x_negative_deceleration(self):
        return self.__x_negative_deceleration

    @x_negative_deceleration.setter
    def x_negative_deceleration(self, value):
        self.__x_negative_deceleration = value

    @property
    def jump_power(self):
        return self.__jump_power

    @jump_power.setter
    def jump_power(self, value):
        self.__jump_power = value

    def __get_blit_pos(self):
        return int(round(self.x, 3)), int(round(self.y, 3))

    def blit(self, window):
        window.blit(self.current, self.__get_blit_pos())

    @property
    def width(self):
        return self.current.get_width()

    @property
    def height(self):
        return self.current.get_height()

    @property
    def size(self):
        return self.current.get_size()

    def __update_topleft(self, pos, update):
        if update == "x":
            self.__topleft = pos, self.__topleft[1]
        elif update == "y":
            self.__topleft = self.__topleft[0], pos
        elif update == "center":
            self.__topleft = pos[0] - self.width / 2, pos[1] - self.height / 2
        elif update == "top":
            self.__topleft = self.__topleft[0], pos
        elif update == "bottom":
            self.__topleft = self.__topleft[0], pos - self.height
        elif update == "left":
            self.__topleft = pos, self.__topleft[1]
        elif update == "right":
            self.__topleft = pos - self.width, self.__topleft[1]
        elif update == "topleft":
            self.__topleft = pos
        self.__topleft = round(self.__topleft[0], 3), round(self.__topleft[1], 3)

    @property
    def x(self):
        return self.topleft[0]

    @x.setter
    def x(self, value):
        self.__update_topleft(value, "x")

    @property
    def y(self):
        return self.topleft[1]

    @y.setter
    def y(self, value):
        self.__update_topleft(value, "y")

    @property
    def topleft(self):
        return self.__topleft

    @topleft.setter
    def topleft(self, value):
        self.__update_topleft(value, "topleft")

    @property
    def center(self):
        return self.__topleft[0] + self.width / 2, self.__topleft[1] + self.height / 2

    @center.setter
    def center(self, value):
        self.__update_topleft(value, "center")

    @property
    def top(self):
        return self.__topleft[1]

    @top.setter
    def top(self, value):
        self.__update_topleft(value, "top")

    @property
    def bottom(self):
        return self.__topleft[1] + self.height

    @bottom.setter
    def bottom(self, value):
        self.__update_topleft(value, "bottom")

    @property
    def left(self):
        return self.__topleft[0]

    @left.setter
    def left(self, value):
        self.__update_topleft(value, "left")

    @property
    def right(self):
        return self.__topleft[0] + self.width

    @right.setter
    def right(self, value):
        self.__update_topleft(value, "right")





