#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import gtk
from gtk import glade
from debug import debug


class Mainwindow:
   def __init__(self):
      self.xml = glade.XML("gui.glade", None, None)
      self.xml.signal_connect("on_window1_key_press_event", self.key_press)
      self.xml.signal_connect("on_window1_key_release_event", self.key_release)
      self.xml.signal_connect("on_window1_destroy", lambda w: gtk.main_quit())

#      self.spin = self.xml.get_widget("fahr")
#      self.result = self.xml.get_widget("celsius")

   def key_press(self, w):
      fahr = self.spin.get_value_as_int();
      cent = (fahr - 32) / 1.8
      texto = "%.2f C" % cent
      self.result.set_label(texto)

   def key_press(self, w):
      fahr = self.spin.get_value_as_int();
      cent = (fahr - 32) / 1.8
      texto = "%.2f C" % cent
      self.result.set_label(texto)

 if __name__ == "__main__":
   ftoc = FtoC()
   gtk.main()


def main():

if __name__ == "__main__":
    exit(main())
