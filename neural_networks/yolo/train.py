from ultralytics import YOLO

model = YOLO("yolov8m.pt")

model.train(
    data='squash.yaml',
    epochs=20,
    imgsz=(640,640),
    batch=4,
    project='runs',
    name='test',
    exist_ok=True,
    plots=True,
)