from ultralytics import YOLO
import time

# start = time.time()
#
# p_model = 'l'
# p_epochs = 5
# p_w = 864
# # p_h = 640
# p_batch = 4
# p_images = 400
#
# model = YOLO(f"yolov8{p_model}.pt")
#
# model.train(
#     data='squash.yaml',
#     epochs=p_epochs,
#     imgsz=p_w,
#     batch=p_batch,
#     project='runs',
#     name=f'yolo_{p_images}_model={p_model}_epochs={p_epochs}_width={p_w}_batch={p_batch}',
#     exist_ok=True,
#     plots=True,
# )
#
# end = time.time()

f = open("time.txt", "a")

# print(end - start)
# f.write(f"{end - start}\n")

start = time.time()

p_model = 'l'
p_epochs = 10
p_w = 864
# p_h = 640
p_batch = 4
p_images = 400

model = YOLO(f"yolov8{p_model}.pt")

model.train(
    data='squash.yaml',
    epochs=p_epochs,
    imgsz=p_w,
    batch=p_batch,
    project='runs',
    name=f'yolo_{p_images}_model={p_model}_epochs={p_epochs}_width={p_w}_batch={p_batch}',
    exist_ok=True,
    plots=True,
)

end = time.time()
print(end - start)
f.write(f"{end - start}\n")

start = time.time()

p_model = 'l'
p_epochs = 15
p_w = 864
# p_h = 640
p_batch = 4
p_images = 400

model = YOLO(f"yolov8{p_model}.pt")

model.train(
    data='squash.yaml',
    epochs=p_epochs,
    imgsz=p_w,
    batch=p_batch,
    project='runs',
    name=f'yolo_{p_images}_model={p_model}_epochs={p_epochs}_width={p_w}_batch={p_batch}',
    exist_ok=True,
    plots=True,
)

end = time.time()
print(end - start)
f.write(f"{end - start}\n")

start = time.time()

p_model = 'l'
p_epochs = 20
p_w = 864
# p_h = 640
p_batch = 4
p_images = 400

model = YOLO(f"yolov8{p_model}.pt")

model.train(
    data='squash.yaml',
    epochs=p_epochs,
    imgsz=p_w,
    batch=p_batch,
    project='runs',
    name=f'yolo_{p_images}_model={p_model}_epochs={p_epochs}_width={p_w}_batch={p_batch}',
    exist_ok=True,
    plots=True,
)

end = time.time()
print(end - start)
f.write(f"{end - start}")

f.close()