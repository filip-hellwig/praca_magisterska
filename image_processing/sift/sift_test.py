import cv2
import os
import numpy as np
import time

start = time.time()

# METHOD PARAMS

p_nfeatures = 8
p_nOctaveLayers = 3
p_contrastThreshold = 0.04
p_edgeThreshold = 4
p_sigma = 2
p_enable_precise_upscale = True

# VALUES DEPENDING ON VIDEO

# Side Video
output_video_name = f'outputs/sift;nfeatures={p_nfeatures};nOctaveLayers={p_nOctaveLayers};contrastThreshold={p_contrastThreshold};edgeThreshold={p_edgeThreshold};sigma={p_sigma};epu={p_enable_precise_upscale}.mp4'
input_video = cv2.VideoCapture('../../squash_rec/testing_video.mp4')
is_side = True
frame_rate = 25
max_frame = 10 * frame_rate
start_m_second = 0 * 1000
playback_frame_rate = 1

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
frame_to_sub = cv2.imread('first_frame/first_frame.jpg', cv2.IMREAD_COLOR)
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
detected_num = 0
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

    sift = cv2.SIFT_create(nfeatures=p_nfeatures, nOctaveLayers=p_nOctaveLayers, contrastThreshold=p_contrastThreshold,
                           edgeThreshold=p_edgeThreshold, sigma=p_sigma, enable_precise_upscale=p_enable_precise_upscale)
    kp = sift.detect(gray, None)

    x_mem = 0
    y_mem = 0
    for kp_s in kp:
        [x, y] = kp_s.pt

        if x != x_mem or y != y_mem:
            detected_num = detected_num + 1
            x_mem = x
            y_mem = y

    frame = cv2.drawKeypoints(frame, kp, frame, color=(0, 0, 255), flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)

    if is_side:
        frame = cv2.rotate(frame, cv2.ROTATE_180)

    cv2.imwrite('sift_example.jpg', frame)
    video_writer.write(frame)

    if frame_num == 10:
        end_time = time.time()
        print((end_time - start_time) * max_frame / 60 / 10)

    if frame_num == max_frame:
        break

    frame_num = frame_num + 1
    print(frame_num)

print(detected_num)
end = time.time()
print(end - start)

cv2.destroyAllWindows()
input_video.release()
video_writer.release()