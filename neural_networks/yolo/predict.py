from ultralytics import YOLO
import cv2
from PIL import Image

model = YOLO("runs/test2/weights/best.pt")

model.predict(
    source='../../squash_rec/side_2.mp4',
    # conf=0.75,
    # show=True,
    project='predictions',
    name='side_pred1',
    save=True,
    save_frames=True,
    max_det=1
)

# res = res.plot(line_width=1)
# res = res[:, :, ::-1]
# res = Image.fromarray(res)
# res.save("output")


