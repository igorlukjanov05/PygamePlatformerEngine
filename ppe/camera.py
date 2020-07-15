import pygame
import ppe

SIMPLE = 0
SMOOTH = 1


class Camera:
    def __init__(self):
        self.__following: ppe.game_object.GameObject = None
        self.__topleft = None
        self.__width = None
        self.__height = None
        self.__x_speed = None
        self.__y_speed = None

        self.__topleft_anchor = None
        self.__bottomright_anchor = None

        self.__group = None
        self.__camera_type = SIMPLE

        self.__following_pos = None

    def init_pos(self, pos):
        self.__topleft = pos

    def init_group(self, group):
        self.__group = group

    def init_size(self, width, height):
        # in development
        self.__width = width
        self.__height = height

    def init_following(self, following, following_pos,
                       camera_type):
        self.__following = following
        self.__following_pos = following_pos
        self.__camera_type = camera_type

    def main(self):
        if self.__following is not None and self.__group is not None:
            if self.__camera_type == SIMPLE:
                self.__topleft = self.__following.center[0] - self.__width / 2, \
                                 self.__following.center[1] - self.__height / 2
                if self.__topleft[0] < self.__topleft_anchor.left:
                    self.__topleft = self.__topleft_anchor.left, self.__topleft[1]
                elif self.__topleft[0] + self.__width > self.__bottomright_anchor.right:
                    self.__topleft = self.__bottomright_anchor.right - self.__width, self.__topleft[1]

                if self.__topleft[1] < self.__topleft_anchor.top:
                    self.__topleft = self.__topleft[0], self.__topleft_anchor.top
                elif self.__topleft[1] + self.__height > self.__bottomright_anchor.bottom:
                    self.__topleft = self.__topleft[0], self.__bottomright_anchor.bottom - self.__height

    def draw(self, window):
        window.blit(self.__following.current, (self.__following.x - self.__topleft[0],
                                               self.__following.y - self.__topleft[1]))
        for obj in self.__group:
            window.blit(obj.current, (obj.x - self.__topleft[0], obj.y - self.__topleft[1]))

    @property
    def following_pos(self):
        return self.__following_pos

    @following_pos.setter
    def following_pos(self, value):
        self.__following_pos = value

    @property
    def camera_type(self):
        return self.__camera_type

    @camera_type.setter
    def camera_type(self, value):
        self.__camera_type = value

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value):
        self.__group = value

    @property
    def anchors(self):
        return {
                "topleft": self.__topleft_anchor,
                "bottomright": self.__bottomright_anchor
        }

    @anchors.setter
    def anchors(self, value):
        self.__topleft_anchor = value[0]
        self.__bottomright_anchor = value[1]

    @property
    def following(self):
        return self.__following

    @following.setter
    def following(self, obj: ppe.game_object.GameObject):
        self.__following = obj

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
    def topleft(self):
        return self.__topleft

    @topleft.setter
    def topleft(self, value):
        self.__topleft = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        # in development
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        # in development
        self.__height = value
