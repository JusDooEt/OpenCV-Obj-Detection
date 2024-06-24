# Guide followed by @learncodebygaming
# https://github.com/learncodebygaming/opencv_tutorials/tree/master
# Test game: https://www.crazygames.com/game/shoot-bounce
import sys
import cv2 as cv
import numpy as np
import os
import pyautogui
from time import time, sleep
from WindowCapture import WindowCapture
from Vision import Vision

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Base

wincap = WindowCapture()
# initialize the Vision class
vision_hex = Vision('hex.png')

vision_hex.init_control_gui()

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # pre-process the mage
    output_image = vision_hex.apply_hsv_filter(screenshot)

    # Obj Detection
    rectangles = vision_hex.find(screenshot, 0.7)
    points = vision_hex.get_click_points(rectangles)
    # Draw Crosshairs on image
    output_image = vision_hex.draw_crosshairs(screenshot, points)

    # Displaye processed image
    cv.imshow('Matches',  output_image)

    # take bot actions
    if len(rectangles) > 0:
        targets = points
        target = wincap.get_screen_position(targets[0])
        pyautogui.moveTo(x = target[0], y = target[1]);
        pyautogui.click()
        sleep(1)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')

# class Base(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.ui = Ui_Base()
#         self.ui.setupUi(self)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     widget = Base()
#     widget.show()
#     sys.exit(app.exec())
