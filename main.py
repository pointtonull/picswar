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
        debug("<-")

    def draw_clicked(self, w):
        debug(" -")

    def rigth_clicked(self, w, info):
        debug(" ->")

    def key_press(self, w, info):
        debug(w, info)
        debug(dir(info))
        debug(info.string)
        debug(info.hardware_keycode)
        debug(info.keyval)

    def destroy(self, w):
        gtk.main_quit()

def cerf(x):
    """Complementary error function."""
    z = abs(x)
    t = 1 / (1 + z / 2.)
    r = t * exp(- z ** 2 - 1.26551223 + t * (1.00002368 + t * (.37409196 + t *
        (.09678418 + t * (-.18628806 + t * (.27886807 + t * (-1.13520398 + t *
        (1.48851587 + t * (-.82215223 + t * .17087277)))))))))

    if (x >= 0.):
        return r
    else:
        return 2. - r

def cdf(x):
    return 1. - 0.5 * cerf(x / (2 ** 0.5))


def main():
    window = Mainwindow()
    gtk.main()

if __name__ == "__main__":
    exit(main())
