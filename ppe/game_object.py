import pygame


class GameObject(object):
    def __init__(self, current=None, topleft=None):
        self.__topleft = topleft
        self.current = current

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
        elif update == "topleft":
            self.__topleft = pos

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
        return self.__topleft[0] + self.width / 2, self.__topleft[1] + self.height / 2

    @top.setter
    def top(self, value):
        self.__update_topleft(value, "top")






