#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import gtk
from gtk import glade
from debug import debug
from math import exp

class Mainwindow:

    def __init__(self):
        self.wtree = glade.XML("gui.glade")

        self.rigth = self.wtree.get_widget("rigth")
        self.left = self.wtree.get_widget("left")

        self.wtree.signal_autoconnect({
            "on_draw_clicked": self.draw_clicked,
            "on_left_button_press_event": self.left_clicked,
            "on_main_destroy": self.destroy,
            "on_main_key_press_event": self.key_press,
            "on_right_button_press_event": self.rigth_clicked,
        })


    def left_clicked(self, w, info):
        return self.left_win()

    def draw_clicked(self, w):
        return self.draw()

    def rigth_clicked(self, w, info):
        return self.right_win()

    def key_press(self, w, info):
        if info.hardware_keycode == 113:
            return self.left_win()
        elif info.hardware_keycode == 114:
            return self.right_win()
        elif info.hardware_keycode == 111:
            return self.rematch()
        elif info.hardware_keycode == 116:
            return self.draw()
        elif info.hardware_keycode == 24:
            return self.destroy()
        else:
            return debug(info.hardware_keycode)

    def destroy(self, w=None):
        return gtk.main_quit()

    def left_win(self):
        return debug("<-")

    def right_win(self):
        return debug(" ->")

    def draw(self):
        return debug(" -")

    def rematch(self):
        return debug("Rematch")


def main():
    window = Mainwindow()
    gtk.main()


if __name__ == "__main__":
    exit(main())
