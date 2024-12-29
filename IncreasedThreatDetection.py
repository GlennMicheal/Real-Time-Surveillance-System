import cv2
import numpy as np

# Load pre-trained deep learning model (e.g., YOLO for object detection)
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Video capture from surveillance camera or local video file
cap = cv2.VideoCapture("video_source.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Pre-process the frame and apply the object detection model
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    detections = net.forward(output_layers)

    for detection in detections:
        for obj in detection:
            scores = obj[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # Threshold for suspicious activities
                center_x = int(obj[0] * frame.shape[1])
                center_y = int(obj[1] * frame.shape[0])
                width = int(obj[2] * frame.shape[1])
                height = int(obj[3] * frame.shape[0])

                # Draw a bounding box and label the object
                cv2.rectangle(frame, (center_x - width // 2, center_y - height // 2),
                              (center_x + width // 2, center_y + height // 2), (0, 255, 0), 2)
                cv2.putText(frame, f"Object {class_id}", (center_x, center_y),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Real-Time Threat Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
