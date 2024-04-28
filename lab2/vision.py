#
#   Copyright mas0yama t.me/cereshouse
#
import numpy as np
import matplotlib.pyplot as plt
import cv2


# Вариант 16
#   figure = 1 - круг
#  цвет = 16 mod 3 + 1 = 2 - синий



# Каждый должен оставить свой след и чего-то добиться

def main():
    src = cv2.imread("output.jpg", cv2.IMREAD_COLOR)
    #cv2.imshow("image", src)
    #cv2.waitKey(0)


    # Hue Saturation Value
    ##blue_low = np.array([220, 100, 20])
    #blue_high = np.array([240, 100, 90])


    #HSV boundaries for blue

    blue_low = np.array([100, 150,0])
    blue_high = np.array([140, 255, 255])
    #red_lower = np.array([0, 0, 50])
    #red_higher = np.array([50, 50, 255])
    mask = cv2.inRange(src, 20, 150)
    #cv2.imshow("mask", mask)
    selection = cv2.bitwise_and(src, src, mask=mask)
    #cv2.imshow("selection", selection)
    ## need to make selection brighter

    gray = cv2.cvtColor(selection, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("sel",gray)
    canny = cv2.Canny(cv2.blur(mask,(3,3) ),1, 255)
    cv2.imshow("canny",canny)
    # cv::findContours - находит контуры в бинарном изображении
    # params:
    #
    contours = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    #cv2.drawContours( src, contours, -1, (0,255,0), 4 )
    for cont in contours:
        # вычисление периметра и определение количества углов
        # Calculates a contour perimeter or a curve length.
        # The function computes a curve length or a closed contour perimeter.
        sm = cv2.arcLength(cont, True)
        
        
        #Approximates a polygonal curve(s) with the specified precision.

        apd = cv2.approxPolyDP(cont, 0.03 * sm, True)
        print(len(apd))
        # выделение контуров
        if len(apd) == 8:
            cv2.drawContours(src, [cont], -1, (251, 0, 255), 10)
    #cv2.imshow("selection", canny)
    cv2.waitKey(0)
    cv2.imwrite("selected.jpg",src)
    #cv2.waitKey(0)
    #cv2.imshow("mask",mask)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()