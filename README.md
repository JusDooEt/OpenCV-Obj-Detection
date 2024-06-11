# OpenCV Object Detection Application
# Latest Update
HSV (Hue, saturation, value) filtering has now been added to the program. This will allow the program to adjust the HSV values of the image being searched. This will allow the program to isolate specific objects based on their HSV value which will prevent a majority of false positive matches from occurring. A simple OpenCV built in GUI is also added to allow the programmer to experiment with all of the HSV values to find the best filter to use when matching a template image.
- HsvFilter Class
  - This is a very simple class that is used to store all the HSV values for a specific filter.
  - This is a more organized way to store and organize multiple different filters for different template images.
## Example Image
![image](https://github.com/JusDooEt/OpenCV-Obj-Detection/assets/152052216/caf51b4f-1cc1-4434-8faf-27315ac9864d)


# About
This application was created by following a guide created by [learncodebygaming](https://github.com/learncodebygaming/opencv_tutorials). The application will detect a template image and track it in real time by repeatedly capturing screenshots and using OpenCV to match the template image. This can be used as a macro for games or tedious or redundant clicking functions and will be able to act as a click bot. User will be able to upload a template image and choose whether to detect or detect and click the matched image. In the future more features like creating keyboard macros will be implemented.

# Output Example
![image](https://github.com/JusDooEt/OpenCV-Obj-Detection/assets/152052216/e972638d-b791-4a97-b369-f9f94dd2755d)
A template image of a hexagon is used and it shown being tracked by the application in the image above by the pink crosshair.

# Classes
## Vision
- This class contains four properties
  - needle_img
    - This property will store the image that is attempting to be 'matched' to the template
  - needle_w
    - The width of needle_img
  - needle_h
    - The height of needle_img
  - method
    - How the class will react if a match is found
    - 'rectangles' will draw a border around the 'match'
    - 'points' will draw a crosshair around the 'match'
- Constructor
  - Uses the arguments passed to initialize class properties
- def find(self, haystack_img, threshold=0.5, debug_mode=None)
  - This class method will use the OpenCV match() method to attempt to 'match' the template with the window image
  - It will return an array of rectangle coordinate and sizes around the 'matched' image
- def get_click_points(self, rectangles)
  - This method receives the array of rectangle returned by the find() method
  - It will return an array of center points for all the rectangle that were passed to the method
- def draw_rectangles(self, haystack_img, rectangles)
  - This method receives the array of rectangle returned by the find() method
  - The method will 'draw' the rectangles passed onto the that was also passed
  - It will return the edited image
- def draw_crosshairs(self, haystack_img, points)
  - This has the same function has the draw_rectangles() method but will draw a crosshair instead
- def init_control_gui(self)
  - Initializes the GUI of sliders to control the image HSV values
- def get_hsv_filter_from_controls(self)
  - Uses the trackbar values from the GUI to create a HsvFilter class and returns it
- def apply_hsv_filter(self, original_image, hsv_filter=None)
  - This will apply the HsvFilter class values to the image passed to the method
- def shift_channel(self, c, amount)
  - Helper function to shift HSV values when needed.
 

## WindowCapture
- This class contains seven properties
  - w
    - window width
  - h
    - window height
  - hwnd
    - window handle/name
  - cropped_x
    - The amount of pixels cropped on the x-axis
  - cropped_y
    -  The amount of pixels cropped on the y-axis
  -  offset_x
    - The amount of pixels offset of the original window on the x-axis
  - offset_y
    - The amount of pixels offset of the original window on the y-axis
- Constructor
  - The constructor will initialize all of the class properties
  - If a window_name is passed then the constructor will attempt to find said window
    - If the window is not found an exception will be thrown and the program will exit
  - The title bar and window border is cropped and the measurements are stored in the relevant properties
- def get_screenshot(self)
  - This class method will return a single frame of the window that is targeted by the class and returns it
- @staticmethod def list_window_names()
  - This will list the available windows
- def get_screen_position(self, pos)
  - Returns the window's position






