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

            # cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
            cv.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

            # Creating text string to display( Color name and RGB values )
            # text = cDetector.getColorName(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
            text = 'Best Possible Color : ' + cp.convert_rgb_to_names((r,g,b)) +  ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

            # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
            cv.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv.LINE_AA)

            # For very light colours we will display text in black colour
            if (r + g + b >= 600):
                cv.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv.LINE_AA)

            clicked = False


        # Break the loop when user hits 'esc' key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()

if __name__ == '__main__':
    img = cv.imread(args['imagePath'])
    detect(img)