from ultralytics import YOLO
import cv2
from PIL import Image
import time

start = time.time()

p_model = 'l'
p_epochs = 20
p_w = 640
# p_h = 640
p_batch = 4
p_images = 400

model = YOLO(f"runs/yolo_{p_images}_model={p_model}_epochs={p_epochs}_width={p_w}_batch={p_batch}/weights/best.pt")
# model = YOLO(f"runs/best-best/weights/best.pt")

model.predict(
    source='../../squash_rec/testing_video.mp4',
    # source='../../house_videos/test1.mp4',
    conf=0.01,
    # show=True,
    project='predictions',
    name=f'yolo_{p_images}_model={p_model}_epochs={p_epochs}_width={p_w}_batch={p_batch}',
    save=True,
    save_frames=True,
    max_det=1,
    show_labels=False,
    show_conf=False,
    imgsz=p_w
)

end = time.time()
print(end - start)
