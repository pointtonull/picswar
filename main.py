#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import gtk
from gtk import glade
from debug import debug

class Mainwindow:

    def __init__(self):
        self.wtree = glade.XML("gui.glade")

        self.rigth = self.wtree.get_widget("rigth")
        self.left = self.wtree.get_widget("left")

        self.wtree.signal_autoconnect({
            "on_main_key_press_event": self.key_press,
            "on_main_destroy": self.destroy,
            "on_left_button_press_event": self.left_clicked,
            "on_rigth_button_press_event": self.rigth_clicked,
        })


    def left_clicked(self, w, info):
        debug(w, info)

    def rigth_clicked(self, w, info):
        debug(w, info)

    def key_press(self, w, info):
        debug(w, info)
        debug(dir(info))
        debug(info.string)
        debug(info.hardware_keycode)
        debug(info.keyval)

    def destroy(self, w):
        gtk.main_quit()


def main():
    window = Mainwindow()
    gtk.main()

if __name__ == "__main__":
    exit(main())
