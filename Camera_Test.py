import cv2

cam = cv2.VideoCapture(0)

#cv2.namedWindow("video", cv2.WINDOW_NORMAL)
#cv2.resizeWindow("video", 600, 600)


while(True):
    _, frame = cam.read()
    cv2.namedWindow("video", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("video", 1024, 600)
    cv2.imshow("video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.imwrite("saved.png", frame)
        break

cam.release()
cv2.destroyAllWindows()









print("done")
