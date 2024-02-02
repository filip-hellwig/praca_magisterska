import numpy as np
import cv2

cap = cv2.VideoCapture('../squash_rec/side_2.mp4')
output_filename = "outputs/out_"
output_extension = ".jpg"

file_num = 1

while cap.isOpened():
    ret, frame = cap.read()

    # if file_num == 10:
    #     break

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    output = output_filename + str(file_num) + output_extension

    cv2.imwrite(output, frame)

    file_num += 1

    print(file_num)

cap.release()
cv2.destroyAllWindows()