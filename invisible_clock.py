import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    # take each frame
    ret, frame = cap.read()
    if ret:
        # converting rgb to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # cv2.imshow("hsv", hsv)

        # getting hsv values
        red = np.uint8([[[0, 0, 255]]])  # bgr value of red
        # get hsv value of red from bgr
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        print(hsv_red)

        # threshold the hsv value to get only red colors
        # lower: hue-10,100,100
        l_red = np.array([0, 100, 100])
        # higher: hue+10,255,255
        u_red = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, l_red, u_red)
        # cv2.imshow("mask", mask)

        part1 = cv2.bitwise_and(back, back, mask=mask)
        # cv2.imshow("part1", part1)

        kernel = np.ones((5, 5), np.uint8)
        erosion = cv2.erode(mask, kernel, iterations=1)
        dilation = cv2.dilate(mask, kernel, iterations=1)

        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        # cv2.imshow('erosion', erosion)
        # cv2.imshow('dilation', dilation)
        # cv2.imshow('opening', opening)
        # cv2.imshow('closing', closing)

        # mask = cv2.bitwise_not(mask)

        part2 = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(closing))
        # cv2.imshow("mask", part2)

        cv2.imshow("cloak", part1+part2)

        if cv2.waitKey(5) == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
