import cv2

from ultralytics import YOLO

# Load the YOLO11 model
model = YOLO("yolo11s.pt")

# Train the model on HomeObjects-3K dataset
model.train(data="HomeObjects-3K.yaml", epochs=100, imgsz=640)

# Save the trained model (best weights)
# The best model is usually saved as 'runs/detect/train/weights/best.pt' by Ultralytics
# Optionally, you can copy or rename it here if needed
print("Training complete. The best model is saved in 'runs/detect/train/weights/best.pt'.")
