
########### COLOR IDENTIFICATION IN THE IMAGE #########################

#########################################################################
#   Author : Sachin Lodhi                                               #
#   Track  : Computer Vision and Internet of Things                     #
#   Batch  : June 2021                                                  #
#   Assignment 2 : COLOR IDENTIFICATION IN THE IMAGE
#   Graduate Rotational Internship Program,                             #
#   The Spark Foundation, June 2021                                     #
#                                                                       #
#########################################################################


import cv2 as cv
import colorPredictor as cp
import argparse
# Argument Parsing
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--imagePath", required=True,
                    help = "Full path of the image file that is to be processed for color detection")
args = vars(parser.parse_args())



# global variables declaration
clicked = False
r = g = b = xpos = ypos = 0


# initilaization with class
class colorDetection():
    def __init__(self, img):
        self.img = img


# function to get x,y coordinates of mouse double click
    def draw_function(self,event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDBLCLK:
            global b, g, r, xpos, ypos, clicked
            clicked = True
            xpos = x
            ypos = y
            b, g, r = self.img[y, x]
            b = int(b)
            g = int(g)
            r = int(r)




def detect(img):
    global clicked, xpos, ypos, r,g,b
    # img = cv.imread("colorpic.jpg")
    cDetector = colorDetection(img)
    cv.namedWindow('image')
   # Binding a function with leftbutton click
    cv.setMouseCallback('image', cDetector.draw_function)

    while (1):

        cv.imshow("image", img)
        if (clicked):
            # Rectangular Boundary
            cv.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

            # Color Information with Possible Color Name and its RGB value
            text = 'Best Possible Color : ' + cp.convert_rgb_to_names((r,g,b)) +  ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

            # Writing text on image
            cv.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv.LINE_AA)

            # for light colors the information would be in dark color
            if (r + g + b >= 600):
                cv.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv.LINE_AA)

            clicked = False

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    img = cv.imread(args['imagePath'])
    detect(img)
