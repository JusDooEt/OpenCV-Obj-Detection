# Guide followed by @learncodebygaming
# https://github.com/learncodebygaming/opencv_tutorials/tree/master
import sys
import cv2 as cv
import numpy as np
import os
from time import time
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



loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # display the processed image
    points = vision_hex.find(screenshot, 0.7, 'points')
    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')

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
