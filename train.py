import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from ultralytics import YOLO
model = YOLO('yolov8_SPD_att.yaml')
model.train(data='your data.yaml', workers=0, epochs=500, batch=8)




