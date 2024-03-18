from ultralytics import YOLO

model = YOLO("yolov8m.pt")

model.train(
    data='squash.yaml',
    epochs=10,
    imgsz=(640,640),
    batch=4,
    project='runs',
    name='video_test_10_epochs_200',
    exist_ok=True,
    plots=True,
)