import cv2
import os
import numpy as np
import time

# VALUES DEPENDING ON VIDEO

# Side Video
output_video_name = 'outputs/output_side.mp4'
input_video = cv2.VideoCapture('../../squash_rec/testing_video.mp4')
is_side = True
frame_rate = 25
max_frame = 10 * frame_rate
start_m_second = 0 * 1000
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

face_cascade = cv2.CascadeClassifier('dataset/classifier/cascade.xml')

frame_num = 0
start_time = time.time()

while input_video.isOpened():
    ret, frame = input_video.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

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