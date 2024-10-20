from flask import Flask, render_template, request
import requests
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# UI route to upload an image
@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # Save uploaded image
        if 'image' not in request.files:
            return 'No image uploaded', 400
        image = request.files['image']
        filename = secure_filename(image.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        image.save(filepath)

        # Send image to AI backend for object detection
        with open(filepath, 'rb') as img_file:
            response = requests.post('http://ai_backend:5001/detect', files={'image': img_file})

        # Handle the response from AI backend
        if response.status_code == 200:
            detections = response.json()['detections']
            return render_template('result.html', detections=detections, image=filename)
        else:
            return 'Error in object detection', 500

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
