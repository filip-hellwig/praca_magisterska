import cv2
import os
import numpy as np
import time

video_name = 'output.mp4'

cap = cv2.VideoCapture('../squash_rec/cam1-1.mp4')
height = 0
width = 0
if cap.isOpened():
    ret, frame = cap.read()
    height, width, layers = frame.shape

s = 0

codec = cv2.VideoWriter.fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter(video_name, codec, 30, (width, height))

start = time.time()

while cap.isOpened():
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    video.write(frame)

    # Convert to grayscale.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Blur using 3 * 3 kernel.
    gray_blurred = cv2.blur(gray, (3, 3))

    ret, thresh = cv2.threshold(gray_blurred, 100, 255, cv2.THRESH_BINARY)
    # ret, thresh = cv2.threshold(gray_blurred, 80, 255, cv2.THRESH_BINARY)

    # cv2.imshow("Detected Circle", thresh)
    # cv2.waitKey(0)

    # Apply Hough transform on the blurred image.
    detected_circles = cv2.HoughCircles(thresh,
                                        cv2.HOUGH_GRADIENT, 1, 20, param1=100,
                                        param2=10, minRadius=40, maxRadius=80)
    # detected_circles = cv2.HoughCircles(thresh,
    #                                     cv2.HOUGH_GRADIENT, 1, 20, param1=100,
    #                                     param2=10, minRadius=40, maxRadius=50)

    # Draw circles that are detected.
    if detected_circles is not None:

        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))

        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]

            # Draw the circumference of the circle.
            cv2.circle(frame, (a, b), r, (0, 255, 0), 2)

            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)
            video.write(frame)

    if s == 10:
        end = time.time()
        print((end - start)*10/60)

    if s == 100:
        break
    s = s+1
    print(s)

cv2.destroyAllWindows()
cap.release()
video.release()