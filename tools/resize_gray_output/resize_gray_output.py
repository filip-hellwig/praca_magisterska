import cv2
import numpy as np
import os
import glob


def store_raw_images():
    pic_num = 1

    if not os.path.exists('outputs'):
        os.makedirs('outputs')

    # get the path/directory
    folder_dir = '../../image_processing/haar_cascade/dataset - Copy/neg'

    # iterate over files in
    # that directory
    for images in glob.iglob(f'{folder_dir}/*'):
        print(pic_num)
        img = cv2.imread(images, cv2.IMREAD_GRAYSCALE)
        resized_image = cv2.resize(img, (100, 100))
        cv2.imwrite("outputs/" + str(pic_num) + ".jpg", resized_image)
        pic_num += 1

store_raw_images()