import pygame
import ppe.game_object


def check_collision(first: ppe.game_object.GameObject,
                    second: ppe.game_object.GameObject):
    # x
    if first.bottom > second.top and first.top < second.bottom:
        if first.right <= second.left:
            if first.right + first.x_speed > second.left + second.x_speed:
                first.right = second.left + second.x_speed
                first.x_speed = 0
        elif first.left >= second.right:
            if first.left + first.x_speed < second.right + second.x_speed:
                first.left = second.right + second.x_speed
                first.x_speed = 0
    # y
    if first.right > second.left and first.left < second.right:
        if first.bottom <= second.top:
            if first.bottom + first.y_speed > second.top + second.y_speed:
                first.on_ground = True
                first.bottom = second.top + second.y_speed
                first.y_speed = 0
        elif first.top >= second.bottom:
            if first.top + first.y_speed < second.bottom + second.y_speed:
                first.top = second.bottom
                first.y_speed = 0


def touch_the_left_side(first: ppe.game_object.GameObject,
                        second: ppe.game_object.GameObject):
    if first.bottom > second.top and first.top < second.bottom:
        if first.right == second.left:
            return True
        return False


def touch_the_right_side(first: ppe.game_object.GameObject,
                         second: ppe.game_object.GameObject):
    if first.bottom > second.top and first.top < second.bottom:
        if first.left == second.right:
            return True
        return False


def touch_the_bottom_side(first: ppe.game_object.GameObject,
                          second: ppe.game_object.GameObject):
    if first.right > second.left and first.left < second.right:
        if first.top == second.bottom:
            return True
        return False


def touch_the_top_side(first: ppe.game_object.GameObject,
                       second: ppe.game_object.GameObject):
    if first.right > second.left and first.left < second.right:
        if first.bottom == second.top:
            return True
        return False


def touch(first: ppe.game_object.GameObject,
          second: ppe.game_object.GameObject):
    return touch_the_top_side(first, second) \
           or touch_the_bottom_side(first, second) \
           or touch_the_left_side(first, second) \
           or touch_the_right_side(first, second)