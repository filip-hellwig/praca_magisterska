import cv2
import os
import numpy as np
import time

# VALUES DEPENDING ON VIDEO

# Side Video
output_video_name = 'outputs/output_side_sub.mp4'
input_video = cv2.VideoCapture('../../squash_rec/side_2.mp4')
is_side = True
frame_rate = 25
max_frame = 10 * frame_rate
start_m_second = 70 * 1000
playback_frame_rate = 2

# Front Video
# output_video_name = 'output_front.mp4'
# input_video = cv2.VideoCapture('../../squash_rec/front_2.mp4')
# is_side = False
# frame_rate = 30
# max_frame = 1 * frame_rate
# start_m_second = 60 * 1000


# REST
input_video_height = 0
input_video_width = 0
frame_to_sub = cv2.imread('first_frame/out_1.jpg', cv2.IMREAD_COLOR)
frame_to_sub = cv2.cvtColor(frame_to_sub, cv2.COLOR_BGR2GRAY)

if input_video.isOpened():
    print(input_video.set(cv2.CAP_PROP_POS_MSEC, start_m_second))
    print(input_video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(input_video.get(cv2.CAP_PROP_POS_MSEC))
    print(input_video.get(cv2.CAP_PROP_FPS ))

    ret, frame = input_video.read()
    input_video_height, input_video_width, layers = frame.shape

codec = cv2.VideoWriter.fourcc('m', 'p', '4', 'v')
video_writer = cv2.VideoWriter(output_video_name, codec, playback_frame_rate, (input_video_width, input_video_height))
# video_writer = cv2.VideoWriter(output_video_name, codec, playback_frame_rate, (input_video_width, input_video_height), isColor=False)

frame_num = 0
start_time = time.time()

while input_video.isOpened():
    ret, frame = input_video.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Convert to grayscale.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.subtract(frame_to_sub, gray)

    # Blur using 3 * 3 kernel.
    gray_blurred = cv2.blur(gray, (3, 3))

    # ret, thresh = cv2.threshold(gray_blurred, 100, 255, cv2.THRESH_BINARY)

    # Apply Hough transform on the blurred image.
    detected_circles = cv2.HoughCircles(gray_blurred,
                                        cv2.HOUGH_GRADIENT, 1, 100, param1=100,
                                        param2=5, minRadius=1, maxRadius=10)

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

    if is_side:
        frame = cv2.rotate(frame, cv2.ROTATE_180)

    video_writer.write(frame)

    if frame_num == 10:
        end_time = time.time()
        print((end_time - start_time) * max_frame / 60 / 10)

    if frame_num == max_frame:
        break

    frame_num = frame_num + 1
    print(frame_num)

cv2.destroyAllWindows()
input_video.release()
video_writer.release()