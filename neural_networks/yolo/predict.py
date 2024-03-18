from ultralytics import YOLO
import cv2
from PIL import Image

model = YOLO("runs/video_test/weights/best.pt")

model.predict(
    source='../../squash_rec/side_4.mp4',
    # source='../../house_videos/test1.mp4',
    conf=0.1,
    # show=True,
    project='predictions',
    name='video_test_5_epochs_low_conf',
    save=True,
    save_frames=True,
    max_det=1
)
