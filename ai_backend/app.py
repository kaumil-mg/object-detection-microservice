from flask import Flask, request, jsonify
import torch
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

@app.route('/detect', methods=['POST'])
def detect_objects():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    # Read the image file
    file = request.files['image'].read()
    img = Image.open(io.BytesIO(file)).convert('RGB')
    img_np = np.array(img)

    # Perform object detection
    results = model(img_np)

    # Get bounding boxes and labels
    detections = []
    for *box, conf, cls in results.xyxy[0]:  # bounding box, confidence, class
        detections.append({
            'box': [int(x) for x in box],  # Convert to int
            'confidence': float(conf),
            'class': int(cls)
        })

    return jsonify({'detections': detections})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
