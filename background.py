import cv2
# webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read()  # reading from webcam
    if ret:
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord("q"):
            # save image
            cv2.imwrite("image.jpg", back)
            break

cap.release()
cv2.destroyAllWindows()
