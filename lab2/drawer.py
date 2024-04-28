import cv2
import numpy as np
import random

figures = ["circle", "rectangle", "triangle", "pentagon"]


RED = (0, 0, 255)
#BLUE = (255, 0, 0)
BLUE = (255,0,0)
YELLOW = (0, 255, 255)


# Простенькая функция для рисования фигурок
#fill figures

def draw_figure(img, figure, x, y, r, color=(0, 0, 255)):
    if figure == "circle":

        cv2.circle(img, (x, y), r, color, thickness=5)
    elif figure == "rectangle":
        cv2.rectangle(img, (x-r, y-r), (x+r, y+r), color,thickness=5)
        #rounded_corners_rectangle(img, x-r, y-r, x+r, y+r, 20, color)
    elif figure == "triangle":
        points = np.array([[x, y-r], [x-r, y+r], [x+r, y+r]])
        cv2.polylines(img, [points], isClosed=True, color=color,thickness=5)
    elif figure == "pentagon":
        points = np.array([[x, y-r], [x-r, y], [x-r//2, y+r], [x+r//2, y+r], [x+r, y]])
        cv2.polylines(img, [points], isClosed=True, color=color,thickness=5)
    else:
        print("Invalid figure")

def main():
    img = np.zeros((1000, 1000, 3), np.uint8)

    points = []
    for i in range(200, 1000, 200):
        for j in range(200, 1000, 200):
            points.append((i,j))
            #cv2.circle(img, (i, j), 80, (0, 0, 255))
    #print(points

    used_points = []




    # рандомно расставляем фигурки

    for color in [RED, BLUE, YELLOW]:
        for fig in figures:
            point = random.choice(points)
            while point in used_points:
                point = random.choice(points)
            used_points.append(point)
            draw_figure(img, fig, point[0], point[1], 80, color)

    cv2.imshow("image", img)
    #cv2.waitKey(0)
    cv2.imwrite("output.jpg", img)

if __name__ == "__main__":
    main()
